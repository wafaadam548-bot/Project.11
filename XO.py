import random
from colorama import Fore, Style, init
init(autoreset=True)

#   GAME SETTINGS
board = ["-"] * 9
current_player = "X"
player_colors = {"X": Fore.GREEN, "O": Fore.LIGHTWHITE_EX}
empty_color = Fore.WHITE
winner = None
game_running = True


#     BEAUTIFUL BOARD
def printBoard():
    def colored(cell):
        if cell == "X":
            return player_colors["X"] + "X" + Style.RESET_ALL
        elif cell == "O":
            return player_colors["O"] + "O" + Style.RESET_ALL
        else:
            return empty_color + "-" + Style.RESET_ALL

    print("\n" + Fore.MAGENTA + "      ✦ TIC TAC TOE ✦")
    print(Fore.YELLOW + "   -------------------------")
    print(Fore.CYAN   + "        1 | 2 | 3")
    print(Fore.YELLOW + "   -------------------------")
    print("        " + colored(board[0]) + " | " + colored(board[1]) + " | " + colored(board[2]))
    print(Fore.YELLOW + "   -------------------------")
    print(Fore.CYAN   + "        4 | 5 | 6")
    print(Fore.YELLOW + "   -------------------------")
    print("        " + colored(board[3]) + " | " + colored(board[4]) + " | " + colored(board[5]))
    print(Fore.YELLOW + "   -------------------------")
    print(Fore.CYAN   + "        7 | 8 | 9")
    print(Fore.YELLOW + "   -------------------------")
    print("        " + colored(board[6]) + " | " + colored(board[7]) + " | " + colored(board[8]) + "\n")


#        PLAYER MOVE
def playerInput():
    global board
    try:
        num = int(input(Fore.CYAN + "➡ Choose a spot (1–9): "))
    except ValueError:
        print(Fore.RED + "❌ Numbers only!")
        return

    if 1 <= num <= 9 and board[num-1] == "-":
        board[num-1] = current_player
    else:
        print(Fore.RED + "❌ Invalid or taken spot, try again!")

#   COMPUTER MOVE
def computerMove():
    empties = [i for i, v in enumerate(board) if v == "-"]
    if empties:
        pos = random.choice(empties)
        board[pos] = "O"
        print(Fore.LIGHTBLUE_EX + "🤖 Computer chose a spot!")


#        WIN CHECKS
def checkHorizontal():
    global winner
    combos = [(0,1,2),(3,4,5),(6,7,8)]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] and board[a] != "-":
            winner = board[a]
            return True
    return False

def checkVertical():
    global winner
    combos = [(0,3,6),(1,4,7),(2,5,8)]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] and board[a] != "-":
            winner = board[a]
            return True
    return False

def checkDiagonal():
    global winner
    combos = [(0,4,8),(2,4,6)]
    for a,b,c in combos:
        if board[a] == board[b] == board[c] and board[a] != "-":
            winner = board[a]
            return True
    return False

def checkTie():
    if "-" not in board and winner is None:
        print(Fore.LIGHTRED_EX + "🤝 It's a tie!")
        return True
    return False

def checkWin():
    if checkHorizontal() or checkVertical() or checkDiagonal():
        print(Fore.LIGHTYELLOW_EX + f"🏆 The winner is {winner}! 🎉")
        return True
    return False


#       SWITCH PLAYER
def switchPlayer():
    global current_player
    current_player = "O" if current_player == "X" else "X"


print(Fore.GREEN + "✨ Welcome to the Beautiful Tic Tac Toe Game! ✨\n")

while True:
    board = ["-"] * 9
    current_player = "X"
    winner = None
    game_running = True

    # GAME START
    while game_running:
        printBoard()

        if current_player == "X":
            playerInput()
        else:
            computerMove()

        if checkWin() or checkTie():
            game_running = False
        else:
            switchPlayer()

    printBoard()

    again = input(Fore.MAGENTA + "🔄 Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print(Fore.GREEN + "👋 Thanks for playing! Goodbye!")
        break
