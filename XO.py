import random
import colorama
from colorama import Fore, Style
colorama.init()
board=[Fore.BLACK+"-","-","-",
        "-","-","-",
        "-","-","-"]

cerrentplayer=Fore.GREEN+"X"
winner="noun"        
gamingRuning=True
def printBoard(board):
    print(board[0]+"|",board[1]+"|",board[2]+"|")
    print("________")
    print(board[3]+"|",board[4]+"|",board[5]+"|")
    print("________")
    print(board[6]+"|",board[7]+"|",board[8]+"|")
def playerInput(board):
    num= int (input(Fore.BLUE+"ENter a number between 1 to 9: "))
    if num>=1 and num<=9 and board[num-1]=="-":
        board[num-1]=cerrentplayer
    else:
        print(Fore.LIGHTRED_EX+"Oops Player is already in that spot !")    

def checkHorezantal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[2]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner=board[6]
def checkRaw(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner= board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner=board[2]
        return True
def checkDiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True 
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner=board[2]
        return True   
def checkTie(board):
    global gamingRuning
    if "-" not in board:
        printBoard(board)
        print(Fore.LIGHTRED_EX+"It is Tie! ")        
        gamingRuning=False
def checkWin():
    global gamingRuning
    if checkHorezantal(board)or checkDiag(board) or checkRaw(board):
        print(Fore.LIGHTYELLOW_EX +f"The winner is {winner}🎉🎉")     
        gamingRuning=False   
def switchPlayer():
    global cerrentplayer
    if cerrentplayer=="X":
        cerrentplayer=Fore.LIGHTWHITE_EX+"O"
    else:
        cerrentplayer="X"    
def computer(board):
    while cerrentplayer==Fore.LIGHTWHITE_EX+"O":
        position=random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchPlayer()


while gamingRuning:
    printBoard(board)
    playerInput(board)         
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
