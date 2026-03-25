SKILL_INDEX={
    # Attacks
    "I-strike":{
        "tags":["battle","attack"],
        "name": "Ice Strike",
        "description":"Perform a weapon attack that deals Ice damage.",
        "attack":{
            "damage_type":"Ice"
        },
        "cooldown":2
    },
    "F-strike":{
        "tags":["battle","attack"],
        "name": "Fire Strike",
        "description":"Perform a weapon attack that deals Fire damage.",
        "attack":{
            "damage_type":"Fire"
        },
        "cooldown":2
    },
    "L-strike":{
        "tags":["battle","attack"],
        "name": "Lightning Strike",
        "description":"Perform a weapon attack that deals Lightning damage.",
        "attack":{
            "damage_type":"Lightning"
        },
        "cooldown":2
    },
    # Spells
    "Bolt":{
        "tags":["battle","attack"],
        "name": "Bolt",
        "description":"launch a single bolt of lightning towards an enemy.",
        "attack":{
            "damage": "2d4",
            "damage_type": "Lightning",
            "accuracy": 150
        },
        "cooldown": 3
    },
    # Heals
    "Heal":{
        "tags":["map", "battle", "restorative"],
        "name": "Heal",
        "description":"Restore the body and mind of an ally.",
        "restorative":"3d4",
        "uses": 3
    },
    # Summons
    "S-Frog":{
        "tags":["map","battle","summon"],
        "name": "Summon Frog",
        "description":"Summon a poisonous frog to help you combat",
        "summon": "Frog",
        "uses": 3
    }
}
