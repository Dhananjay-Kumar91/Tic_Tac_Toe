##########################################################################################################
#Function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with #
#a number on a number pad, so you get a 3 by 3 board representation.                                     #
##########################################################################################################

def display_board(board):
    '''
    Input: "board" is a list of 10 elements
    output: Print "board" in a 5x5 Tic Tac Toe board

    '''
    # Clear the screen on each call before printing new board

    print('\n'*200)

    print(" "+board[7]+"|"+board[8]+"|"+board[9]+" ")
    print(" -----  ")
    print(" "+board[4]+"|"+board[5]+"|"+board[6]+" ")
    print(" -----  ")
    print(" "+board[1]+"|"+board[2]+"|"+board[3]+" ")

    # using mutiple print statement for readability,can be printed in a single print command using "\n"


##########################################################################################################
#Function that can take in a player input and assign their marker as 'X' or 'O'. Think about using while #
#loops to continually ask until you get a correct answer.                                                #
##########################################################################################################

def player_input():
    '''

    Input: ask for User input for marker selection 'X' or 'O'
    output: Return player1 marker and player2 marker

    '''
    marker = ""

    while not (marker == 'X' or marker == "O"):

        marker = input(" Player 1 Please pick a marker 'X' or 'O': ").upper()

    if marker == 'X':

        return 'X', 'O'

    else:

        return 'O', 'X'

##########################################################################################################
#Function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9)#
# and assigns it to the board.                                                                           #
##########################################################################################################


def place_marker(board, marker, position):
    '''
    Input: board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
    Output: None

    '''

    board[position] = marker

##########################################################################################################
#Function that takes in a board and a mark (X or O) and then checks to see if that mark has won.         #
#                                                                                                        #
##########################################################################################################

def win_check(board, mark):
    '''
    Input: board and a marker
    Output: Check the board for win condition of 3 markers in a series and return Boolean True or False
    
    '''
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # Top Row Match
    (board[7] == mark and board[8] == mark and board[9] == mark) or #Middle Row Match
    (board[7] == mark and board[8] == mark and board[9] == mark) or # Botton row Match
    (board[7] == mark and board[4] == mark and board[1] == mark) or #1st Left Column
    (board[8] == mark and board[5] == mark and board[2] == mark) or #Middle Column
    (board[9] == mark and board[6] == mark and board[3] == mark) or #Right Column
    (board[7] == mark and board[5] == mark and board[3] == mark) or #Right Diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) #Left Diagonal
    

##########################################################################################################
#Function that uses the random module to randomly decide which player goes first. You may want to lookup #
#random.randint() Return a string of which player went first.                                            #
##########################################################################################################

import random

def choose_first():
    '''
    Randomly select which player goes first
    
    '''
    
    if (random.randint(0,1) == 0):
        return 'Player 2'
    else:
        return 'Player 1'


##########################################################################################################
#Function that returns a boolean indicating whether a space on the board is freely available.            #
#                                                                                                        #
##########################################################################################################

def space_check(board, position):
    
    '''
    Input: takes argument as board aand a position on the board
    Output: Returns True if the the position is free on the board else returns error
    
    '''
    return (board[position] == ' ')


##########################################################################################################
#Function that checks if the board is full and returns a boolean value. True if full, False otherwise.   #
#                                                                                                        #
##########################################################################################################

def full_board_check(board):
    '''
    Input: Takes in board as input
    output: Returns Boolean True if the board is full else false
    
    '''
    
    for i in range(1,10):
        
        if space_check(board,i):
            
            return False
        
    return True


##########################################################################################################
#Function that asks for a player's next position (as a number 1-9) and then uses the function from step 6#
#to check if it's a free position. If it is, then return the position for later use.                     #
##########################################################################################################

def player_choice(board):
    '''
    
    Input: Takes Board as input
    output: returns position if the entered position is free
    
    '''
    position = 0
    count = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        
        if count < 1:
            
            position = int(input("Choose your next position: (1-9): "))
            count += 1
        else:
            position = int(input("Entered Position out of range or Position already occupied \nChoose your next position: (1-9): "))
            count += 1
    return position



##########################################################################################################
#Function that asks the player if they want to play again and returns a boolean True if they do want to  #
#play again.                                                                                             #
##########################################################################################################

def replay():
    '''
    
    asks the player if they want to play again and returns a boolean True if they do want to play again
    
    '''
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

    