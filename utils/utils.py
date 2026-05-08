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

BLACK_BG           = '\033[0;40m'
RED_BG             = '\033[0;41m'
GREEN_BG           = '\033[0;42m'
YELLOW_BG          = '\033[0;43m'
BLUE_BG            = '\033[0;44m'
MAGENTA_BG         = '\033[0;45m'
CYAN_BG            = '\033[0;46m'
WHITE_BG           = '\033[0;47m'
GREY_BG            = '\033[0;100m'
BRIGHT_RED_BG      = '\033[0;101m'
BRIGHT_GREEN_BG    = '\033[0;102m'
BRIGHT_YELLOW_BG   = '\033[0;103m'
BRIGHT_BLUE_BG     = '\033[0;104m'
BRIGHT_MAGENTA_BG  = '\033[0;105m'
BRIGHT_CYAN_BG     = '\033[0;106m'
BRIGHT_WHITE_BG    = '\033[0;107m'

BG_FROM_COLOUR ={
BLACK           :BLACK_BG         ,      
RED             :RED_BG           ,  
GREEN           :GREEN_BG         ,  
YELLOW          :YELLOW_BG        ,  
BLUE            :BLUE_BG          ,  
MAGENTA         :MAGENTA_BG       ,  
CYAN            :CYAN_BG          ,  
WHITE           :WHITE_BG         ,  
GREY            :GREY_BG          ,  
BRIGHT_RED      :BRIGHT_RED_BG    ,  
BRIGHT_GREEN    :BRIGHT_GREEN_BG  ,  
BRIGHT_YELLOW   :BRIGHT_YELLOW_BG ,  
BRIGHT_BLUE     :BRIGHT_BLUE_BG   ,  
BRIGHT_MAGENTA  :BRIGHT_MAGENTA_BG,  
BRIGHT_CYAN     :BRIGHT_CYAN_BG   ,  
BRIGHT_WHITE    :BRIGHT_WHITE_BG  ,  
}



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
    BLINK,
    BLACK_BG         ,
    RED_BG           ,
    GREEN_BG         ,
    YELLOW_BG        ,
    BLUE_BG          ,
    MAGENTA_BG       ,
    CYAN_BG          ,
    WHITE_BG         ,
    GREY_BG          ,
    BRIGHT_RED_BG    ,
    BRIGHT_GREEN_BG  ,
    BRIGHT_YELLOW_BG ,
    BRIGHT_BLUE_BG   ,
    BRIGHT_MAGENTA_BG,
    BRIGHT_CYAN_BG   ,
    BRIGHT_WHITE_BG  ,
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
