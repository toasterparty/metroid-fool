from random import Random

START_ID = 10_000_306
SEED = 6
FIGHT_LAYER = 4

rng = Random(SEED)
next_id = START_ID

def id():
    global next_id
    id = next_id
    next_id += 1
    return id

def randrange(min_val, max_val):
    return min_val + rng.random()*(max_val-min_val)

regular_pirate_counter = 1639788
shadow_pirate_counter = 1640036

regular_pirates = [1638404, 1638405, 1638406, 1638413, 1638414, 1638416, 1638868, 1639436]
shadow_pirates = [1638833, 1638834, 1638835, 1638994, 1638995, 1639011]
elite_pirate = 1639358
turret = 0x001901B9
metroids = [0x00190598, 0x00190599]

enemies = []
enemies.extend(regular_pirates)
enemies.extend(shadow_pirates)
enemies.append(elite_pirate)
enemies.append(turret)
enemies.extend(metroids)

# Need 18
crates = [
    (0x00190423, [-18.2847, -771.9351, 70.8779]),
    (0x00190426, [-21.2326, -771.2648, 70.8779]),
    (0x0019021E, [-13.729,  -823.2877, 94.9719]),
    (0x0019041A, [-11.9508, -816.5155, 90.8369]),
    (0x00190126, [-51.1069, -798.6355, 70.8664]),
    (0x0019018F, [-35.7989, -790.2687, 95.163]),
    (0x00190177, [-38.5436, -789.5445, 95.171]),
    (0x00190413, [-10.9677, -817.3539, 92.9916]),
    (0x00190206, [-15.6102, -821.2131, 90.8936]),
    (0x00190236, [-17.0209, -822.8183, 90.8995]),
    (0x0019042F, [-29.9078, -772.4063, 70.82]),
    (0x0019018F, [-35.7989, -790.2687, 95.163]),
]

tubes = [
    (0x0019014B, [-17.255, -785.4798, 74.5681]),
    (0x00190147, [-31.256, -785.5288, 74.5546]),
    (0x001901D0, [-19.2854, -811.8151, 74.5192]),
    (0x0019014F, [-27.6554, -811.8229, 74.5815]),
    (0x0019026D, [-31.2452, -785.5236, 98.9981]),
    (0x00190153, [-17.2561, -785.4908, 98.9321]),
]

remaining_hiding_spots = []
remaining_hiding_spots.extend(crates)
remaining_hiding_spots.extend(tubes)

assert len(remaining_hiding_spots) >= len(enemies)

timer_id = id()
alert_timer_id = id()
counter_id = id()
special_function_id = 10000304
hudmemo_id = 10000305

remove_connections = [
    {
        "senderId": 1639019, # trapped metroid actor
        "state": "INACTIVE",
        "targetId": 0x00190598,
        "message": "ACTIVATE",
    },
    {
        "senderId": 0x0019026D, # Platform Glass Tube
        "state": "DEAD",
        "targetId": 0x00190598,
        "message": "ACTIVATE",
    },
    {
        "senderId": 0x001901CC, # trapped metroid actor
        "state": "INACTIVE",
        "targetId": 0x00190599,
        "message": "ACTIVATE",
    },
    {
        "senderId": 0x001901D0, # Platform Glass Tube
        "state": "DEAD",
        "targetId": 0x00190599,
        "message": "ACTIVATE",
    }
]

delete_ids = [
    # trapped metroid actors
    1639019, 0x001901CC,
    # pirate activate trigger
    0x00190014,
    # scan thingy
    0x00190335, 0x001903B8, 0x0019033D, 0x001903D7,
    # Fight Music
    0x0019066B, 0x0019056B, 0x00190662, 0x0019051B,
    # Don't kill enemies when crates boom
    0x0019041D,
]

timers = [
    {
        "id": timer_id,
        "layer": FIGHT_LAYER,
        "time": 0.02,
        "startImmediately": True,
    },
    {
        "id": alert_timer_id,
        "layer": FIGHT_LAYER,
        "time": 0.1
    },
]

counters = [
    {
        "id": counter_id,
        "layer": FIGHT_LAYER,
        "maxValue": len(enemies),
    }
]

edit_objs = {
    # Barrier
    "1639218": {
        "layer": FIGHT_LAYER,
        "position": [-41.931, -783.3328, 94.201],
        "rotation": [0, 0, 0]
    }
}

connections = [
    {
        "senderId": counter_id,
        "state": "MAX_REACHED",
        "targetId": 1639218, # barrier
        "message": "DEACTIVATE",
    },
    {
        "senderId": counter_id,
        "state": "MAX_REACHED",
        "targetId": 10000302, # barrier trigger
        "message": "DEACTIVATE",
    },
    {
        "senderId": counter_id,
        "state": "MAX_REACHED",
        "targetId": special_function_id,
        "message": "DECREMENT",
    },
    {
        "senderId": counter_id,
        "state": "MAX_REACHED",
        "targetId": hudmemo_id,
        "message": "SET_TO_ZERO",
    },
]

for enemy_id in enemies:
    is_pirate = enemy_id in shadow_pirates or enemy_id in regular_pirates or enemy_id == elite_pirate

    if is_pirate:
        death_state = "DEATH_RATTLE"
    else:
        death_state = "DEAD"

    hiding_spot_idx = rng.randrange(0, len(remaining_hiding_spots))
    hiding_spot = remaining_hiding_spots.pop(hiding_spot_idx)

    hiding_spot_id, hiding_spot_pos = hiding_spot

    if is_pirate and hiding_spot in tubes:
        hiding_spot_pos[2] -= 2.2

    if enemy_id == turret:
        hiding_spot_pos[2] += 1.5
    if enemy_id in metroids:
        hiding_spot_pos[2] += 0.8
    elif hiding_spot in tubes:
        hiding_spot_pos[0] += randrange(-3, 3)
        hiding_spot_pos[1] += randrange(-3, 3)

    scale = randrange(0.5, 2)
    scale = [scale, scale, scale]

    def put_enemy(enemy_id):
        connections.extend(
            [
                # Start inactive
                {
                    "senderId": timer_id,
                    "state": "ZERO",
                    "targetId": enemy_id,
                    "message": "DEACTIVATE",
                },
                # Contribute to the counter
                {
                    "senderId": enemy_id,
                    "state": death_state,
                    "targetId": counter_id,
                    "message": "INCREMENT",
                },
                # Reveal Enemy
                {
                    "senderId": hiding_spot_id,
                    "state": "INACTIVE",
                    "targetId": enemy_id,
                    "message": "ACTIVATE",
                },
                {
                    "senderId": hiding_spot_id,
                    "state": "INACTIVE",
                    "targetId": alert_timer_id,
                    "message": "RESET_AND_START",
                },
                {
                    "senderId": alert_timer_id,
                    "state": "ZERO",
                    "targetId": enemy_id,
                    "message": "ALERT",
                }
            ]
        )

        # move enemy
        edit_objs[enemy_id] = {
            "layer": FIGHT_LAYER,
            "position": hiding_spot_pos,
            "speed": randrange(0.8, 2.5),
            "scale": scale,
        }

        edit_objs[hiding_spot_id] = {
            "vulnerability": "Blue"
        }

    if enemy_id == turret:
        put_enemy(0x001901B7) # turret base

    put_enemy(enemy_id)

data = {
    "timers": timers,
    "counters": counters,
    "editObjs": edit_objs,
    "removeConnections": remove_connections,
    "addConnections": connections,
    "deleteIds": delete_ids,
}

import json

with open('hydra.json', 'w') as file:
    file.write(json.dumps(data, indent=4))
