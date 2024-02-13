import json
from random import Random

# Helpers

def position_to_grid(position):
    grid = []

    for axis in range(0, 3):
        n = (position[axis] - MAZE_ORIGIN[axis]) // UNIT_SIZE
        n = max(n, 0)
        n = min(n, GRID_SIZE[axis] - 1)
        grid.append(int(n))

    return grid

def grid_to_position(grid):
    return [
        MAZE_ORIGIN[axis] + ((grid[axis] + 0.5) * UNIT_SIZE) for axis in range(0, 3)
    ]

# Parameters

MAZE_CENTER = (164.5, 21.4, -87.7)
MAZE_START = (164.7, 21.4, -98.8)
MAZE_SCALE = (40.0, 70.0, 20.0)
UNIT_SIZE = 5.5
WALL_WIDTH = 0.2

OBJECT_LIMIT = 1000

# Calculated parameters

MAZE_ORIGIN = [
    MAZE_CENTER[axis] - MAZE_SCALE[axis]/2 for axis in range(0, 3)
]

GRID_SIZE = [
    max(int(n // UNIT_SIZE), 1) for n in MAZE_SCALE
]

START = position_to_grid(MAZE_START)

# Generate Maze

class MazeWall:
    def __init__(self):
        self.mutable = True
        self.state = True
    
    def carve(self):
        if self.mutable:
            self.state = False

    def __str__(self) -> str:
        return f"{self.state} (mut={self.mutable})"

    def __repr__(self):
        return self.__str__()

class MazeNode:
    def __init__(self):
        self.visited = False

class Maze:
    # [x][y][z]
    nodes: list[list[list[MazeNode]]]

    # [axis][x][y][z]
    walls: list[list[list[list[MazeWall]]]]

    rng: Random

    def __init__(self, seed):
        self.rng = Random(seed)

        self.nodes = []
        for x in range(0, GRID_SIZE[0]):
            self.nodes.append([])
            for y in range(0, GRID_SIZE[1]):
                self.nodes[x].append([])
                for _ in range(0, GRID_SIZE[2]):
                    self.nodes[x][y].append(MazeNode())

        self.walls = []
        for axis in range(0, 3):
            self.walls.append([])
            x_size = GRID_SIZE[0]
            if axis == 0:
                x_size += 1

            for x in range(0, x_size):
                self.walls[axis].append([])
                y_size = GRID_SIZE[1]
                if axis == 1:
                    y_size += 1

                for y in range(0, y_size):
                    self.walls[axis][x].append([])
                    z_size = GRID_SIZE[2]
                    if axis == 2:
                        z_size += 1

                    for _ in range(0, z_size):
                        self.walls[axis][x][y].append(MazeWall())

    # Where fn:
    #   def fn(axis, x, y, z, wall)
    def walls_iter(self, fn):
        for axis in range(0, len(self.walls)):
            for x in range(0, len(self.walls[axis])):
                for y in range(0, len(self.walls[axis][x])):
                    for z in range(0, len(self.walls[axis][x][y])):
                        wall = self.walls[axis][x][y][z]
                        fn(axis, (x, y, z), wall)

    # Where fn:
    #   def fn(position, node)
    def nodes_iter(self, fn):
        for x in range(0, len(self.nodes)):
            for y in range(0, len(self.nodes[x])):
                for z in range(0, len(self.nodes[x][y])):
                    node = self.nodes[x][y][z]
                    fn((x, y, z), node)

    def place_exterior(self):
        def maybe_place_wall(axis, position, wall: MazeWall):
            if position[axis] == 0 or position[axis] == (GRID_SIZE[axis] - 1):
                wall.mutable = False

        self.walls_iter(maybe_place_wall)

    def node_for_position(self, position) -> MazeNode:
        x, y, z = position
        return self.nodes[x][y][z]

    def node_neighbors(self, position) -> list[tuple]:
        neighbors = []
        for axis in range(0, 3):
            value = position[axis]

            if value > 0:
                neighbor = list(position)
                neighbor[axis] -= 1
                neighbors.append(neighbor)

            if value < (GRID_SIZE[axis] - 1):
                neighbor = list(position)
                neighbor[axis] += 1
                neighbors.append(neighbor)

        return neighbors

    def wall_for_position(self, axis, position) -> MazeWall:
        x, y, z = tuple(position)
        return self.walls[axis][x][y][z]

    def node_walls(self, position) -> list[MazeWall]:
        walls = []

        for axis in range(0, 3):
            neighbor = list(position)
            walls.append(self.wall_for_position(axis, neighbor))
            neighbor[axis] += 1
            walls.append(self.wall_for_position(axis, neighbor))

        return walls

    def carve_entrance(self):
        start = self.node_for_position(START)
        start.visited = True

        for position in self.node_neighbors(START):
            node = self.node_for_position(position)
            node.visited = True

        for wall in self.node_walls(START):
            wall.carve()

    def process_order(self) -> list[tuple]:
        process_order = []
        def collect_node_position(position, node: MazeNode):
            if not node.visited:
                process_order.append(position)
        self.nodes_iter(collect_node_position)
        self.rng.shuffle(process_order)
        return process_order

    def connecting_wall(self, pos1, pos2) -> MazeWall:
        diff = [
            pos1[0] - pos2[0],
            pos1[1] - pos2[1],
            pos1[2] - pos2[2],
        ]

        wall_axis = 0

        if abs(sum(diff)) != 1:
            raise Exception(f"{pos1} <--> {pos2} is not something that can be carved")

        if abs(diff[0]) == 1:
            wall_axis = 0
        elif abs(diff[1]) == 1:
            wall_axis = 1
        elif abs(diff[2]) == 1:
            wall_axis = 2
        else:
            assert False

        wall_pos = list(pos1)
        wall_pos[wall_axis] = max(pos1[wall_axis], pos2[wall_axis])

        return self.wall_for_position(wall_axis, wall_pos)

    def carve_from_node(self, node_pos):
        history: list[tuple] = []
        current_pos = node_pos
        dead_end = False

        while not dead_end:
            # Visit node
            current_node = self.node_for_position(current_pos)
            if current_node.visited:
                # print(f"Reconnected at {current_pos}")
                break
            current_node.visited = True

            options = self.node_neighbors(current_pos)
            if len(options) == 0:
                raise Exception(f"{current_pos} has no neighbors")

            options = list(filter(lambda pos: pos not in history, options))

            if len(options) == 0:
                print(f"Dead End: {current_pos}")
                return

            option_pos = self.rng.choice(options)

            # Open path to node
            wall = self.connecting_wall(current_pos, option_pos)
            # print(f"Carve {current_pos} -> {option_pos}")
            wall.carve()

            # Move to node
            current_pos = option_pos
            history.append(current_pos)
            dead_end = False

    def furthest_exterior_node_from(self, node_pos: tuple, history: list[tuple]):
        def valid_option(pos):
            if pos in history:
                return False

            return not self.connecting_wall(node_pos, pos).state

        def is_exterior(pos):
            for axis in range(0, 3):
                if pos[axis] == GRID_SIZE[axis] - 1:
                    return True

                # The floor is not a valid exit
                if axis != 2 and pos[axis] == 0:
                    return True 

            return False

        history.append(node_pos)
        best_exit = None
        for option_pos in self.node_neighbors(node_pos):
            if not valid_option(option_pos):
                continue

            exit = self.furthest_exterior_node_from(option_pos, history.copy())

            if exit is None:
                continue

            if best_exit is None or best_exit[1] < exit[1]:
                best_exit = exit
            elif best_exit[1] == exit[1]:
                best_exit = self.rng.choice((best_exit, exit))

        if best_exit is None and is_exterior(node_pos):
            best_exit = (node_pos, len(history))

        return best_exit

    def carve_exit(self):
        history = []
        exit_pos, path_len = self.furthest_exterior_node_from(START, history)
        
        for axis in range(0, 3):
            if axis != 2 and exit_pos[axis] == 0:
                wall = self.wall_for_position(axis, exit_pos)
                wall.state = False
            elif exit_pos[axis] == GRID_SIZE[axis] - 1:
                wall_pos = list(exit_pos)
                wall_pos[axis] += 1
                wall = self.wall_for_position(axis, wall_pos)
                wall.state = False

        print(f"EXIT={exit_pos}")
        print(f"Solution Len: {path_len}")
        

    def generate(self):
        self.place_exterior()
        self.carve_entrance()
        nodes = self.process_order()
        for node_pos in nodes:
            if not self.node_for_position(node_pos).visited:
                self.carve_from_node(node_pos)

        self.carve_exit()

    def export_walls(self):
        export_data = []

        def export_wall(axis, position, wall: MazeWall):
            if not wall.state:
                return

            position = grid_to_position(position)
            position[axis] -= UNIT_SIZE / 2

            scale = [UNIT_SIZE for _ in range(0, 3)]
            scale[axis] = WALL_WIDTH

            export_data.append(
                {
                    "position": position,
                    "scale": scale,
                    "texture": "Mine",
                }
            )

        self.walls_iter(export_wall)

        count = len(export_data)
        print(f"Wall Count: {count}")

        if count > OBJECT_LIMIT:
            raise Exception("Too many objects")

        return {
            "blocks": export_data,
            "editObjs": {
                "1769482": {
                    "position": grid_to_position(START)
                }
            }
        }


print(f"GRID_SIZE={GRID_SIZE}")
# print(f"MAZE_ORIGIN={MAZE_ORIGIN}")
print(f"START={START}")

maze = Maze(12345)
maze.generate()
json_data = maze.export_walls()
with open('maze.json', 'w') as file:
    file.write(json.dumps(json_data, indent=4))
