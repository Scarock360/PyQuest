import math
import sys
import re
sys.path.insert(0,"../PyQuest\\game_states" )
sys.path.insert(0,"../PyQuest\\resources" )
from game_state import AbstractGameState
from utils._item_index import ITEM_INDEX
from utils.utils import GREEN, GREY, ENDC, chunks, roll, text_len
from functools import partial

class InventoryState(AbstractGameState):
    menu_options = [
        "Use",
        "Discard",
        "Combine",
        "Back"
    ]

    row_selection = {"min":0,"c_min":0,"c":0,"c_max":0,"max":0}
    selected_item=0
    previous_state=""

    @classmethod
    def setup(cls,game):
        cls.GAME = game

    @classmethod
    def pre_shift(cls,previous_state):
        cls.previous_state = previous_state
        max_selection = math.ceil(len(cls.GAME.inventory)/2)-1
        cls.selected_item = 0
        cls.row_selection={
            "min":0,
            "c_min":0,
            "c":0,
            "c_max":min(max_selection,10),
            "max":max_selection
        }
        cls.previous_dialog = cls.GAME.dialog_box
        cls.change_selection(1)
        cls.change_selection(-1)

    @classmethod
    def handle_inputs(cls,key):
        match f"{key}":
            case "'w'":
                cls.change_selection(-2)
            case "'d'":
                cls.change_selection(1)
            case "'a'":
                cls.change_selection(-1)
            case "'s'":
                cls.change_selection(2)

    @classmethod
    def change_selection(cls,change):
        new_selection = cls.selected_item + change
        if new_selection < 0 or new_selection > len(cls.GAME.inventory) - 1:
            return
        cls.selected_item = new_selection

        r_s = cls.row_selection
        r_s["c"] = math.floor((new_selection)/2)

        if r_s["c"] == r_s["c_min"]:
            if r_s["c_min"] != r_s["min"]:
                r_s["c_min"] -= 1
                r_s["c_max"] -= 1

        if r_s["c"] == r_s["c_max"]:
            if r_s["c_max"] != r_s["max"]:
                r_s["c_max"] += 1
                r_s["c_min"] += 1

        items = list(cls.GAME.inventory.items())
        items.sort(key= lambda x: -int(cls.previous_state in ITEM_INDEX[x[0]]["tags"]))
        item_name = items[cls.selected_item][0]
        cls.GAME.dialog_box = ITEM_INDEX.get(item_name,{"Description":"Unknown item\n"})["Description"]
        cls.generate_display()

    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "Use":
                cls.use_item()
            case "Back":
                cls.GAME.change_state(cls.previous_state)
                cls.GAME.dialog_box = cls.previous_dialog

    @classmethod
    def _use_restorative(cls, item, target):
        item_detail = ITEM_INDEX[item]
        restored_hit_points = cls.GAME.party[target].restore_hit_points(item_detail["restorative"])
        cls.GAME.update_health_bars()
        message = f"{cls.GAME.party[target].name} consumed the {item} restoring "+\
            f"{GREEN}{restored_hit_points}{ENDC} hit points.\n"
        if "one-use" in item_detail["tags"]:
            cls.GAME.remove_item(item)
        if cls.previous_state == "battle":
            cls.GAME.states["battle"].combat_log.append(message)
            cls.GAME.states["battle"].combat_log_selected = -1
            cls.GAME.states["battle"].end_turn()
            cls.GAME.change_state("battle")
        else:
            cls.GAME.dialog_box= message
            cls.GAME.change_state("inventory")
            cls.GAME.states["inventory"].generate_display()

    @classmethod
    def _use_grenade(cls, item, target):
        item_detail = ITEM_INDEX[item]
        damage_delbt = target.take_damage(roll(item_detail['grenade']["amount"]),item_detail['grenade']["type"])
        cls.GAME.update_health_bars()
        message = f"You threw the {item} at {target.name} dealing {GREEN}{damage_delbt}{ENDC} {item_detail['grenade']['type']} damage.\n"
        if "one-use" in item_detail["tags"]:
            cls.GAME.remove_item(item)
        if cls.previous_state == "battle":
            cls.GAME.states["battle"].combat_log.append(message)
            cls.GAME.states["battle"].combat_log_selected = -1
            cls.GAME.states["battle"].end_turn()
            cls.GAME.change_state("battle")

    @classmethod
    def use_item(cls):
        items = list(cls.GAME.inventory.keys())
        items.sort(key= lambda x: -int(cls.previous_state in ITEM_INDEX[x]["tags"]))
        item = items[cls.selected_item]
        item_detail = ITEM_INDEX[item]
        item_tags = item_detail["tags"]
        if cls.previous_state in item_tags:
            if "restorative" in item_tags:
                options = {v.name:partial(cls._use_restorative,item,k) for k,v in cls.GAME.party.items()}
                options["Cancel"] = partial(cls.GAME.change_state,"inventory")
                
                cls.GAME.states["question"].pre_shift(
                    "inventory",
                    f"Who will use the {item}?",
                    options
                )
                cls.GAME.change_state("question")
            if "grenade" in item_tags:
                options = {
                    e.name: partial(cls._use_grenade,item,e) 
                    for e in cls.GAME.states["battle"].enemies
                }
                options["Cancel"] = partial(cls.GAME.change_state,"inventory")
                
                cls.GAME.states["question"].pre_shift(
                    "inventory",
                    f"Who will you throw the {item} at?",
                    options
                )
                cls.GAME.change_state("question")
        
        #     tags = item_detail["tags"]
        #     if "restorative" in tags:
                
        #         cls.GAME.dialog_box=f"You drank the {item}\n"
        #     elif "grenade" in tags:
        #         cls.GAME.dialog_box=f"You threw the {item}\n"
        #     else:
        #         cls.GAME.dialog_box=f"You used the {item}\n"
        #     if "one-use" in tags:
        #         cls.GAME.remove_item(item)
        # else:
        #     cls.GAME.dialog_box=f"You cant use the {item           } at this time.\n"
        # cls.generate_display()

    @classmethod
    def generate_display(cls):
        items = list(cls.GAME.inventory.items())

        if len(items) == 0:
            cls.GAME.change_state(cls.previous_state)
            cls.GAME.dialog_box = cls.previous_dialog
            return


        items.sort(key= lambda x: -int(cls.previous_state in ITEM_INDEX[x[0]]["tags"]))
        raw_view = [
            f"{'      ' if index != cls.selected_item else '    ➤ '}{GREY if not cls.previous_state in ITEM_INDEX[item[0]]['tags'] else ENDC}{item[0]}{'.'*(15-len(item[0]))}x{'0'*(3-len(f'{item[1]}'))}{item[1]}{ENDC}"
            for index,item in enumerate(items)
        ]
        

        view = ["   ".join(c) for c in chunks(raw_view, 2)][cls.row_selection["c_min"]:][:11]

        while len(view) < 11:
            view.append(" ")
        view = [f"{l}{' '*(60-text_len(l))}" for l in view]
        if cls.row_selection["c_min"] != cls.row_selection["min"]:
            view[0] = view[0][0:-2] + "⮙ "

        if cls.row_selection["c_max"] != cls.row_selection["max"]:
            view[-1] = view[-1][0:-2] + "⮛ "

        item_name = items[cls.selected_item][0]
        cls.GAME.play_area = "\n".join([f"{line}" for line in view])
