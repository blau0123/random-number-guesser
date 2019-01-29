import random


def draw_board(board):
    # This function prints out the board that it was passed and should not return anything
    # HINT: pass a list to this function that holds the position of 'X's and 'O's
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    for x in range(3):
        print("---", end="")
    print("\n" + board[3] + ' | ' + board[4] + ' | ' + board[5])
    for x in range(3):
        print("---", end="")
    print("\n" + board[0] + ' | ' + board[1] + ' | ' + board[2])
    return


def input_player_letter():
    # Ask the player if they want to be 'X' or 'O'
    # Return the chosen letter
    # Hint: Use a loop to keep prompting the player for a letter if the input is not valid
    tick = input("Choose 'X' or 'O' for da game yeet: ")
    while tick != 'X' and tick != 'O':
        tick = input("Choose 'X' or 'O' for da game yeet: ")

    return tick


def who_goes_first():
    # Randomly choose who goes first
    # Return the string 'computer' or 'player'
    # HINT: look up the documentation for the 'random' library
    who_first = random.randint(0, 2)
    if who_first == 0:
        return 'computer'
    else:
        return 'player'


def main():

    print('Welcome to Tic Tac Toe')
    starter = who_goes_first()

    player_letter = input_player_letter()
    computer_letter = 'X'
    # Here assign computer_letter to be 'O' if player_letter is 'X' or vice versa
    if player_letter == 'O':
        computer_letter = 'X'
    else:
        computer_letter = 'O'

    # initialize your board list here to pass to draw the board
    board = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    draw_board(board)


main()
