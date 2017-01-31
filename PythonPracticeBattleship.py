# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:18:05 2017

@author: btilley
"""
# This is some fun code that I wrote while learning Python with Codeacademy.
# This makes a Battleship game that involves a user and their inputted guesses.

from random import randint

# Create the game board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

# Generate random integers for the row and column where the battleship hides.
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

# For loop to prompt user for 5 guess to sink the battleship.
for turn in range(4):
    print(turn), 
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            if turn == 3:
                print("Game Over")
                board[guess_row][guess_col] = "X"
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
    print(turn + 1)
print_board(board)
