START_ID = 10000335
next_id = START_ID

def id():
    global next_id
    id = next_id
    next_id += 1
    return id

rooms = [
    # (room_id, dec_layers)
    (1690530837, [1]), # Specimen Storage
    (351383175 , [2, 3, 4, 5, 6, 10]), # Research Entrance
    (3056950407, [1, 10]), # Hydra Lab Entryway
    (245580074 , [1, 2, 4, 10]), # Research Lab Hydra
    (2102741926, [1, 2, 10]), # Observatory Access
    (2120180247, [1, 2, 10]), # Observatory
    (1717448744, [1, 2, 10]), # West Tower Entrance
    (2124934084, [1, 10]), # West Tower
    (3858019950, [1, 2, 4, 10]), # Control Tower
    (216672071 , [10]), # East Tower
    (137821706 , [1, 10]), # Aether Lab Entryway
    (893946318 , [1, 2, 4, 5, 10]), # Research Lab Aether
    (3422621718, [1, 2, 10]), # Research Core Access
    (2007836944, [1, 2, 10]), # Research Core
]

relay_id = id()
trigger_id = 10000331
door_block_id = 10000332
timer_id = 10000333
hudmemo_id = id()

connections = []
special_functions = []
relays = [
    {
        "id": relay_id,
    }
]
hudmemos = [
    {
        "id": hudmemo_id,
        "text": "&just=center;Hooray you fixed it",
        "messageTime": 9
    }
]

connections.append(
    {
        "senderId": 0x0028040A,
        "state": "INACTIVE",
        "targetId": relay_id,
        "message": "SET_TO_ZERO",
    }
)

connections.append(
    {
        "senderId": relay_id,
        "state": "ZERO",
        "targetId": hudmemo_id,
        "message": "SET_TO_ZERO",
    }
)

machine = [
    0x0028028C, 0x0028028D, 0x0028028F
]

remove_connections = [
    {
        "senderId": 0x002803FD,
        "state": "ZERO",
        "targetId": machine[0],
        "message": "DECREMENT",
    },
    {
        "senderId": 0x002803FC,
        "state": "ZERO",
        "targetId": machine[0],
        "message": "DECREMENT",
    },
    {
        "senderId": 0x002803FE,
        "state": "ZERO",
        "targetId": machine[1],
        "message": "DECREMENT",
    },
    {
        "senderId": 0x002803FC,
        "state": "ZERO",
        "targetId": machine[2],
        "message": "DECREMENT",
    },
]

for connection in remove_connections:
    connection = connection.copy()
    connection["message"] = "INCREMENT"

    connections.append(connection)

active_false_ids = [
    2621724, # pickup
]

active_false_ids.extend(machine)

# deactivate on room load
for _id in active_false_ids:
    connections.append(
        {
            "senderId": timer_id,
            "state": "ZERO",
            "targetId": _id,
            "message": "DEACTIVATE",
        }
    )

disable_ids = [
    trigger_id,
    door_block_id,
]

for _id in disable_ids:
    connections.append(
        {
            "senderId": relay_id,
            "state": "ZERO",
            "targetId": _id,
            "message": "DEACTIVATE",
        }
    )
   
connections.append(
    {
        "senderId": relay_id,
        "state": "ZERO",
        "targetId": 10000334, # worldlightfader
        "message": "ACTION",
    }
)

for room_id, layers, in rooms:
    for layer in layers:
        layer_change_id = id()

        special_functions.append(
            {
                "id": layer_change_id,
                "type": "ScriptLayerController",
                "layerChangeRoomId": room_id,
                "layerChangeLayerId": layer,
            }
        )

        connections.append(
            {
                "senderId": relay_id,
                "state": "ZERO",
                "targetId": layer_change_id,
                "message": "DECREMENT",
            }
        )

data = {
    "relays": relays,
    "specialFunctions": special_functions,
    "hudmemos": hudmemos,
    "addConnections": connections,
    "removeConnections": remove_connections,
}

import json

with open('labs.json', 'w') as file:
    file.write(json.dumps(data, indent=4))
