import json

layer = 11
next_id = 10001210

# x=-369.5902 +/- 5
region_scan_pos = [-364.5902, 366.032, -18.6673]
region_scan_rot = 115
room_scan_pos = [-374.5902, 366.032, -18.6673]
room_scan_rot = 65

pickup_pos = [-369.6044, 380.5261, -24.3]

def id():
    global next_id
    id = next_id
    next_id += 1
    return id

spawn_point_id = id()
tutorial_scan_id = id()
tutorial_lock_block1 = id()
tutorial_lock_block2 = id()

data = {
    "pickups": [
        {
            "type": "Nothing"
        }
    ],
    "doors": {
        "2": {
            "shieldType": "Blue",
            "blastShieldType": "None"
        },
        "3": {
            "shieldType": "Blue",
            "blastShieldType": "None"
        },
        "4": {
            "shieldType": "Blue",
            "blastShieldType": "None"
        }
    },
    "relays": [],
    "specialFunctions": [],
    "extraScans": [
        {
            "position": [-322.4694, 327.2704, -33.3408],
            "text": "What a lovely lil' plant. Maybe I'll take a trimming back with me when I'm done here."
        }
    ],
    "spawnPoints": [
        {
            "id": spawn_point_id,
            "layer": layer,
            "active": False,
            "position": [-369.6044, 380.5261, -24.3],
            "morphed": True,
        }
    ],
    "triggers": [
        {
            "id": 11000000,
            "position": [-399.861, 393.6213, -17.2384],
            "scale": [13, 10, 5],
            "deactivateOnEnter": True,
            "layer": 3
        },
        {
            "position": [-369.128387, 404.473297, -8.2],
            "scale": [13.5, 13.0, 8.5],
            "force": [
                0,
                -400.0,
                150.0
            ],
            "flags": 8193,
            "layer": 3
        },
        {
            "id": 11000005,
            "position": [-336.9284, 404.1733, -12.6547],
            "scale": [18, 9, 9],
            "deactivateOnEnter": True,
            "layer": 3
        },
        {
            "id": 11000010, # water trigger
            "position": [-334.8394, 309.9352, -8.6111],
            "scale": [6.1, 13.2, 50]
        }
    ],
    "timers": [
        {
            "id": 11000001,
            "time": 0.02,
            "layer": 3
        },
        {
            "id": 11000011,
            "time": 0.02,
            "startImmediately": True
        }
    ],
    "liquids": [
        {
            "id": 11000009,
            "type": "Water",
            "position": [-334.8394, 309.9352, -8.6111],
            "scale": [6.1, 13.2, 50]
        }
    ],
    "blocks": [
        # temple blocker
        {
            "layer": 3,
            "position": [-384.2, 303.02, -14.0],
            "scale": [6, 1, 6],
        },
        # ship blockers
        {
            "id": tutorial_lock_block1,
            "layer": layer,
            "position": [-407.5, 367.02, -21.3],
            "scale": [1, 6, 6],
        },
        {
            "id": tutorial_lock_block2,
            "layer": layer,
            "position": [-295.5, 396.42, -38.4],
            "scale": [1, 6, 6],
        },
    ],
    "editObjs": {
        "268": { # camera7
            "position": [-339.4529, 327.2898, -29.3721]
        },
        "273": { # camera7's target
            "position": [-343.1256, 319.2706, -34.2105]
        },
        "272": { # camera7's target
            "position": [-341.5256, 313.5706, -34.9105]
        },
        "271": { # camera7's path waypoint
            "position": [-339.4529, 327.2898, -29.3721]
        },
        "293": { # camera10's target
            "position": [-321.190186, 319.832001, -34.167301]
        },
        "294": { # camera10's target
            "position": [-321.190186, 319.832001, -34.167301]
        },
        "292": { # camera10's start position
            "position": [-331.0564, 319.9657, -30.7432]
        },
        "291": { # camera10's end position
            "position": [-325.7564, 328.4657, -33.7432]
        },
        "300": { # target
            "position": [-322.3564, 327.1657, -33.4432]
        },
        "301": { # target
            "position": [-322.3564, 327.1657, -33.4432]
        },
        "305": { # target
            "position": [-322.3564, 327.1657, -33.4432]
        },
        "303": { # target
            "position": [-322.3564, 327.1657, -33.4432]
        },
        "298": { # path
            "position": [-324.0, 349.0, -28.0]
        },
        "307": { # path
            "position": [-324.0, 341.4461, -29.9394]
        },
        "299": { # path
            "position": [-324.0, 333.8922, -31.8788]
        },
        "306": { # path
            "position": [-324.0, 333.8922, -32.8788]
        },
        # circle pan
        "318": { # target
            "position": [-342.6856, 311.9993, -36.5549]
        },
        "338": { # target
            "position": [-343.3856, 320.5993, -34.1549]
        },
        "314": { # camera path waypoint
            "position": [-349.4856, 312.49980000000005, -32.4533]
        },
        "315": { # camera path waypoint
            "position": [-346.1295, 310.5461, -32.5481]
        },
        "316": { # camera path waypoint
            "position": [-342.3867, 310.4837, -32.6237]
        },
        "317": { # camera path waypoint
            "position": [-340.1703, 314.3514, -32.5571]
        },
        "319": { # camera path waypoint
            "position": [-341.4507, 319.9044, -32.074]
        },
        "322": { # camera path waypoint
            "position": [-347.2093, 319.98479999999995, -30.722900000000003]
        },
        "424": { # SJF scan
            "position": [-390.9964, 307.4193, -5.3191]
        },
        "425": { # blue patch scan
            "position": [-377.8229, 348.7109, -13.5328],
            "layer": 3
        },
        "467": { # save station trigger
            "scale": [5.0, 5.0, 5.0],
            "layer": 4
        },
        "321": { # ship
            "layer": 4
        },
        "463": { # save station beam
            "layer": 4
        },
        "498": { # back from load trigger
            "layer": 4
        },
        "579": { # trigger push up
            "layer": 4
        },
        "464": { # save station energy
            "layer": 4
        },
        "484": { # save station base lights
            "layer": 4
        },
        "489": { # savestation hum
            "layer": 4
        },
        "91": { # ship sound
            "layer": 4
        },
        "573": { # ship sound
            "layer": 4
        },
        "466": { # map station sound
            "layer": 4
        },
        "88": { # ambience left
            "layer": 4
        },
        "557": { # audio fade out
            "layer": 4
        }
    },
    "addConnections": [
        {
            "senderId": 0x00000212, # Timer Save Out of Ship Delay
            "state": "ZERO",
            "targetId": spawn_point_id,
            "message": "SET_TO_ZERO"
        },
        {
            "senderId": 0x00000206, # Relay-cinema-not saving
            "state": "ZERO",
            "targetId": spawn_point_id,
            "message": "SET_TO_ZERO"
        },
        {
            "senderId": 11000010, # water trigger
            "state": "ENTERED",
            "targetId": 11000009, # water
            "message": "ACTIVATE"
        },
        {
            "senderId": 11000010, # water trigger
            "state": "EXITED",
            "targetId": 11000009, # water
            "message": "DEACTIVATE"
        },
        {
            "senderId": 11000011, # auto-start timer
            "state": "ZERO",
            "targetId": 11000009, # water
            "message": "DEACTIVATE"
        },
        {
            "senderId": 425,
            "state": "SCAN_DONE",
            "targetId": 468, # save station spawn point
            "message": "SET_TO_ZERO"
        },
        {
            "senderId": 425,
            "state": "SCAN_DONE",
            "targetId": 467, # save station trigger
            "message": "DEACTIVATE"
        },
        {
            "senderId": 425,
            "state": "SCAN_DONE",
            "targetId": 11000001, # custom timer
            "message": "RESET_AND_START"
        },
        {
            "senderId": 11000001, # custom timer
            "state": "ZERO",
            "targetId": 467,
            "message": "ACTIVATE"
        },
        {
            "senderId": 11000000, # trigger near SJF
            "state": "ENTERED",
            "targetId": 468, # save station spawn point
            "message": "SET_TO_ZERO"
        },
        {
            "senderId": 11000005, # trigger near alcove
            "state": "ENTERED",
            "targetId": 557, # StreamedAudio FadeIn/Out Long
            "message": "DECREMENT"
        }
    ],
    "deleteIds": [
        126, # pickup
        611  # cutscene skip
    ]
}

