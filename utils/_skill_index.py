SKILL_INDEX={
    # MARTIAL
    "P-Stance":{
        "tags":["self_flag","battle","map"],
        "name": "Power Stance",
        "description":"adopt a power boosting stance.",
        "self_flag":{
            "remove":["Power Stance","Defence Stance","Agile Stance","Balanced Stance"],
            "add":{"Power Stance":"Martial"}
        },
        "cooldown": 0
    },
    "D-Stance":{
        "tags":["self_flag","battle","map"],
        "name": "Defence Stance",
        "description":"adopt a resiliance boosting stance.",
        "self_flag":{
            "remove":["Power Stance","Defence Stance","Agile Stance","Balanced Stance"],
            "add":{"Defence Stance":"Martial"}
        },
        "cooldown": 0
    },
    "A-Stance":{
        "tags":["self_flag","battle","map"],
        "name": "Agile Stance",
        "description":"adopt an agility boosting stance.",
        "self_flag":{
            "remove":["Power Stance","Defence Stance","Agile Stance","Balanced Stance"],
            "add":{"Agile Stance":"Martial"}
        },
        "cooldown": 0
    },
    "B-Stance":{
        "tags":["self_flag","battle","map"],
        "name": "Balanced Stance",
        "description":"adopt a stance boosting all stats.",
        "self_flag":{
            "remove":["Power Stance","Defence Stance","Agile Stance","Balanced Stance"],
            "add":{"Balanced Stance":"Martial"}
        },
        "cooldown": 0
    },
    "Lunge":{
        "tags":["battle","temp_buff","attack"],
        "name": "Lunge",
        "description":"Perform a reckless attack that leaves you vulnerable.",
        "temp_buff":{
            "stats":{
                "power":"*2",
                "resilience":"/2"
            },
            "then":{
                "attack":{}
            }
        },
        "cooldown":0
    },
    "Thrust":{
        "tags":["battle","temp_buff","attack"],
        "name": "Thrust",
        "description":"Perform a weaker but precise attack.",
        "temp_buff":{
            "stats":{
                "agility":"*2",
                "power":"/2"
            },
            "then":{
                "attack":{}
            }
        },
        "cooldown":0
    },
    "Defend":{
        "tags":["battle","temp_buff"],
        "name": "Defend",
        "description":"Prepare for an incoming attack.",
        "temp_buff":{
            "stats":{
                "resilience":"*2",
                "agility":"/2"
            }
        },
        "cooldown":0
    },
    "Execute":{
        "tags":["battle","temp_buff","attack"],
        "name": "Execution Technique",
        "description":"Perform a single powerful precise attack.",
        "temp_buff":{
            "stats":{
                "agility":"*2",
                "power":"*3"
            },
            "then":{
                "attack":{"count":1}
            }
        },
        "cooldown":2
    },
    "Exploit":{
        "tags":["battle","attack"],
        "name": "Execution Technique",
        "description":"Perform a single powerful precise attack.",
        "attack":{
            "count": 1,
            "accuracy": 100000
        },
        "cooldown":2
    },
    "Fortress":{
        "tags":["battle","temp_buff"],
        "name": "Fortress Technique",
        "description":"Perform a single powerful precise attack.",
        "temp_buff":{
            "stats":{
                "agility":"*2",
                "power":"*3"
            },
            "then":{
                "attack":{"count":1}
            }
        },
        "cooldown":2
    },
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
    },

    # Un-sorted
    "Glint":{},
    "S-Pixie":{},
    "S-Gnome":{},
    "Drain":{},
    "EnPower":{},
    "M-EnPower":{},
    "Bolster":{},
    "M-Bolster":{},
    "Quicken":{},
    "M-Quicken":{},
    "M-Heal":{},
    "Flash":{},
    "Feed":{},
    "S-Power":{},
    "S-Virtue":{},
    "Multi-S":{},
    "Resist":{},
    "Critster":{},
    "Deify":{},
    "Restore":{},
    "Dawn":{},
    "S-Guardian":{},
    "S-Zealot":{},
    "S-Archon":{},



}
