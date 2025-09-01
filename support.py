from random import choices, seed

seed(7030)
NUM_NUMBERS = 5
MAX_NUMBER = 5

WHITE = 'W'
BLACK = 'B'

HIDDEN_NUMBER = '?'
EMPTY_GUESS = '___' 
EMPTY_FEEDBACK = '_'
BOARD_HALVES_SEP = ' || || '
BOARD_FOOTER = '         Guesses              Feedback'

HELP_COMMAND = ["h", "H"]
QUIT_COMMAND = ["q", "Q"]
HINT_COMMAND = ["t", "T"]

ENTER_COMMAND_MESSAGE = "Please enter your guess (h to see valid format): "

HELP_MESSAGE = """Valid commands: 
- Provide 5 numbers seperated by comma (,)
Available_numbers: 1,2,3,4,5
- t/T: Get a hint
- h/H: Display help text
- q/Q: Quit current game\n"""

INVALID_NUMBER_MESSAGE = f"\nInvalid number! Available numbers: 1,2,3,4,5\n"
INVALID_FORMAT_MESSAGE = "\nInvalid command. Enter 'h' for valid command format or 'q' to quit\n"

WIN_MESSAGE = "\nCongratulations! You guessed the key!"
RETRY_MESSAGE = "\n Would you like to retry? "
LOST_MESSAGE = "\nSorry, you've lost the game."
HINT_MESSAGE = "\nSorry, you've used all hints."
HINT_EARLY_MESSAGE = "\nYou can get hint after attempting 3 guesses!"

def generate_key() -> list[str]:
    """
    Generates a random 5-number secret key from the available numbers.
    
    Returns:
        (list[str]): The generated secret key. 
    """
    numbers = []
    for num in range(MAX_NUMBER):
        numbers.append(f"[{num+1}]")
    
    key = choices(numbers, k = MAX_NUMBER)
    return key