ROOM_IDS = [
    3689744570,
    925831207,
    3339035544,
    603152353,
    3001573804,
    835750603,
    1876146603,
    2965866933,
    1829788744,
    87039645,
    3156907596,
    717679670,
    2445362367,
    2109790043,
    1125708118,
    3004337398,
    2451570395,
    3223329329,
]

# (region, rooms)
#            ----> (room, room_id)
REGIONS = [
    (
        id(),
        'Tallon Overworld',
        [
            (id(), 'Tallon Overworld North (Tallon Canyon)'),
            (id(), 'Tallon Overworld West (Root Cave)'),
            (id(), 'Tallon Overworld East (Frigate Crash Site)'),
            (id(), 'Tallon Overworld South (Great Tree Hall, Upper)'),
            (id(), 'Tallon Overworld South (Great Tree Hall, Lower)'),
        ]
    ),
    (
        id(),
        'Chozo Ruins',
        [
            (id(), 'Chozo Ruins West (Main Plaza)'),
            (id(), 'Chozo Ruins North (Sun Tower)'),
            (id(), 'Chozo Ruins East (Reflecting Pool, Save Station)'),
            (id(), 'Chozo Ruins South (Reflecting Pool, Far End)'),
        ]
    ),
    (
        id(),
        'Magmoor Caverns',
        [
            (id(), 'Magmoor Caverns North (Lava Lake)'),
            (id(), 'Magmoor Caverns West (Monitor Station)'),
            (id(), 'Magmoor Caverns East (Twin Fires)'),
            (id(), 'Magmoor Caverns South (Magmoor Workstation, Save Station)'),
            (id(), 'Magmoor Caverns South (Magmoor Workstation, Debris)'),
        ]
    ),
    (
        id(),
        'Phendrana Drifts',
        [
            (id(), 'Phendrana Drifts North (Phendrana Shorelines)'),
            (id(), 'Phendrana Drifts South (Quarantine Cave)'),
        ]
    ),
    (
        id(),
        'Phazon Mines',
        [
            (id(), 'Phazon Mines East (Main Quarry)'),
            (id(), 'Phazon Mines West (Phazon Processing Center)'),
        ]
    ),
]

