CREATURE_INDEX = {
    "Hero":{
        "Drops":{}
    },
    "Dummy":{
        "exp": 0,
        "max_hp": 99999999,
        "power": 0,
        "resilience": 0,
        "agility": 0,
        "damage": "1d4",
        "damage_type": "Smash",
        "accuracy": 100,
        "resistances":{
            "Slash": 0
        },
        "actions":[
            {
                "action":"nothing",
                "message": "The {NAME} just stands there waiting to suffer.\n",
                "chance":10
            }
        ]
    },
    "Clown":{
        "exp": 50,
        "max_hp": 20,
        "power": 3,
        "resilience": 3,
        "agility": 3,
        "damage": "1d4",
        "damage_type": "Smash",
        "accuracy": 100,
        "resistances":{
            "Slash": 0
        },
        "actions":[
            {
                "action":"attack",
                "chance":10
            },
            {
                "action":"nothing",
                "message": "{NAME} is just clowning around.\n",
                "chance":10
            }
        ],
        "levels":{
            2: "Double Attack",
        }
    },
    "Rat":{
        "exp": 10,
        "max_hp": 5,
        "power": 1,
        "resilience": 1,
        "agility": 1,
        "damage": "1d2",
        "damage_type": "Stab",
        "accuracy": 85,
        "resistances":{},
        "actions":[
            {
                "action":"attack",
                "chance":10
            },
        ]
    },
    "Hat Rat":{
        "exp": 10,
        "max_hp": 5,
        "power": 1,
        "resilience": 1,
        "agility": 1,
        "damage": "1d2",
        "damage_type": "Stab",
        "accuracy": 85,
        "resistances":{},
        "actions":[
            {
                "action":"attack",
                "chance":10
            },
        ],
        "equipment":[
            None,
            None,
            "Rat Hat",
            None,
            None,
            None,
            None,
        ],
        "levels":{
            1: "Spark",
        }
    },
    "Pigeon":{
        "exp": 10,
        "max_hp": 8,
        "power": 1,
        "resilience": 1,
        "agility": 10,
        "damage": "1d2",
        "damage_type": "Slash",
        "accuracy": 85,
        "resistances":{},
        "actions":[
            {
                "action":"attack",
                "chance":10
            },
        ],
        "drops":{
            "feather": 100
        },
        "levels":{
            1:"Gust"
        }
    },
    "Pixie":{
    "exp": 10,
    "max_hp": 8,
    "power": 1,
    "resilience": 1,
    "agility": 10,
    "damage": "1d2",
    "damage_type": "Magic",
    "accuracy": 85,
    "resistances":{},
    "actions":[
        {
            "action":"attack",
            "chance":10
        },
    ],
    "levels":{
        1: "Basic Divine Magic",
        10: "Basic Vampiric Magic",
    }
},
    "Gnome":{
        "exp": 10,
        "max_hp": 8,
        "power": 4,
        "resilience": 1,
        "agility": 10,
        "damage": "1d2",
        "damage_type": "Magic",
        "accuracy": 85,
        "resistances":{},
        "actions":[
            {
                "action":"attack",
                "chance":10
            },
        ],
        "levels":{
            3:"Double Attack"
        }
    }
}
