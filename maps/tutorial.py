from utils.utils import GREEN,ENDC,BLUE, MAGENTA
from maps.abstract_level import abstract_level
class tutorial(abstract_level):
    @classmethod
    def get_level(cls):
        return {
        "map": \
"""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓T2Wt▓▓▓▓▓▓▓▓C1  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓
▓▓▓▓▓▓▓▓WT▓▓▓▓▓▓▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓WTWtWTB1WTWtWT▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓
▓▓WtWTWtWTWtWTWt▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓▓▓WtWTWtWTWt▓▓▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓
▓▓▓▓▓▓WtWTWt▓▓▓▓▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓==▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░D1IB
▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓░░  ░░E1░░  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓==▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓  ░░  ░░  ░░  ▓▓  ▒▒T1▒▒  ▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓
▓▓░░  ░░  ░░  ░░▓▓▒▒  ▒▒  ▒▒▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓▒▒  ▒▒  ▒▒▓▓
▓▓  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ⎹⎸  ▒▒  ▒▒  ▓▓
▓▓░░  ░░SP░░  ░░⎹⎸▒▒  ▒▒  ▒▒▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓▒▒  ▒▒  ▒▒▓▓
▓▓B2░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
""",
        "solid_chars":"▓⋐⋑⚠WTC1IB",
        "default_interactions":
        {
            "▓▓": "Its just a wall.\n",
            "▒▒": "You feel safe here\n",
            "  ": "There's nothing on the floor here.\n",
            "░░": "There's nothing on the floor here.\n",
            "⋐⋑": "The chest is empty.\n",
            "⎹⎸" : "The door is open.\n",
            "==" : "The door is open.\n",
            "☠ " : "Nothing but the dead.\n",
            "⚠ " : "The enemy you ran from.\n",
            "WT" : "The water looks clear and refreshing.\n",
            "./" : "You've pulled this lever already.\n",
        },
        "colours": {
            "░░": "GREY",
            "▒▒": "CYAN",
            "▓▓": "BRIGHT_WHITE",
            #"⚠ ": "RED",
            "☠ ": "WHITE",
            "IB": "BLACK"
        },
        "escaped_tiles":{
            "WT": f"{BLUE}▒▒{ENDC}",
            "Wt": f"{BLUE}░░{ENDC}",
            "D1": f"{MAGENTA}▒▒{ENDC}",
            "C1": "./",
            "SP": "  "
        },
        "entry_text": f"Welcome to the tutorial.\nTo move use {GREEN}WASD{ENDC}",
        "custom_interactions":{
            "C1":{
                "events":[
                    {"replace_all":{"replace":"WT","with":"░░"}},
                    {"replace_all":{"replace":"Wt","with":"  "}},
                    {"msg":"You hear water flowing nearby.\n"}
                ],
                #"location": {"x":18,"y":2},
                "one_time":True
            }
        },
        "enemies":{
            "E1":{
                "enemies":[
                    {
                        "creature":"Hat Rat",
                        "level": 1
                    },
                    {
                        "creature":"Pigeon",
                        "level": 1
                    }
                ]
            },
            "B1":{
                "enemies":[{
                    "creature":"Clown",
                    "boss_name":"Bozo, the Swamp Clown",
                    "level":2
                }]
            },
            "B2":{
                "enemies":[{
                    "creature":"Dummy",
                    "boss_name":"dummy",
                    "level":1
                }],
            }
        },
        "treasures":{
            "T1":{
                "items":[
                    {
                        "item":"Molotov",
                        "quantity": 3
                    },
                    {
                        "item":"War axe",
                        "quantity": 1
                    }
                ]
            },
            "T2":{
                "items":[
                    {
                        "item":"Potion",
                        "quantity": 3
                    },
                    {
                        "item":"Rusty lance",
                        "quantity": 1
                    }
                ]
            }
        },
        "location_triggers":{
            "D1":{
                "events":[
                    {
                        "change_level":{
                            "level":"tutorial_outside",
                            "location":{ "x": 86, "y": 16},
                            "tile": "D1"
                        }
                    }
                ],
                "one_time":False
            }
        }
    }