assert len(ROOM_IDS) == sum(len(ROOMS) for _, _, ROOMS in REGIONS)

data['layers'] = {
    # True for debug
    layer: False,
    12: False, # ridley dead
}

pickup_id = id()
data['pickups'].append(
    {
        'id': pickup_id,
        'position': [-392.5887, 395.6094, -14.59],
        'type': 'Nothing',
        'scanText': 'Warp to Escape Sequence',
        'respawn': True,
        'destination': 'Impact Crater:Metroid Prime Lair',
    }
)
data['editObjs'][pickup_id] = {
    "layer": 12
}

# Create helper relays
change_layers_relay_id = id()
clear_pickups_relay_id = id()
clear_region_scans_relay_id = id()
clear_room_scans_relay_id = id()
data['relays'].extend([
    {
        'id': change_layers_relay_id,
        'layer': layer,
    },
    {
        'id': clear_pickups_relay_id,
        # DEFAULT LAYER
    },
    {
        'id': clear_region_scans_relay_id,
        'layer': layer,
    },
    {
        'id': clear_room_scans_relay_id,
        'layer': layer,
    },
])

# Create auto-start timers
auto_start_timer_default = id()
auto_start_timer = id()
data['timers'].extend([
    {
        'id': auto_start_timer_default,
        # DEFAULT LAYER
        'time': 0.02,
        'startImmediately': True,
    },
    {
        'id': auto_start_timer,
        'layer': layer,
        'time': 0.04,
        'startImmediately': True,
    },
])

data['addConnections'].extend([
    # Clear everything when the room loads
    {
        'senderId': auto_start_timer_default,
        'state': 'ZERO',
        'targetId': clear_pickups_relay_id,
        'message': 'SET_TO_ZERO',
    },
    {
        'senderId': auto_start_timer_default,
        'state': 'ZERO',
        'targetId': clear_region_scans_relay_id,
        'message': 'SET_TO_ZERO',
    },
    {
        'senderId': auto_start_timer_default,
        'state': 'ZERO',
        'targetId': clear_room_scans_relay_id,
        'message': 'SET_TO_ZERO',
    },
    # Propogate layer changes when room loads
    {
        'senderId': auto_start_timer,
        'state': 'ZERO',
        'targetId': change_layers_relay_id,
        'message': 'SET_TO_ZERO',
    },
    # Disable cutscene skips for saving when room loads
    {
        'senderId': auto_start_timer,
        'state': 'ZERO',
        'targetId': 627,
        'message': 'DEACTIVATE',
    },
    {
        'senderId': auto_start_timer,
        'state': 'ZERO',
        'targetId': 4,
        'message': 'DEACTIVATE',
    },
])

