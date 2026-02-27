# DO NOT modify or add any import statements
from support import *

# Name: Kung Tsz Fung
# Student Number: s4899606
# Favorite Marsupial: Koala
# -----------------------------------------------------------------------------

# Write your classes and functions here

available_numbers = ["1","2","3","4","5"]   #setting up the available number to test

def num_hours():
    """
    show the expected time I take to finish the assignment
    """
    return float (36)

def generate_initial_board (board_size: int) ->list[list[str]]:
    """
    generate rows with 5 empty_guess and 5 empty_feedback accoarding to the borad size input
    return the board
    """

    row = [EMPTY_GUESS]* 5 + [EMPTY_FEEDBACK]*5 
    board = []
    for x in range(board_size):                  #append the board size according to the input
        board.append(row[:]) 
    return board     

def display_board(board: list[list[str]]) -> None:
    """
    make the board visible to player by sepearte it into 2parts(guess and feedback)
    then print out using format string
    """

    for i, row in enumerate(board, 1):            #split the board into guess part(first 5) and feedback part(after 5)
        guess = " ".join(row[:5])
        feedback = " ".join(row[5:])
        if i<10:                                  #formating : as 10 cotains 2digits which will move the board by 1space
            print(str(i) +"  " + guess + " || || " + feedback)
        else:                                     #adding this part ensure the board remain consistence until 99rows
            print(str(i) +" " + guess + " || || " + feedback)
    print(BOARD_FOOTER)                                           

def display_key(key: list[str], used_hints: int)-> None:
    """
    The function to provide key to the player, 
    by checking the hints number and showing 1 key for 1 hint use
    print out the key to the user
    """

    display_key = []
    
    if used_hints > len(key):                      #to analyse how many keys to be shown 
        used_hints = len(key)
        
    for i in range(len(key)):                      #check the number of used_hints, showing 1 key for each hints,else show ? 
        if i < used_hints:
            display_key.append(key[i])
        else:
            display_key.append(HIDDEN_NUMBER)

    print("Key:", "  ".join(display_key))

def check_input(command: str) -> bool:
    """
    check the input for user with 3 expect situations and only return true when
    1. input is help/quit/hint command
    2. input has correct length
    3. input is in availalbe number
    else, return false with message
    """

    if command in HELP_COMMAND or command in QUIT_COMMAND or command in HINT_COMMAND:
        return True

    test = command.split(",")
    if len(test)!=5:                               #test it's length, if it's longer than 5, which means the format is wrong(5number only takes 5 spaces)
        print (INVALID_FORMAT_MESSAGE)
        return False
    
    for num in test:                               #check the input(after the length is right)
        if num not in available_numbers:
            print (INVALID_NUMBER_MESSAGE)
            return False
    return True


def get_command() -> str:
    """
    continue to get the user input and give feedback for different inputs,
    use check_input to filter out the wrong input(only True will be analyse)
    format it if the input is number
    return the letter if it is command
    """

    while True:
        command = input(ENTER_COMMAND_MESSAGE)
        
        if check_input(command) == True:           #use the check_input function to check the input,only evaluate the right input(True)

            if command in HELP_COMMAND or command in QUIT_COMMAND or command in HINT_COMMAND: #if the input is in command, return the letter
                return command

            else:                                  #if the input is number, formating it 
                user_guess = ''
                for x in command:
                    if x in available_numbers:
                        user_guess = user_guess + "[" + x + "]"
                    elif x == ",":
                        user_guess = user_guess +','
                return user_guess

def place_guess(board: list[list[str]], guess: str, row: int)-> None:
    """
    to format the input from strings into a list, and place it into the board
    """
    
    guess_list = guess.split(",")
    board[row][:5] = guess_list



def place_feedback(board: list[list[str]],\
                   feedback: list[str], row: int)-> None:
    """
    to place the feedback into the board
    """

    for i in range(len(feedback)):               #place it to the board, 5 is the point where feedback start
        board[row][5+i] = feedback[i]

def provide_feedback(key: list[str], guess: str)-> list[str]:
    """
    check the guess with key one by one, add B(same order same number) and W(same number) to the feedback
    and return it as a list
    """

    guess = guess.split(',')
    feedback = []
    not_use =[]
    new_guess=[]

    for i in range(len(key)):                    #check the guess with key (same number and order)
        if key[i] == guess[i]:
            feedback.append(BLACK)
        else:                                    #put the not checked key and guess to the new list for later use
            not_use +=((key[i]),)
            new_guess.append(guess[i])
   
    for i in range(len(new_guess)):              #check the guess with key (only for same number),remove the checked key after
        if new_guess[i] in not_use:
            feedback.append(WHITE)
            not_use.remove(new_guess[i])
    return feedback

def play_game() -> None:                         #starting the game with preset board and key
    """
    The main function of the program and let the player play the game. The function contains 4steps.
    1. Print the initial board to the player
    2. Prompt the user to input continuously
    3. Evaluate the input and provide feedback accordingly
    4. Check the winning/losing condition
    """

    board = generate_initial_board (10)      
    key = generate_key()                                
    hint_used = 0
    attempts = 0

    print("Welcome to Mastermind!")     
    display_key(key, hint_used)                  #display the orignal board to player    
    display_board(board)                                   
    
    while True:                                  #use while loop to prompt user's input
        
        command = get_command()                  #use get_command to check the user input
        
        if command in HELP_COMMAND:              #print the help message if the input is h/H
            print(HELP_MESSAGE)
                
        elif command in QUIT_COMMAND:                       
            break                                       
                
        elif command in HINT_COMMAND:           #to give hints with the input t/T, check still have hints and after 3attempts 
            if hint_used >=3:                                
                print(HINT_MESSAGE)                         
            elif attempts >=3:                              
                hint_used += 1
                display_key(key, hint_used)                 
            else:
                print(HINT_EARLY_MESSAGE)                   

        else:                                   #progress the game by placing guess and giving feedback, showing board and key everytime player enter guesses
            place_guess(board, command, attempts)           
            feedback = provide_feedback(key, command)       
            place_feedback(board, feedback, attempts)       

            display_key(key, hint_used)
            display_board(board)
            
            if feedback == [BLACK] * 5:         #determind if the player is win before 10attempts
                print(WIN_MESSAGE)                                                 
                break
                    
            attempts += 1                     
            
            if attempts == 10:                 #if the player finish 10 attempts and still do not get the true answer, they will lose the game
                print(LOST_MESSAGE + f" The key was: {' '.join(key)}")     
                break
                    
    
def main() -> None:          #this is the function to run the game automatically and print the welcome message before start
    """
    The function for starting the game while opened
    Ask player for the retry if the game ended.
    """
    
    play_game()
    
    while True:
        retry = input(RETRY_MESSAGE)
        if retry in "Yy":
            play_game()
        else:
            return 


if __name__ == "__main__":
    main()

