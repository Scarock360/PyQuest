from utils.utils import GREEN,ENDC,BLUE, MAGENTA
from maps.abstract_level import abstract_level
class tutorial(abstract_level):
    @classmethod
    def get_level(cls):
        return {
        "map": \
"""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓WTWt▓▓▓▓▓▓▓▓./  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓
▓▓▓▓▓▓▓▓WT▓▓▓▓▓▓▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓WTWtWTWtWTWtWT▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓
▓▓WtWTWtWTWtWTWt▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓▓▓WtWTWtWTWt▓▓▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓
▓▓▓▓▓▓WtWTWt▓▓▓▓▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓==▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░DRIB
▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓
▓▓░░  ░░  ░░  ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓==▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓
▓▓░░  ░░  ░░  ░░▓▓▒▒  ▒▒  ▒▒▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓▒▒  ▒▒  ▒▒▓▓
▓▓  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ⎹⎸  ▒▒  ▒▒  ▓▓
▓▓░░  ░░  ░░  ░░⎹⎸▒▒  ▒▒  ▒▒▓▓░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░▓▓▒▒  ▒▒  ▒▒▓▓
▓▓  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ░░  ▓▓  ▒▒  ▒▒  ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
""",
        "solid_chars":"▓⋐⋑𝍑WT./IB",
        "starting_position":{ "x": 8, "y": 14},
        "custom_interactions":[
            {
                "events":[
                    {"replace_all":{"replace":"WT","with":"░░"}},
                    {"replace_all":{"replace":"Wt","with":"  "}},
                    {"msg":"You hear water flowing nearby.\n"}
                ],
                "location": {"x":18,"y":2},
                "one_time":True
            }
        ],
        "default_interactions":
        {
            "▓▓": "Its just a wall.\n",
            "▒▒": "You feel safe here\n",
            "  ": "There's nothing on the floor here.\n",
            "░░": "There's nothing on the floor here.\n",
            "⋐⋑": "The chest is empty.\n",
            "⎹⎸" : "The door is open.\n",
            "==" : "The door is open.\n",
            "🕱🕱" : "Nothing but the dead.\n",
            "𝍑 " : "The enemy you ran from.\n",
            "WT" : "The water looks clear and refreshing.\n",
            "./" : "You've pulled this lever already.\n",
        },
        "colours": {
            "░░": "GREY",
            "▒▒": "CYAN",
            "▓▓": "BRIGHT_WHITE",
            "𝍑 ": "RED",
            "🕱🕱": "WHITE",
            "IB": "BLACK"
        },
        "escaped_tiles":{
            "WT": f"{BLUE}▒▒{ENDC}",
            "Wt": f"{BLUE}░░{ENDC}",
            "DR": f"{MAGENTA}▒▒{ENDC}"
        },
        "entry_text": f"Welcome to the tutorial.\nTo move use {GREEN}WASD{ENDC}",
        "encounters":[
            {
                "enemies":[
                    {
                        "creature":"Rat",
                        "level": 1
                    },
                    {
                        "creature":"Pigeon",
                        "level": 1
                    }
                ],
                "location": {"x":8,"y":10}
            },
            {
                "enemies":[{
                    "creature":"Clown",
                    "boss_name":"Bozo, the Swamp Clown",
                    "level":1
                }],
                "location": {"x":8,"y":4},
            },
            {
                "enemies":[{
                    "creature":"Dummy",
                    "boss_name":"dummy",
                    "level":1
                }],
                "location": {"x":2,"y":17},
            }
        ],
        "treasures":[
            {
                "items":[
                    {
                        "item":"Molotov",
                        "quantity": 3
                    },
                    {
                        "item":"War axe",
                        "quantity": 1
                    }
                ],
                "location": {"x":22,"y":13}
            },
            {
                "items":[
                    {
                        "item":"Potion",
                        "quantity": 3
                    },
                    {
                        "item":"Rusty lance",
                        "quantity": 1
                    }
                ],
                "location": {"x":6,"y":2}
            }
        ],
        "location_triggers":[
            {
                "location":{"x":76,"y":10},
                "events":[
                    {"change_level":{"level":"tutorial_outside", "location":{ "x": 86, "y": 16}}}
                ],
                "one_time":False
            }
        ]
    }