# Add layer changers
for room_id in ROOM_IDS:
    layer_changer_id = id()
    data['specialFunctions'].append({
            'id': layer_changer_id,
            'type': 'ScriptLayerController',
            'layerChangeRoomId':  room_id,
            'layerChangeLayerId': layer,
        }
    )
    data['addConnections'].append({
            'senderId': change_layers_relay_id,
            'state': 'ZERO',
            'targetId': layer_changer_id,
            'message': 'INCREMENT',
        }
    )

# temp fix for v1.0.1
data['addConnections'].append({
        'senderId': auto_start_timer,
        'state': 'ZERO',
        'targetId': REGIONS[0][0],
        'message': 'ACTIVATE',
    }
)
data['addConnections'].append({
        'senderId': auto_start_timer,
        'state': 'ZERO',
        'targetId': tutorial_lock_block1,
        'message': 'DEACTIVATE',
    }
)
data['addConnections'].append({
        'senderId': auto_start_timer,
        'state': 'ZERO',
        'targetId': tutorial_lock_block2,
        'message': 'DEACTIVATE',
    }
)

# # Add tutorial scan
# data['extraScans'].append(
#     {
#         'id': tutorial_scan_id,
#         'layer': layer,
#         'position': [-369.6, 372.332, -24.4673],
#         'rotation': 270,
#         'isRed': True,
#         'combatVisible': True,
#         'text': "Whoever took your ship appears to have upgraded it and returned it. Use &push;&main-color=#43CD80;Scan Visor&pop; to toggle the above terminals to select your desired destination. Additionally, you can recall at each of these ingress points.",
#     }
# )

# # Activate the first region scan when the player reads the tutorial
# data['addConnections'].append({
#         'senderId': tutorial_scan_id,
#         'state': 'SCAN_DONE',
#         'targetId': REGIONS[0][0],
#         'message': 'ACTIVATE',
#     }
# )
# data['addConnections'].append({
#         'senderId': tutorial_scan_id,
#         'state': 'SCAN_DONE',
#         'targetId': tutorial_lock_block1,
#         'message': 'DEACTIVATE',
#     }
# )
# data['addConnections'].append({
#         'senderId': tutorial_scan_id,
#         'state': 'SCAN_DONE',
#         'targetId': tutorial_lock_block2,
#         'message': 'DEACTIVATE',
#     }
# )

# # ... or when they come back from warp/load
# data['addConnections'].append({
#         'senderId': 0x000001FD, # Relay-cinema loading
#         'state': 'ZERO',
#         'targetId': REGIONS[0][0],
#         'message': 'ACTIVATE',
#     }
# )
# data['addConnections'].append({
#         'senderId': 0x000001FD,
#         'state': 'ZERO',
#         'targetId': tutorial_lock_block1,
#         'message': 'DEACTIVATE',
#     }
# )
# data['addConnections'].append({
#         'senderId': 0x000001FD,
#         'state': 'ZERO',
#         'targetId': tutorial_lock_block2,
#         'message': 'DEACTIVATE',
#     }
# )

# Activate the spawn point once we've actually started picking out destinations
for _, _, ROOMS in REGIONS:
    data['addConnections'].append({
            'senderId': ROOMS[0][0],
            'state': 'SCAN_DONE',
            'targetId': spawn_point_id,
            'message': 'ACTIVATE',
        }
    )

first_region = True
first_room = True

