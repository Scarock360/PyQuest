CLASS_INDEX={
    "Martial":{
        "class_id": "Martial",
        "class_name":"Warrior",
        "description": "A simple combat specialist, that maximises simple attacks.",
        "type": "Base",
        "nodes": {
            "Double Attack":{
                "ability_id":"Double Attack",
                "description":"Double attack means you can hit twice when attacking.",
                "effect":{
                    "increase" :{
                        "attack_count": 1
                    }
                },
                "requirements":{}
            },
            "Powerful Hands":{
                "ability_id":"Powerful Hands",
                "description":"Powerful hands lets you wield two handed weapons in one.",
                "effect":{
                    "increase_flag":{
                        "Powerful Hands": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Dual Wield":{
                "ability_id":"Dual Wield",
                "description":"Dual Wield lets you wield a weapon in your off hand.",
                "effect":{
                    "increase_flag":{
                        "Dual Wield": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Shield Master":{
                "ability_id":"Shield Master",
                "description":"Shield Master improves shields and even weaponises them.",
                "effect":{
                    "increase_flag":{
                        "Shield Master": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Power Stance":{
                "ability_id":"Power Stance",
                "description":"Power Stance: Adopt a stance that boosts power.",
                "effect":{
                    "skills": ["P-Stance"]
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Defensive Stance":{
                "ability_id":"Defensive Stance",
                "description":"Defensive Stance: Adopt a stance that boosts resilience.",
                "effect":{
                    "skills": ["D-Stance"]
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Agile Stance":{
                "ability_id":"Agile Stance",
                "description":"Agile Stance: Adopt a stance that boosts agility.",
                "effect":{
                    "skills": ["A-Stance"]
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Balanced Stance":{
                "ability_id":"Balanced Stance",
                "description":"Balanced Stance: Adopt a stance that boosts all stats.",
                "effect":{
                    "skills": ["B-Stance"]
                },
                "requirements":{
                    "description":"Requires two Stance abilities.",
                    "previous_nodes": { "number_of" : {"number": 2 , "of":["Power Stance","Defensive Stance","Agile Stance"]}}
                }
            },
            "Lunge":{
                "ability_id":"Lunge",
                "description":"Lunge: Sacrifice resilience for greater power.",
                "effect":{
                    "skills": ["Lunge"]
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Defend":{
                "ability_id":"Defend",
                "description":"Defend: Sacrifice agility for greater resilience.",
                "effect":{
                    "skills": ["Defend"]
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Thrust":{
                "ability_id":"Thrust",
                "description":"Thrust: Sacrifice power for greater agility.",
                "effect":{
                    "skills": ["Thrust"]
                },
                "requirements":{
                    "description":"Requires the Double Attack ability.",
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Executioner":{
                "ability_id":"Executioner",
                "description":"Execute: Single powerful strike.",
                "effect":{
                    "skills": ["Execute"]
                },
                "requirements":{
                    "description":"Requires the Lunge and Power Stance abilities.",
                    "previous_nodes": { "all_of" : ["Lunge","Power Stance"]}
                }
            },
            "Fortress":{
                "ability_id":"Fortress",
                "description":"Fortress: Multiply resilience and charge revenge counter.",
                "effect":{
                    "skills": ["Fortress"]
                },
                "requirements":{
                    "description":"Requires the Defend and Defensive Stance abilities.",
                    "previous_nodes": { "all_of" : ["Defend", "Defensive Stance"]}
                }
            },
            "Exploiter":{
                "ability_id":"Exploiter",
                "description":"Exploit: A single guaranteed critical hit.",
                "effect":{
                    "skills": ["Exploit"]
                },
                "requirements":{
                    "description":"Requires the Thrust and Agile Stance abilities.",
                    "previous_nodes": { "all_of" : ["Thrust", "Agile Stance"]}
                }
            },
            "Triple Attack":{
                "ability_id":"Triple Attack",
                "description":"Triple attack means you can hit thrice when attacking.",
                "effect":{
                    "increase" :{
                        "attack_count": 1
                    }
                },
                "requirements":{
                    "description":"Requires 4 Martial abilities.",
                    "Investment" : {
                        "Martial": 4
                    }
                }
            },
            "Giant Hands":{
                "ability_id":"Giant Hands",
                "description":"Giant Hands is a more potent version of Powerful Hands.",
                "effect":{
                    "increase_flag":{
                        "Powerful Hands": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Triple Attack and Powerful Hands abilities.",
                    "previous_nodes": { "all_of" : ["Triple Attack","Powerful Hands"]}
                }
            },
            "Twin Blade":{
                "ability_id":"Twin Blade",
                "description":"Twin Blade is a more potent version of Dual Wield.",
                "effect":{
                    "increase_flag":{
                        "Dual Wield": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Triple Attack and Dual Wield abilities.",
                    "previous_nodes": { "all_of" : ["Triple Attack","Dual Wield"]}
                }
            },
            "Shield Lord":{
                "ability_id":"Shield Lord",
                "description":"Shield Lord is a more potent version of Shield Master.",
                "effect":{
                    "increase_flag":{
                        "Shield Master": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Triple Attack and Shield Master abilities.",
                    "previous_nodes": { "all_of" : ["Triple Attack","Shield Master"]}
                }
            },
            "Quad Attack":{
                "ability_id":"Quad Attack",
                "description":"Quad attack means you can hit four times when attacking.",
                "effect":{
                    "increase" :{
                        "attack_count": 1
                    }
                },
                "requirements":{
                    "description":"Requires 9 Martial abilities.",
                    "Investment" : {
                        "Martial": 9
                    }
                }
            },
            "Quint Attack":{
                "ability_id":"Quint Attack",
                "description":"Quint Attack means you can hit five times when attacking.",
                "effect":{
                    "increase" :{
                        "attack_count": 1
                    }
                },
                "requirements":{
                    "description":"Requires all other Martial abilities.",
                    "Investment" : {
                        "Martial": 19
                    }
                }
            }
        }
    },
    "Elemental":{
        "class_id": "Elemental",
        "class_name":"Mage",
        "description": "An arcane master of fire and ice, wind and earth.",
        "type": "Base",
        "nodes": {
            "Chill":{
                "ability_id":"Chill",
                "description":"Chill: a single target cold spell.",
                "effect":{
                    "skills": ["Chill"]
                },
                "requirements":{}
            },
            "Freeze":{
                "ability_id":"Freeze",
                "description":"Freeze: a multi target cold spell.",
                "effect":{
                    "skills": ["Freeze"],
                    "increase_flag":{
                        "Cold Adept": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Chill ability.",
                    "previous_nodes": { "all_of" : ["Chill"]}
                }
            },
            "Torrent":{
                "ability_id":"Torrent",
                "description":"Torrent: a powerful single target cold spell.",
                "effect":{
                    "skills": ["Torrent"]
                },
                "requirements":{
                    "description":"Requires the Freeze ability.",
                    "previous_nodes": { "all_of" : ["Freeze"]}
                }
            },
            "Spark":{
                "ability_id":"Spark",
                "description":"Spark: a single target fire spell.",
                "effect":{
                    "skills": ["Spark"]
                },
                "requirements":{}
            },
            "Heat":{
                "ability_id":"Heat",
                "description":"Heat: a multi target fire spell.",
                "effect":{
                    "skills": ["Heat"],
                    "increase_flag":{
                        "Fire Adept": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Spark ability.",
                    "previous_nodes": { "all_of" : ["Spark"]}
                }
            },
            "Flare":{
                "ability_id":"Flare",
                "description":"Flare: a powerful single target fire spell.",
                "effect":{
                    "skills": ["Flare"]
                },
                "requirements":{
                    "description":"Requires the Heat ability.",
                    "previous_nodes": { "all_of" : ["Heat"]}
                }
            },
            "Gust":{
                "ability_id":"Gust",
                "description":"Shunt: a single target wind spell",
                "effect":{
                    "skills": ["Shunt"]
                },
                "requirements":{}
            },
            "Thunder":{
                "ability_id":"Thunder",
                "description":"Thunder: a multi target wind spell.",
                "effect":{
                    "skills": ["Bolt"],
                    "increase_flag":{
                        "Wind Adept": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Gust ability.",
                    "previous_nodes": { "all_of" : ["Gust"]}
                }
            },
            "Kinetic":{
                "ability_id":"Kinetic",
                "description":"Slam: a powerful single target wind spell.",
                "effect":{
                    "skills": ["Slam"]
                },
                "requirements":{
                    "description":"Requires the Thunder ability.",
                    "previous_nodes": { "all_of" : ["Thunder"]}
                }
            },
            "Rock and Stone":{
                "ability_id":"Rock and Stone",
                "description":"Toss rock: a single target earth spell.",
                "effect":{
                    "skills": ["Toss rock"],
                },
                "requirements":{}
            },
            "Quake":{
                "ability_id":"Quake",
                "description":"Quake: a multi target earth spell.",
                "effect":{
                    "skills": ["Quake"]
                },
                "requirements":{
                    "description":"Requires the Rock and Stone ability.",
                    "previous_nodes": { "all_of" : ["Rock and Stone"]}
                }
            },
            "Steel":{
                "ability_id":"Steel",
                "description":"Javelin: a powerful single target spell.",
                "effect":{
                    "skills": ["Javelin"],
                },
                "requirements":{
                    "description":"Requires the Quake ability.",
                    "previous_nodes": { "all_of" : ["Quake"]}
                }
            },
            "Spirit":{
                "ability_id":"Spirit",
                "description":"Mastery over the creation of weaponised false souls.",
                "effect":{
                    "skills": [
                        "Banshee",
                        "Wail"
                    ]
                },
                "requirements":{
                    "description":"Requires the Flare and Freeze abilities.",
                    "previous_nodes": { "all_of" : ["Flare","Freeze"]}
                }
            },
            "Mirage":{
                "ability_id":"Mirage",
                "description":"Mastery over what others are allowed to perceive.",
                "effect":{
                    "skills": [
                        "Warp",
                        "Shimmer"
                    ]
                },
                "requirements":{
                    "description":"Requires the Torrent and Heat abilities.",
                    "previous_nodes": { "all_of" : ["Torrent","Heat"]}
                }
            },
            "Detonation":{
                "ability_id":"Detonation",
                "description":"Mastery over imesureable force.",
                "effect":{
                "effect":{
                    "skills": [
                        "Explode"
                    ]
                },},
                "requirements":{
                    "description":"Requires the Kinetic and Heat abilities.",
                    "previous_nodes": { "all_of" : ["Kinetic","Heat"]}
                }
            },
            "Energy":{
                "ability_id":"Energy",
                "description":"Mastery over the manipulation of pure energy.",
                "effect":{
                    "skills": [
                        "E-Beam",
                        "E-Bomb"
                    ]
                },
                "requirements":{
                    "description":"Requires the Flare and Thunder Stance abilities.",
                    "previous_nodes": { "all_of" : ["Flare","Thunder"]}
                }
            },
            "Gravity":{
                "ability_id":"Gravity",
                "description":"Mastery over the fundamental force of gravity.",
                "effect":{
                    "skills": [
                        "Crush",
                        "B-Hole"
                    ]
                },
                "requirements":{
                    "description":"Requires the Kinetic and Quake abilities.",
                    "previous_nodes": { "all_of" : ["Kinetic","Quake"]}
                }
            },
            "Magnetic":{
                "ability_id":"Magnetic",
                "description":"Mastery over repelling and attracting magics.",
                "effect":{
                    "skills": [
                        "Induction",
                        "Flux"
                    ]
                },
                "requirements":{
                    "description":"Requires the Steal and Thunder abilities.",
                    "previous_nodes": { "all_of" : ["Steel","Thunder"]}
                }
            },
            "Crystal":{
                "ability_id":"Crystal",
                "description":"Mastery over energised crystalline structures.",
                "effect":{
                    "skills": [
                        "C-Burst",
                        "C-Rain"
                    ]
                },
                "requirements":{
                    "description":"Requires the Steel and Freeze abilities.",
                    "previous_nodes": { "all_of" : ["Steel","Freeze"]}
                }
            },
            "Pressure":{
                "ability_id":"Pressure",
                "description":"Mastery over the pressure within encased objects.",
                "effect":{
                    "skills": [
                        "Fathom",
                        "Atmosphere"
                    ]
                },
                "requirements":{
                    "description":"Requires the Torrent and Quake abilities.",
                    "previous_nodes": { "all_of" : ["Torrent","Quake"]}
                }
            },
        }
    },
    "Divine":{
        "class_id": "Divine",
        "class_name":"Cleric",
        "description": "A servant of heaven that amplifies their allies strengths.",
        "type": "Base",
        "nodes": {
            "Basic Divine Magic":{
                "ability_id":"Basic Divine Magic",
                "description":"Teaches the basic divine spells Heal and Glint.",
                "effect":{
                    "skills": [
                        "Heal",
                        "Glint"
                    ]
                },
                "requirements":{}
            },
            "Fae Summons":{
                "ability_id":"Fae Summons",
                "description":"Teaches the ability to summon pixies and Gnomes.",
                "effect":{
                    "skills": [
                        "S-Pixie",
                        "S-Gnome"
                    ]
                },
                "requirements":{
                    "description":"Requires the Basic Divine Magic ability.",
                    "previous_nodes": { "all_of" : ["Basic Divine Magic"]}
                }
            },
            "Basic Vampiric Magic":{
                "ability_id":"Basic Vampiric Magic",
                "description":"Teaches the basic vampiric spell Drain.",
                "effect":{
                    "skills": [
                        "Drain"
                    ]
                },
                "requirements":{
                    "description":"Requires the Basic Divine Magic ability.",
                    "previous_nodes": { "all_of" : ["Basic Divine Magic"]}
                }
            },
            "EnPower":{
                "ability_id":"EnPower",
                "description":"Teaches the buff spell EnPower.",
                "effect":{
                    "skills": [
                        "EnPower"
                    ]
                },
                "requirements":{
                    "description":"Requires the Basic Divine Magic ability.",
                    "previous_nodes": { "all_of" : ["Basic Divine Magic"]}
                }
            },
            "Mass EnPower":{
                "ability_id":"Mass EnPower",
                "description":"Teaches the buff spell Mass EnPower.",
                "effect":{
                    "skills": [
                        "M-EnPower"
                    ]
                },
                "requirements":{
                    "description":"Requires the EnPower ability.",
                    "previous_nodes": { "all_of" : ["EnPower"]}
                }
            },
            "Bolster":{
                "ability_id":"Bolster",
                "description":"Teaches the buff spell Bolster.",
                "effect":{
                    "skills": [
                        "Bolster"
                    ]
                },
                "requirements":{
                    "description":"Requires the Basic Divine Magic ability.",
                    "previous_nodes": { "all_of" : ["Basic Divine Magic"]}
                }
            },
            "Mass Bolster":{
                "ability_id":"Mass Bolster",
                "description":"Teaches the buff spell Mass Bolster.",
                "effect":{
                    "skills": [
                        "M-Bolster"
                    ]
                },
                "requirements":{
                    "description":"Requires the Bolster ability.",
                    "previous_nodes": { "all_of" : ["Bolster"]}
                }
            },
            "Quicken":{
                "ability_id":"Quicken",
                "description":"Teaches the buff spell Quicken.",
                "effect":{
                    "skills": [
                        "Quicken"
                    ]
                },
                "requirements":{
                    "description":"Requires the Basic Divine Magic ability.",
                    "previous_nodes": { "all_of" : ["Basic Divine Magic"]}
                }
            },
            "Mass Quicken":{
                "ability_id":"Mass Quicken",
                "description":"Teaches the buff spell Mass Quicken.",
                "effect":{
                    "skills": [
                        "M-Quicken"
                    ]
                },
                "requirements":{
                    "description":"Requires the Quicken ability.",
                    "previous_nodes": { "all_of" : ["Quicken"]}
                }
            },
            "Advanced Divine Magic":{
                "ability_id":"Advanced Divine Magic",
                "description":"Teaches the advanced divine spells Mass Heal and Flash.",
                "effect":{
                    "skills": [
                        "M-Heal",
                        "Flash"
                    ]
                },
                "requirements":{
                    "description":"Requires 4 Martial abilities.",
                    "Investment" : {
                        "Divine": 4
                    }
                }
            },
            "Advanced Vampiric Magic":{
                "ability_id":"Advanced Vampiric Magic",
                "description":"Teaches the advanced vampiric spell Feed.",
                "effect":{
                    "skills": [
                        "Feed"
                    ]
                },
                "requirements":{
                    "description":"Requires Advanced Divine and Basic Vampiric Magic abilities.",
                    "previous_nodes": { "all_of" : ["Advanced Divine Magic","Basic Vampiric Magic"]}
                }
            },
            "Angelic Summons":{
                "ability_id":"Angelic Summons",
                "description":"Teaches the ability to summon Powers and Virtues.",
                "effect":{
                    "skills": [
                        "S-Power",
                        "S-Virtue"
                    ]
                },
                "requirements":{
                    "description":"Requires Advanced Divine Magic and Fae Summons abilities.",
                    "previous_nodes": { "all_of" : ["Advanced Divine Magic","Fae Summons"]}
                }
            },
            "Multi Strike":{
                "ability_id":"Multi Strike",
                "description":"Teaches the buff spell Multi Strike.",
                "effect":{
                    "skills": [
                        "Multi-S",
                    ]
                },
                "requirements":{
                    "description":"Requires Advanced Divine Magic and Mass EnPower abilities.",
                    "previous_nodes": { "all_of" : ["Advanced Divine Magic","Mass EnPower"]}
                }
            },
            "Resist":{
                "ability_id":"Resist",
                "description":"Teaches the buff spell Resist.",
                "effect":{
                    "skills": [
                        "Resist",
                    ]
                },
                "requirements":{
                    "description":"Requires Advanced Divine Magic and Mass Bolster abilities.",
                    "previous_nodes": { "all_of" : ["Advanced Divine Magic","Mass Bolster"]}
                }
            },
            "Critster":{
                "ability_id":"Critster",
                "description":"Teaches the buff spell Critster.",
                "effect":{
                    "skills": [
                        "Critster",
                    ]
                },
                "requirements":{
                    "description":"Requires Advanced Divine Magic and Mass Quicken abilities.",
                    "previous_nodes": { "all_of" : ["Advanced Divine Magic","Mass Quicken"]}
                }
            },
            "Deify":{
                "ability_id":"Deify",
                "description":"Teaches the buff spell Deify.",
                "effect":{
                    "skills": [
                        "Deify",
                    ]
                },
                "requirements":{
                    "description":"Requires Multi Strike, resist and Critster abilities.",
                    "previous_nodes": { "all_of" : ["Multi Strike","Resist","Critster"]}
                }
            },
            "Mastered Divine Magic":{
                "ability_id":"Mastered Divine Magic",
                "description":"Teaches the master divine spells Restore and Dawn.",
                "effect":{
                    "skills": [
                        "Restore",
                        "Dawn"
                    ]
                },
                "requirements":{
                    "description":"Requires Advanced Divine Magic and 8 other divine abilities.",
                    
                    "previous_nodes": {
                        "all_of" : ["Advanced Divine Magic"]
                    },
                    "Investment" : {
                        "Divine": 9
                    }
                }
            },
            "Summon Divine Guardian":{
                "ability_id":"Summon Divine Guardian",
                "description":"Teaches the ability to summon Divine Guardians.",
                "effect":{
                    "skills": [
                        "S-Guardian",
                    ]
                },
                "requirements":{
                    "description":"Requires Angelic Summons and 8 other divine abilities.",
                    "previous_nodes": {
                        "all_of" : ["Angelic Summons"],
                    },
                    "Investment" : {
                        "Divine": 9
                    }
                }
            },
            "Summon Avenging Angel":{
                "ability_id":"Summon Avenging Angel",
                "description":"Teaches the ability to summon Zealot.",
                "effect":{
                    "skills": [
                        "S-Zealot",
                    ]
                },
                "requirements":{
                    "description":"Requires Angelic Summons and 8 other divine abilities.",
                    "previous_nodes": {
                        "all_of" : ["Angelic Summons"]
                    },
                    "Investment" : {
                        "Divine": 9
                    }
                }
            },
            "Summon Archon":{
                "ability_id":"Summon Archon",
                "description":"Teaches the ability to summon Zealots.",
                "effect":{
                    "skills": [
                        "S-Archon",
                    ]
                },
                "requirements":{
                    "description":"Requires all other divine abilities.",
                    "Investment" : {
                        "Divine": 19
                    }
                }
            },
        }
    },
    "Enchanter":{
        "class_id": "Enchanter",
        "class_name":"Enchanter",
        "description": "An arcane specialist that augments all actions with magic.",
        "type": "Prestige",
        "required_base" : ["Martial","Elemental"],
        "nodes":{
            "True Enchanter":{
                "ability_id":"True Enchanter",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{
                    "description":"Requires 5 Martial and Elemental abilities.",
                    "Investment" : {
                        "Martial": 5,
                        "Elemental": 5,
                    }
                }
            },
            "Mirage Enchantment":{
                "ability_id":"Mirage Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Mirage Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Mirage abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Mirage"]}
                }
            },
            "Spirit Enchantment":{
                "ability_id":"Spirit Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Spirit Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Spirit abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Spirit"]}
                }
            },
            "Energy Enchantment":{
                "ability_id":"Energy Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Energy Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Energy abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Energy"]}
                }
            },
            "Detonation Enchantment":{
                "ability_id":"Detonation Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Detonation Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Detonation abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Detonation"]}
                }
            },
            "Gravity Enchantment":{
                "ability_id":"Gravity Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Gravity Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Gravity abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Gravity"]}
                }
            },
            "Magnetic Enchantment":{
                "ability_id":"Magnetic Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Magnetic Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Magnetic abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Magnetic"]}
                }
            },
            "Crystal Enchantment":{
                "ability_id":"Crystal Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Crystal Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Crystal abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Crystal"]}
                }
            },
            "Pressure Enchantment":{
                "ability_id":"Pressure Enchantment",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{
                    "increase_flag":{
                        "Pressure Enchantment": 1
                    }
                },
                "requirements":{
                    "description":"Requires the Balanced Stance and Pressure abilities.",
                    "previous_nodes": { "all_of" : ["Balanced Stance","Pressure"]}
                }
            },
        }
    },
    "Paladin":{
        "class_id": "Paladin",
        "class_name":"Paladin",
        "description": "A holy warrior that wields the wrath of god and cold steel.",
        "type": "Prestige",
        "required_base" : ["Martial","Divine"],
        "nodes":{
            "True Paladin":{
                "ability_id":"True Paladin",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{
                    "description":"Requires 5 Martial and Divine abilities.",
                    "Investment" : {
                        "Martial": 5,
                        "Divine": 5,
                    }
                }
            },
            "p-1":{
                "ability_id":"p-1",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "p-2":{
                "ability_id":"p-2",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "p-3":{
                "ability_id":"p-3",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "p-4":{
                "ability_id":"p-4",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
        }
    },
    "Magus":{
        "class_id": "Magus",
        "class_name":"Magus",
        "description": "An arcane powerhouse capable of casting incredible spells.",
        "type": "Prestige",
        "required_base" : ["Divine","Elemental"],
        "nodes":{
            "True Magus":{
                "ability_id":"True Magus",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{
                    "description":"Requires 5 Elemental and Divine abilities.",
                    "Investment" : {
                        "Divine": 5,
                        "Elemental": 5,
                    }
                }
            },
            "m-1":{
                "ability_id":"p-1",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "m-2":{
                "ability_id":"p-2",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "m-3":{
                "ability_id":"p-3",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "m-4":{
                "ability_id":"p-4",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
        }
    }
}