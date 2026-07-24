import math

_DYNAMIC_DAMAGE_TABLE={
    "Fire":{
        "weak": lambda lv: f"{math.ceil(lv/10)}d3+{math.ceil(lv/4)}",
        "normal": lambda lv: f"{math.ceil(lv/4)}d3+{math.ceil(lv/3)}",
        "powerful": lambda lv: f"{math.ceil(lv/3)}d3+{math.ceil(lv/2)}",
    },
    "Cold":{
        "weak": lambda lv: f"{math.ceil(lv/5)}d2",
        "normal": lambda lv: f"{math.ceil(lv/3)}d2",
        "powerful": lambda lv: f"{lv}d2"
    },
    "Earth":{
        "weak": lambda lv: f"{math.ceil(lv/2)}",
        "normal": lambda lv: f"{lv}",
        "powerful": lambda lv: f"{math.ceil(lv*2.5)}"
    },
    "Wind":{
        "weak": lambda lv: f"1d{lv}",
        "normal": lambda lv: f"1d({lv}*3)",
        "powerful": lambda lv: f"1d({lv}*5)",
    },
    "Divine":{
        "weak": lambda lv: f"{math.ceil(lv/2)}d2",
        "normal": lambda lv: f"{math.ceil(lv/3)}d4",
        "powerful": lambda lv: f"{lv}d4",
    }
}


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
        "tags":["battle","temp_buff","attack","weapon"],
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
        "tags":["battle","temp_buff","attack","weapon"],
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
        "tags":["battle","temp_buff","attack","weapon"],
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
        "tags":["battle","attack","weapon"],
        "name": "Execution Technique",
        "description":"Perform a single powerful precise attack.",
        "attack":{
            "count": 1,
            "accuracy": 100000
        },
        "cooldown":2
    },
    "Fortress":{
        "tags":["battle","self_flag"],
        "name": "Fortress Technique",
        "description":"Perform a single powerful precise attack.",
        "self_flag":{
            "add":{"Fortress": 1}
        },
        "cooldown":2
    },
    # ELEMENTAL
    "Chill":{
        "tags":["battle","attack","spell"],
        "name": "Chill",
        "description":"Drop the temperature of a creature severely.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Cold"]["normal"],
            "damage_type": "Cold",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Spark":{
        "tags":["battle","attack","spell"],
        "name": "Spark",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Fire"]["normal"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 2
    },
    "Shunt":{
        "tags":["battle","attack","spell","light"],
        "name": "Shunt",
        "description":"Blast a creature with a heavy wind.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Wind"]["normal"],
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Toss rock":{
        "tags":["battle","attack","spell"],
        "name": "Toss rock",
        "description":"Throw a god damn rock at them.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Earth"]["normal"],
            "damage_type": "Earth",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Freeze":{
        "tags":["battle","attack","spell","cleave"],
        "name": "Freeze",
        "description":"Drop the temperature of a creature severely.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Cold"]["normal"],
            "damage_type": "Cold",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Heat":{
        "tags":["battle","attack","spell","cleave"],
        "name": "Heat",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Fire"]["normal"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 2
    },
    "Bolt":{
        "tags":["battle","attack","spell","cleave","light"],
        "name": "Bolt",
        "description":"Blast a creature with a heavy wind.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Wind"]["normal"],
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Quake":{
        "tags":["battle","attack","spell","cleave"],
        "name": "Quake",
        "description":"Throw a god damn rock at them.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Earth"]["normal"],
            "damage_type": "Earth",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Torrent":{
        "tags":["battle","attack","spell"],
        "name": "Torrent",
        "description":"Drop the temperature of a creature severely.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Cold"]["powerful"],
            "damage_type": "Cold",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Flare":{
        "tags":["battle","attack","spell"],
        "name": "Flare",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Fire"]["powerful"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 1
    },
    "Slam":{
        "tags":["battle","attack","spell","light","haste:100"],
        "name": "Slam",
        "description":"Blast a creature with a heavy wind.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Wind"]["powerful"],
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 6
    },
    "Javelin":{
        "tags":["battle","attack","spell","penetrating"],
        "name": "Javelin",
        "description":"Throw a god damn rock at them.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Earth"]["powerful"],
            "damage_type": "Earth",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Banshee":{
        "tags":["battle","attack","spell","spirit"],
        "name": "Banshee",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Fire"]["powerful"],
            "damage_type": "Cold",
            "accuracy": 150,
        },
        "cooldown": 2
    },
    "Wail":{
        "tags":["battle","attack","spell","spirit","cleave"],
        "name": "Wail",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Fire"]["normal"],
            "damage_type": "Cold",
            "accuracy": 150,
        },
        "cooldown": 2
    },
    "Warp":{
        "tags":["battle","attack","spell","mirage:Elemental"],
        "name": "Warp",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Cold"]["powerful"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Shimmer":{
        "tags":["battle","attack","spell","mirage:Elemental","cleave"],
        "name": "Shimmer",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Cold"]["normal"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Explode":{
        "tags":["battle","attack","spell","cleave"],
        "name": "Explode",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": lambda lv: f"{lv}d{lv}",
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 4
    },
    "E-Beam":{
        "tags":["battle","attack","spell","energy:Elemental","light"],
        "name": "Energy Beam",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Wind"]["powerful"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 2
    },
    "E-Bomb":{
        "tags":["battle","attack","spell","energy:Elemental","cleave","light"],
        "name": "Energy Bomb",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Wind"]["normal"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 2
    },
    "Crush":{
        "tags":["battle","attack","spell","energy:Elemental","light"],
        "name": "Crush",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Earth"]["powerful"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "B-Hole":{
        "tags":["battle","attack","spell","energy:Elemental","cleave","light"],
        "name": "Black Hole",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Earth"]["normal"],
            "damage_type": "Fire",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Induction":{
        "tags":["battle","attack","spell","magnetic:Elemental","light"],
        "name": "Induction",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Wind"]["powerful"],
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Flux":{
        "tags":["battle","attack","spell","magnetic:Elemental","cleave","light"],
        "name": "Flux",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Wind"]["normal"],
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "C-Burst":{
        "tags":["battle","attack","spell","light"],
        "name": "Crystal Burst",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":3,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Earth"]["normal"],
            "damage_type": "Earth",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "C-Rain":{
        "tags":["battle","attack","spell","cleave","light"],
        "name": "Crystal Rain",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":3,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Earth"]["weak"],
            "damage_type": "Earth",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Fathom":{
        "tags":["battle","attack","spell","pressure:Elemental","light"],
        "name": "Fathom",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Cold"]["powerful"],
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "Atmosphere":{
        "tags":["battle","attack","spell","pressure:Elemental","cleave","light"],
        "name": "Atmosphere",
        "description":"Shower an enemy in super heated sparks.",
        "class":"Elemental",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Cold"]["normal"],
            "damage_type": "Wind",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    # DIVINE
    "Heal":{
        "tags":["map", "battle", "restorative"],
        "name": "Heal",
        "description":"Restore the body and mind of an ally.",
        "class":"Divine",
        "dynamic_restorative": lambda lv: f"{math.ceil(lv/2)}d5",
        "restorative": "1d5",
        "uses": 3
    },
    "Glint":{
        "tags":["battle","attack","spell"],
        "name": "Glint",
        "description":"launch a moat of light towards an enemy.",
        "class":"Divine",
        "attack":{
            "count":1,
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Divine"]["weak"],
            "damage_type": "Holy",
            "accuracy": 150,
        },
        "cooldown": 0
    },
    "S-Pixie":{
        "tags":["battle","map","summon"],
        "name": "Summon Pixie",
        "description":"Summon a Pixie to aid you.",
        "class":"Divine",
        "summon":{
            "creature":"Pixie"
        },
        "uses": 10
    },
    "S-Gnome":{
        "tags":["battle","map","summon"],
        "name": "Summon Gnome",
        "description":"launch a moat of light towards an enemy.",
        "class":"Divine",
        "summon":{
            "creature":"Gnome"
        },
        "uses": 1
    },
    "Drain":{
        "tags":["battle","attack","spell"],
        "name": "Glint",
        "description":"launch a moat of light towards an enemy.",
        "class":"Divine",
        "attack":{
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Divine"]["normal"],
            "damage_type": "Necro",
            "accuracy": 150,
        },
        "cooldown": 2
    },
    "EnPower":{},
    "M-EnPower":{},
    "Bolster":{},
    "M-Bolster":{},
    "Quicken":{},
    "M-Quicken":{},
    "M-Heal":{},
    "Flash":{
        "tags":["battle","attack","spell","cleave"],
        "name": "Glint",
        "description":"launch a moat of light towards an enemy.",
        "class":"Divine",
        "attack":{
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Divine"]["weak"],
            "damage_type": "Holy",
            "accuracy": 150,
        },
        "cooldown": 1
    },
    "Feed":{
        "tags":["battle","attack","spell","cleave"],
        "name": "Glint",
        "description":"launch a moat of light towards an enemy.",
        "class":"Divine",
        "attack":{
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Divine"]["normal"],
            "damage_type": "Necro",
            "accuracy": 150,
        },
        "cooldown": 3
    },
    "S-Power":{},
    "S-Virtue":{},
    "Multi-S":{},
    "Resist":{},
    "Critster":{},
    "Deify":{},
    "Restore":{},
    "Dawn":{
        "tags":["battle","attack","spell","cleave"],
        "name": "Glint",
        "description":"launch a moat of light towards an enemy.",
        "class":"Divine",
        "attack":{
            "dynamic_damage": _DYNAMIC_DAMAGE_TABLE["Divine"]["powerful"],
            "damage_type": "Holy",
            "accuracy": 150,
        },
        "cooldown": 1
    },
    "S-Guardian":{},
    "S-Zealot":{},
    "S-Archon":{},
}
