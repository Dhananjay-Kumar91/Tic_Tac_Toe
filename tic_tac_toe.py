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
