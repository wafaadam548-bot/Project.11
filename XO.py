import random
from colorama import Fore, Style, init
init(autoreset=True)

board = ["-"] * 9
current_player = "X"
player_colors = {"X": Fore.GREEN, "O": Fore.LIGHTWHITE_EX}
empty_color = Fore.WHITE
winner = None
game_running = True

def printBoard():
    def colored(cell):
        if cell == "X":
            return player_colors["X"] + "X" + Style.RESET_ALL
        elif cell == "O":
            return player_colors["O"] + "O" + Style.RESET_ALL
        else:
            return empty_color + "-" + Style.RESET_ALL
    print(colored(board[0]) + "|" + colored(board[1]) + "|" + colored(board[2]))
    print("________")
    print(colored(board[3]) + "|" + colored(board[4]) + "|" + colored(board[5]))
    print("________")
    print(colored(board[6]) + "|" + colored(board[7]) + "|" + colored(board[8]))

def playerInput():
    global board, current_player
    try:
        num = int(input(Fore.CYAN + "Enter a number between 1 and 9: "))
    except ValueError:
        print(Fore.LIGHTRED_EX + "Please enter a valid number.")
        return
    if 1 <= num <= 9 and board[num-1] == "-":
        board[num-1] = current_player
    else:
        print(Fore.LIGHTRED_EX + "Oops! That spot is taken or invalid.")

def checkHorizontal():
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]; return True
    if board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]; return True
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]; return True
    return False

def checkVertical():
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]; return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]; return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]; return True
    return False

def checkDiagonal():
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]; return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]; return True
    return False

def checkTie():
    global game_running
    if "-" not in board and winner is None:
        printBoard()
        print(Fore.LIGHTRED_EX + "It is a tie!")
        game_running = False

def checkWin():
    global game_running
    if checkHorizontal() or checkDiagonal() or checkVertical():
        print(Fore.LIGHTYELLOW_EX + f"The winner is {winner} 🎉🎉")
        game_running = False

def switchPlayer():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def computerMove():
    empties = [i for i, v in enumerate(board) if v == "-"]
    if not empties:
        return
    pos = random.choice(empties)
    board[pos] = "O"

while game_running:
    printBoard()
    if current_player == "X":
        playerInput()
    else:
        computerMove()
    checkWin()
    checkTie()
    if not game_running:
        break
    switchPlayer()
printBoard()