for region_idx, region_data in enumerate(REGIONS):
    region_scan_id, region, ROOMS = region_data
    # Add Region Scan
    scan = {
        'id': region_scan_id,
        'layer': layer,
        'position': region_scan_pos,
        'rotation': region_scan_rot,
        'isRed': True,
        'text': region,
    }
    if first_region:
        scan['combatVisible'] = True
        first_region = False
    data['extraScans'].append(scan)
    data['addConnections'].append(
        {
            'senderId': clear_region_scans_relay_id,
            'state': 'ZERO',
            'targetId': region_scan_id,
            'message': 'DEACTIVATE',
        }
    )

    # When scanned, clear everything
    data['addConnections'].extend([
        {
            'senderId': region_scan_id,
            'state': 'SCAN_DONE',
            'targetId': clear_pickups_relay_id,
            'message': 'SET_TO_ZERO',
        },
        {
            'senderId': region_scan_id,
            'state': 'SCAN_DONE',
            'targetId': clear_region_scans_relay_id,
            'message': 'SET_TO_ZERO',
        },
        {
            'senderId': region_scan_id,
            'state': 'SCAN_DONE',
            'targetId': clear_room_scans_relay_id,
            'message': 'SET_TO_ZERO',
        },
    ])

    # When scanned, start a short timer to select the region
    timer_id = id()
    data['timers'].append(
        {
            'id': timer_id,
            'layer': layer,
            'time': 0.04
        }
    )
    data['addConnections'].append(
        {
            'senderId': region_scan_id,
            'state': 'SCAN_DONE',
            'targetId': timer_id,
            'message': 'RESET_AND_START',
        }
    )

    # When the timer elapses, activate the next region's scan
    next_region_idx = (region_idx + 1) % len(REGIONS)
    data['addConnections'].append(
        {
            'senderId': timer_id,
            'state': 'ZERO',
            'targetId': REGIONS[next_region_idx][0],
            'message': 'ACTIVATE',
        }
    )

    # When the timer elapses, activate the first room in this region's scan
    data['addConnections'].append(
        {
            'senderId': timer_id,
            'state': 'ZERO',
            'targetId': ROOMS[0][0],
            'message': 'ACTIVATE',
        }
    )

    for room_idx, (room_scan_id, room) in enumerate(ROOMS):
        # Add Room Scan
        scan = {
            'id': room_scan_id,
            'layer': layer,
            'position': room_scan_pos,
            'rotation': room_scan_rot,
            'isRed': True,
            'text': room.replace(' (', '\n('),
        }
        if first_room:
            scan['combatVisible'] = True
            first_room = False
        data['extraScans'].append(scan)
        data['addConnections'].append(
            {
                'senderId': clear_room_scans_relay_id,
                'state': 'ZERO',
                'targetId': room_scan_id,
                'message': 'DEACTIVATE',
            }
        )

        # Add warp pickup
        pickup_id = id()
        data['pickups'].append(
            {
                'id': pickup_id,
                # DEFAULT LAYER
                'position': pickup_pos,
                'type': 'Nothing',
                'respawn': True,
                'destination': room,
            }
        )
        data['addConnections'].append(
            {
                'senderId': clear_pickups_relay_id,
                'state': 'ZERO',
                'targetId': pickup_id,
                'message': 'DEACTIVATE',
            }
        )

        # Move warp pickup to upgraded ship layer
        data['editObjs'][pickup_id] = {
            'layer': layer,
        }

        # When scanned, clear everything but the region
        data['addConnections'].extend([
            {
                'senderId': room_scan_id,
                'state': 'SCAN_DONE',
                'targetId': clear_pickups_relay_id,
                'message': 'SET_TO_ZERO',
            },
            {
                'senderId': room_scan_id,
                'state': 'SCAN_DONE',
                'targetId': clear_room_scans_relay_id,
                'message': 'SET_TO_ZERO',
            },
        ])

        # When scanned, start a short timer to select the room
        timer_id = id()
        data['timers'].append(
            {
                'id': timer_id,
                'layer': layer,
                'time': 0.04
            }
        )
        data['addConnections'].append(
            {
                'senderId': room_scan_id,
                'state': 'SCAN_DONE',
                'targetId': timer_id,
                'message': 'RESET_AND_START',
            }
        )

        # When the timer elapses, activate the next room's scan
        next_room_idx = (room_idx + 1) % len(ROOMS)
        data['addConnections'].append(
            {
                'senderId': timer_id,
                'state': 'ZERO',
                'targetId': ROOMS[next_room_idx][0],
                'message': 'ACTIVATE',
            }
        )

        # When the timer elapses, activate the pickup
        data['addConnections'].append(
            {
                'senderId': timer_id,
                'state': 'ZERO',
                'targetId': pickup_id,
                'message': 'ACTIVATE',
            }
        )

        # When the timer elapses, deactivate the standard reposition
        data['addConnections'].append(
            {
                'senderId': timer_id,
                'state': 'ZERO',
                'targetId': 0x000001D4, # save spawn point
                'message': 'DEACTIVATE',
            }
        )

    first_region = False

with open('landing_site.json', 'w') as file:
    file.write(json.dumps(data, indent=4))
