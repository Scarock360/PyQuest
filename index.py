import os
import ctypes
from pynput.keyboard import Listener as KeyboardListner
import time
from utils.utils import tl,tr,bl,br,hr,vt,lt,rt,tt,bt, text_len
from utils._item_index import ITEM_INDEX
from game_states.map_state import MapState
from game_states.title_state import TitleState
from game_states.battle_state import BattleState
from game_states.Inventory_state import InventoryState
from game_states.equipment_state import EquipmentState
from game_states.question_state import QuestionState
from game_states.skills_state import SkillsState
from game_states.status_state import StatusState




class Game:
    window = os.getppid()

    states = {
        "map": MapState,
        "title": TitleState,
        "battle": BattleState,
        "inventory": InventoryState,
        "equipment": EquipmentState,
        "question": QuestionState,
        "skills": SkillsState,
        "status": StatusState
    }

    current_state = TitleState

    inventory = {}

    party = {}
    dialog_box = ""
    _party = "            "
    _menu = ""
    _menu_values = {"min":0,"c_min":0,"c":0,"c_max":0,"max":0}
    play_area=""
    _pressed = []
    _running = True
    _render = True

    @classmethod
    def setup(cls):
        for _,state in cls.states.items():
            state.setup(cls)
        menu_max = len(Game.current_state.menu_options)-1
        cls._menu_values= {"min":0,"c_min":0,"c":0,"c_max":min(menu_max,3),"max":menu_max}

        class _CursorInfo(ctypes.Structure):
            _fields_ = [("size", ctypes.c_int),
                        ("visible", ctypes.c_byte)]

        if os.name == 'nt':
            ci = _CursorInfo()
            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
            ci.visible = False
            ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
        elif os.name == 'posix':
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()

    @classmethod
    def _print_screen(cls):
        if cls._render:
            print("\033[0;0H")
            top = f"{tl}{hr*3}PARTY{hr*4}{tt}{hr*60}{tr}"
            p = [f"{vt}{l}{vt}" for l in cls._party.split("\n")]
            while len(p) < 9:
                p.append(f"{vt}{' '*12}{vt}")

            party = "\n".join(p)
            seperator = f"{lt}{hr*3}MENUS{hr*4}{rt}"
            menu = "\n".join([f"{vt}{l}{' '*(12-text_len(l))}{vt}" for l in cls._menu.split("\n")])
            bottom = f"{bl}{hr*12}{bt}{hr*60}{br}"

            screen_lines ="\n".join([
                top,
                party,
                seperator,
                menu,
                bottom
            ]).split("\n")

            screen_lines[-4] = screen_lines[-4][:-1] + lt + f"{hr*60}{rt}"

            for index,line in enumerate(cls.play_area.split("\n")):
                screen_lines[index+1] += f"{line}{' '*(60-text_len(line))}{vt}"

            for index,line in enumerate(cls.dialog_box.split("\n")):
                screen_lines[(-3)+index] += f"{line}{' '*(60-text_len(line))}{vt}"



            print("\n".join(screen_lines))

    @classmethod
    def menu_up(cls):
        mvs=cls._menu_values

        if mvs["c"] == mvs["min"]:
            return
        mvs["c"] -= 1

        if mvs["c"] == mvs["c_min"] and mvs["c_min"] != mvs["min"]:
            mvs["c_min"] -= 1
            mvs["c_max"] -= 1
        cls.create_menu()

    @classmethod
    def menu_down(cls):
        mvs=cls._menu_values

        if mvs["c"] == mvs["max"]:
            return
        mvs["c"] += 1

        if mvs["c"] == mvs["c_max"] and mvs["c_max"] != mvs["max"]:
            mvs["c_min"] += 1
            mvs["c_max"] += 1
        cls.create_menu()

    @classmethod
    def create_menu(cls):
        menu = []
        menu_options = list(cls.current_state.menu_options)
        mvs = cls._menu_values
        for i, menu_option in enumerate(menu_options):
            if i == mvs["c"]:
                menu.append(f"➤ {menu_option}")
            elif i == mvs["c_min"]:
                if mvs["c_min"] != mvs["min"]:
                    menu.append(f"⮙ {menu_option}")
                else:
                    menu.append(f"  {menu_option}")
            elif i == mvs["c_max"]:
                if mvs["c_max"] != mvs["max"]:
                    menu.append(f"⮛ {menu_option}")
                else:
                    menu.append(f"  {menu_option}")
            else:
                menu.append(f"  {menu_option}")

        menu = menu[mvs["c_min"]:mvs["c_max"]+1]
        while len(menu) < 4:
            menu.append("")

        cls._menu = "\n".join(menu)

    @classmethod
    def create_play_area(cls):
        cls.current_state.generate_display()

    @classmethod
    def process_input(cls,key):
        try:
            if not key in cls._pressed:
                match f"{key}":
                    case "Key.esc":
                        cls._running = False
                    case "Key.down":
                        cls.menu_down()
                    case "Key.up":
                        cls.menu_up()
                    case "Key.enter":
                        cls.current_state.handle_menu_event(
                            cls.current_state.menu_options[
                                cls._menu_values["c"]
                            ]
                        )
                    case "'r'":
                        cls._render = not cls._render
                        if not cls._render:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("\033[0;0H")
                            print("rendering disabled")
                cls.current_state.handle_inputs(key)
                cls._pressed.append(key)
        except Exception as e:
            cls._render = False
            print("\033[17;0H")
            raise e



    @classmethod
    def process_release(cls,key):
        if key in cls._pressed:
            cls._pressed.remove(key)

    @classmethod
    def change_state(cls,state):
        cls.current_state = cls.states[state]
        cls.current_state.generate_display()
        menu_max = len(Game.current_state.menu_options)-1
        cls._menu_values= {"min":0,"c_min":0,"c":0,"c_max":min(menu_max,3),"max":menu_max}
        cls.create_menu()

    @classmethod
    def add_item(cls,item,count=1):
        if item is None:
            return
        if item not in cls.inventory:
            cls.inventory[item] = 0
        cls.inventory[item] += count
        cls.inventory[item] = min(cls.inventory[item],999)

    @classmethod
    def remove_item(cls,item,count=1):
        if item is None:
            return
        cls.inventory[item] -= count
        if cls.inventory[item] < 0:
            pass
        if cls.inventory[item] == 0:
            cls.inventory.pop(item)

    @classmethod
    def update_health_bars(cls):
        cls._party="\n".join([c.create_health_bar() for _,c in cls.party.items()])

    @classmethod
    def write_to_dialog_box(cls, message):
        valid = True
        split_message = message.split("\n")
        for line in split_message:
            if text_len(line) > 60:
                valid = False
        if valid:
            cls.dialog_box = message
            return
        else:
            one_line_message =" ".join(split_message)
            if text_len(one_line_message) > 120:
                pass
            else:
                words = one_line_message.split(" ")
                line = words.pop(0)
                while(len(words)>0 and text_len(line+ f"{words[0]}") < 60):
                    line = " ".join([line, words.pop(0)])
                line2 = " ".join(words)
                if text_len(line) < 60 and text_len(line2) < 60:
                    cls.dialog_box = "\n".join([line,line2])


if __name__ == "__main__":
    held = {}
    Game.setup()
    Game.create_menu()
    Game.create_play_area()
    keyboard_listner = KeyboardListner(on_press=Game.process_input,on_release=Game.process_release)
    keyboard_listner.start()
    frame = 0
    while Game._running:
        frame += 1
        if frame == 7:
            frame = 0
        for button in Game._pressed:
            if button not in held:
                held[button] = frame
            elif held[button] == frame:
                held.pop(button)
                Game._pressed.pop(Game._pressed.index(button))
        Game._print_screen()
        time.sleep(0.0167)
