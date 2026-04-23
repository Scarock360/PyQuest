CLASS_INDEX={
    "Martial":{
        "class_id": "Martial",
        "class_name":"Warrior",
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
                "ability_id":"Quad Attack",
                "description":"Quint Attack means you can hit five times when attacking.",
                "effect":{
                    "increase" :{
                        "attack_count": 1
                    }
                },
                "requirements":{
                    "description":"Requires 19 Martial abilities.",
                    "Investment" : {
                        "Martial": 19
                    }
                }
            }
        }
    },
    "Arcane":{
        "class_id": "Arcane",
        "class_name":"Mage",
        "type": "Base",
        "nodes": {
            "Arcane-1":{
                "ability_id":"Arcane-1",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Arcane-2":{
                "ability_id":"Arcane-2",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Arcane-3":{
                "ability_id":"Arcane-3",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Arcane-4":{
                "ability_id":"Arcane-4",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Arcane-5":{
                "ability_id":"Arcane-5",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
        }
    },
    "Divine":{
        "class_id": "Divine",
        "class_name":"Cleric",
        "type": "Base",
        "nodes": {
            "Divine-1":{
                "ability_id":"Divine-1",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Divine-2":{
                "ability_id":"Divine-2",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Divine-3":{
                "ability_id":"Divine-3",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Divine-4":{
                "ability_id":"Divine-4",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "Divine-5":{
                "ability_id":"Divine-5",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
        }
    },
    "Spell Sword":{
        "class_id": "Spell Sword",
        "class_name":"Spell Sword",
        "type": "Prestige",
        "required_base" : ["Martial","Arcane"],
        "nodes":{
            "True Spell Sword":{
                "ability_id":"True Spell Sword",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{
                    "Investment" : {
                        "Martial": 5,
                        "Arcane": 5,
                    }
                }
            },
            "ss-1":{
                "ability_id":"ss-1",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "ss-2":{
                "ability_id":"ss-2",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "ss-3":{
                "ability_id":"ss-3",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            },
            "ss-4":{
                "ability_id":"ss-4",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{}
            }
        }
    },
    "Paladin":{
        "class_id": "Paladin",
        "class_name":"Paladin",
        "type": "Prestige",
        "required_base" : ["Martial","Divine"],
        "nodes":{
            "True Paladin":{
                "ability_id":"True Paladin",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{
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
        "type": "Prestige",
        "required_base" : ["Divine","Arcane"],
        "nodes":{
            "True Magus":{
                "ability_id":"True Magus",
                "description":"PLACEHOLDER DESCRIPTION",
                "effect":{},
                "requirements":{
                    "Investment" : {
                        "Divine": 5,
                        "Arcane": 5,
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
