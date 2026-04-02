CLASS_INDEX={
    "Martial":{
        "class_name":"Warrior",
        "type": "Base",
        "nodes": {
            "Double Attack":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Powerful Hands":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Dual Wield":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Shield Master":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Power Stance":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Defensive Stance":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Agile Stance":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Double Attack"]}
                }
            },
            "Balanced Stance":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "number_of" : {"number": 2 , "of":["Power Stance","Defensive Stance","Agile Stance"]}}
                }
            },
            "Triple Attack":{
                "description":{},
                "effect":{},
                "requirements":{
                    "Investment" : 4
                }
            },
            "Giant Hands":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Triple Attack","Powerful Hands"]}
                }
            },
            "Twin Blade":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Triple Attack","Dual Wield"]}
                }
            },
            "Shield Lord":{
                "description":{},
                "effect":{},
                "requirements":{
                    "previous_nodes": { "all_of" : ["Triple Attack","Shield Master"]}
                }
            },
            "Quadruple Attack":{
                "description":{},
                "effect":{},
                "requirements":{
                    "Investment" : 9
                }
            }
        }
    },
    "Arcane":{
        "class_name":"Mage",
        "type": "Base",
        "nodes": {
            "Arcane-1":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Arcane-2":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Arcane-3":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Arcane-4":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Arcane-5":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
        }
    },
    "Divine":{
        "class_name":"Cleric",
        "type": "Base",
        "nodes": {
            "Divine-1":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Divine-2":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Divine-3":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Divine-4":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
            "Divine-5":{
                "description":{},
                "effect":{},
                "requirements":{}
            },
        }
    },
    "Spell Sword":{
        "class_name":"Spell Sword",
        "type": "Prestige",
        "nodes":{}
    },
    "Paladin":{
        "class_name":"Spell Sword",
        "type": "Prestige",
        "nodes":{}
    },
    "Magus":{
        "class_name":"Spell Sword",
        "type": "Prestige",
        "nodes":{}
    }
}
