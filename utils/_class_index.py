CLASS_INDEX={
    "Martial":{
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
        "type": "Base",
        "nodes": {}
    },
    "Divine":{
        "type": "Base",
        "nodes": {}
    }
}