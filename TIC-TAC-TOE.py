#Two Player Tic-Tac-Toe .

''' Build tic tac toe table using dictionary, key 1-9 will be the locations a player's input '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' To print updated tic tac toe board after a player makes a move '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#fucntion to play the game 


def game():
    
    turn = 'X'
    numOfMoves = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if int(move) > 9 or int(move) < 1:
            print("invalid input. please enter a value between 1-9")
            continue

        if theBoard[move] == ' ':
            theBoard[move] = turn
            numOfMoves = numOfMoves + 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # Top horizontal 
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")                
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # Middle horizontal
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # Bottom Horizontal
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # Left Vertical
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # Middle Vertical
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # Right Vertical
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # Diagonal
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # Diagonal
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print(" ** " +turn + " won. **")
            break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'Cat Game'.
        if numOfMoves == 9:
            print("\nGame Over.\n")                
            print("CAT Game")

        # Switch player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        

if __name__ == "__main__":
    game()