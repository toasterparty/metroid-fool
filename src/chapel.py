from random import Random

# Configuration
SEED=4
CENTER=(-370.1, -172.0, 42.1)
SCALE=(40, 50, 13)
START_ID=9_800_000
SHEEGOTHS=[917562, 917568, 917553, 917544, 917520] # last one is momma

MIN_SPEED=1
MAX_SPEED=8
MAX_OFFSET=6
NUM_WAYPOINTS=50

# End Configuration

next_id: int = START_ID
rng = Random(SEED)
min_pos = [
    CENTER[0] - (SCALE[0]/2),
    CENTER[1] - (SCALE[1]/2),
    CENTER[2] - (SCALE[2]/2),
]
max_pos = [
    CENTER[0] + (SCALE[0]/2),
    CENTER[1] + (SCALE[1]/2),
    CENTER[2] + (SCALE[2]/2),
]

def id():
    global next_id
    id = next_id
    next_id += 1
    return id

def randrange(min_val, max_val):
    return min_val + rng.random()*(max_val-min_val)

timer_id = id()

data = {}

data["timers"] = []
data["waypoints"] = []
data["platforms"] = []
data["actorRotates"] = []
data["editObjs"] = {}
data["addConnections"] = []

for _ in range(0, NUM_WAYPOINTS):
    data["waypoints"].append(
        {
            "id": id(),
            "position": [
                randrange(min_pos[axis], max_pos[axis]) for axis in range(0, 3)
            ],
            "speed": randrange(MIN_SPEED, MAX_SPEED),
        }
    )

for i, waypoint in enumerate(data["waypoints"]):
    if i == len(data["waypoints"]) - 1:
        next_waypoint = data["waypoints"][0]
    else:
        next_waypoint = data["waypoints"][i+1]

    data["addConnections"].append(
        {
            "senderId": waypoint["id"],
            "state": "ARRIVED",
            "targetId": next_waypoint["id"],
            "message": "NEXT",
        }
    )

for sheegoth_id in SHEEGOTHS:
    platform_id = id()
    actor_rotate_id = id()

    starting_waypoint = rng.choice(data["waypoints"])
    starting_waypoint_id = starting_waypoint["id"]
    starting_position = starting_waypoint["position"]
    sheegoth_position = [
        starting_position[axis] + randrange(0 - MAX_OFFSET, MAX_OFFSET) for axis in range(0, 3)
    ]

    data["editObjs"][sheegoth_id] = {
        "position": sheegoth_position,
        "speed": 2,
        "vulnerability": "Blue",
    }

    data["platforms"].append(
        {
            "id": platform_id,
            "position": starting_position,
            "type": "Empty",
        }
    )

    data["editObjs"][platform_id] = {
        "speed": 1,
    }

    data["actorRotates"].append(
        {
            "id": actor_rotate_id,
            "rotation": [
                randrange(0, 360) for _ in range(0, 3)
            ],
            "timeScale": randrange(0.1, 5),
            "updateActive": True,
            "updateOnCreation": False,
            "updateActors": True,
        }
    )

    data["addConnections"].extend(
        [
            {
                "senderId": timer_id,
                "state": "ZERO",
                "targetId": platform_id,
                "message": "STOP",
            },
            {
                "senderId": sheegoth_id,
                "state": "ACTIVE",
                "targetId": platform_id,
                "message": "START",
            },
            {
                "senderId": sheegoth_id,
                "state": "ACTIVE",
                "targetId": actor_rotate_id,
                "message": "ACTION",
            },
            {
                "senderId": platform_id,
                "state": "ACTIVE",
                "targetId": starting_waypoint_id,
                "message": "FOLLOW",
            },
            {
                "senderId": platform_id,
                "state": "PLAY",
                "targetId": sheegoth_id,
                "message": "ACTIVATE",
            },
            {
                "senderId": actor_rotate_id,
                "state": "PLAY",
                "targetId": platform_id,
                "message": "PLAY",
            },
        ]
    )

for relay_id in [917656, 917659]:
    data["addConnections"].append(
        {
            "senderId": 917636, # Wave beam platform lowest waypoint
            "state": "ARRIVED",
            "targetId": relay_id,
            "message": "SET_TO_ZERO",
        }
    )

data["timers"] = [
    {
        "id": 917591,
        "time": 15
    },
    {
        "id": timer_id,
        "time": 0.02,
        "startImmediately": True,
    }
]

data["addConnections"].append(
    {
        "senderId": 917636, # Wave beam platform lowest waypoint
        "state": "ARRIVED",
        "targetId": 917591,
        "message": "RESET_AND_START",
    }
)

data["addConnections"].append(
    {
        "senderId": 10000660, # player in area
        "state": "ENTERED",
        "targetId": 917665, # lock door relay
        "message": "SET_TO_ZERO",
    }
)

import json
with open('chapel.json', 'w') as file:
    file.write(json.dumps(data, indent=4))
