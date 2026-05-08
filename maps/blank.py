from utils.utils import GREEN,ENDC,BLUE, MAGENTA
from maps.abstract_level import abstract_level
class blank(abstract_level):
    @classmethod
    def get_level(cls):
        return {
        "map": \
"""
▓▓▓▓▓▓▓▓
▓▓SP░░▓▓
▓▓▓▓▓▓▓▓
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
        "colours": {},
        "escaped_tiles":{
            "SP": "  "
        },
        "entry_text": "",
        "custom_interactions":{},
        "enemies":{},
        "treasures":{},
        "location_triggers":{}
    }
