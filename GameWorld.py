import colorama
from colorama import Fore, Style
colorama.init()

while True:
    print(Fore.WHITE + Style.BRIGHT + "===================================")
    print(Fore.WHITE + Style.BRIGHT + "------------------------------------")
    print(Fore.YELLOW + Style.BRIGHT + "🎮 Welcome to the Games World!! 🎮")
    print(Fore.CYAN + "Please Choose What you want to Play")
    print(Fore.YELLOW + "1. X,O (TIC TAC TOE)")
    print(Fore.YELLOW + "2. Guess The Number")

    choice =int( input(Fore.LIGHTWHITE_EX + "\nEnter Your Choice (1,2): ")).strip()

    if choice == "1":
        import XO
    elif choice == "2":
        import Guess  
    else:
        print(Fore.RED + "❌ Sorry, make sure you write correctly.")

    print(Fore.CYAN + "\nPlease Press Enter to Exit the page")
    again = input(Fore.LIGHTMAGENTA_EX + "Do you want to play again? (yes/no): ").strip().lower()

    if again != "yes":
        print(Fore.BLACK + "💖 Thank you for playing Game World! 💖") 
        break
