import sys, inspect
sys.path.insert(0,"../PyQuest\\game_states" )
from utils.utils import GREEN,YELLOW,CYAN,MAGENTA,ENDC,RED,BLINK
from game_state import AbstractGameState
from creature import Creature
from player_creature import PlayerCreature
from utils._skill_index import SKILL_INDEX

class TitleState(AbstractGameState):
    menu_options = [
        "New",
        "Continue",
        "Load",
        "Exit"
    ]

    TITLE_COLOUR = YELLOW+BLINK
    DEATH_COLOUR = RED+BLINK
    game_over = False

    @classmethod
    def setup(cls, game):
        cls.GAME = game

    @classmethod
    def pre_shift(cls):
        cls.game_over = True

    @classmethod
    def handle_inputs(cls,key):
        pass

    @classmethod
    def handle_menu_event(cls,event):
        match event:
            case "New":
                cls.GAME.states["map"].previously_visited={}
                cls.GAME.states["map"].load_level_from_file("tutorial")
                cls.GAME.party = {"hero": PlayerCreature("Hero",20,2,2,2,"1d3","Smash",100,{},list(SKILL_INDEX.keys()))}
                #cls.GAME.party["hero"].level = 20
                cls.GAME.inventory = {"Lesser Potion":5}
                cls.GAME.update_health_bars()
                cls.GAME.change_state("map")
            case "Exit":
                cls.GAME._running = False

    @classmethod
    def generate_display(cls):
        if cls.game_over:
            cls.GAME.dialog_box = f"        {RED}You've met with a terrible fate, haven't you?{ENDC}\n"
            cls.GAME.play_area = f"""
{cls.DEATH_COLOUR}                                                          {ENDC}
{cls.DEATH_COLOUR}    _____.___.              ________  .__           .___  {ENDC}
{cls.DEATH_COLOUR}    \__  |   | ____  __ __  \______ \ |__| ____   __| _/  {ENDC}
{cls.DEATH_COLOUR}     /   |   |/  _ \|  |  \  |    |  \|  |/ __ \ / __ |   {ENDC}
{cls.DEATH_COLOUR}     \____   (  ⟨_⟩ )  |  /  |    `   \  \  ___// /_/ |   {ENDC}
{cls.DEATH_COLOUR}     / ______|\____/|____/  /_______  /__|\___  >____ |   {ENDC}
{cls.DEATH_COLOUR}     \/                             \/        \/     \/   {ENDC}
{cls.DEATH_COLOUR}                                                          {ENDC}
{cls.DEATH_COLOUR}                                                          {ENDC}
"""
        else:
            cls.GAME.dialog_box = f"Welcome to PyQuest\nTo navigate the menu use the {GREEN}ARROW KEYS{ENDC} and {GREEN}ENTER{ENDC}"
            cls.GAME.play_area = f"""
{cls.TITLE_COLOUR}                                                          {ENDC}
{cls.TITLE_COLOUR} _________        ________                          __    {ENDC}
{cls.TITLE_COLOUR} \_____   \___.__.\_____  \  __ __   ____   _______/  |_  {ENDC}
{cls.TITLE_COLOUR}  |    ___⟨   |  | /  / \  \|  |  \_/ __ \ /  ___/\   __\\{ENDC}
{cls.TITLE_COLOUR}  |   |    \___  |/   \_/.  \  |  /\  ___/ \___ \  |  |   {ENDC}
{cls.TITLE_COLOUR}  |___|    / ____|\_____\ \_/____/  \___  ⟩____  ⟩ |__|   {ENDC}
{cls.TITLE_COLOUR}           \/            \__⟩           \/     \/         {ENDC}
{cls.TITLE_COLOUR}                                       :Why did i do this{ENDC}
{cls.TITLE_COLOUR}                                                          {ENDC}
"""