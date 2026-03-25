import random

tl = '╔'
tr = '╗'
bl = '╚'
br = '╝'
hr = '═'
vt = '║'

lt = '╠'
rt = '╣'
tt = '╦'
bt = '╩'

FULL_BLOCK  = u'\u2593'
HALF_BLOCK  = u'\u2592'
EMPTY_BLOCK = u'\u2591'

BLACK           = '\033[0;30m'
RED             = '\033[0;31m'
GREEN           = '\033[0;32m'
YELLOW          = '\033[0;33m'
BLUE            = '\033[0;34m'
MAGENTA         = '\033[0;35m'
CYAN            = '\033[0;36m'
WHITE           = '\033[0;37m'
GREY            = '\033[0;90m'
BRIGHT_RED      = '\033[0;91m'
BRIGHT_GREEN    = '\033[0;92m'
BRIGHT_YELLOW   = '\033[0;93m'
BRIGHT_BLUE     = '\033[0;94m'
BRIGHT_MAGENTA  = '\033[0;95m'
BRIGHT_CYAN     = '\033[0;96m'
BRIGHT_WHITE    = '\033[0;97m'

UNDRLN          = '\033[4m'
BOLD            = '\033[1m'
BLINK           = '\033[5m'

ENDC            = '\033[0m'

COLOUR_ARRAY=[
    ENDC,
    BLACK,
    RED,
    GREEN,
    YELLOW,
    BLUE,
    MAGENTA,
    CYAN,
    WHITE,
    GREY,
    BRIGHT_RED,
    BRIGHT_GREEN,
    BRIGHT_YELLOW,
    BRIGHT_BLUE,
    BRIGHT_MAGENTA,
    BRIGHT_CYAN,
    BRIGHT_WHITE,
    UNDRLN,
    BOLD,
    BLINK
]


def roll(roll_detail):
    roll_value = 0
    roll_count, roll_die = roll_detail.split("d")
    roll_count = int(roll_count)
    roll_die = int(roll_die)
    for _ in range(roll_count):
        roll_value += random.Random().randint(1,roll_die)
    return roll_value

def text_len(string):
    return len(raw_text(string))

def raw_text(string):
    processed_string = string
    for colour in COLOUR_ARRAY:
        processed_string= processed_string.replace(colour,"")
    return processed_string


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    def _chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
    return list(_chunks(lst, n))

def question(question_text: str,options: dict,):
    return options[0]