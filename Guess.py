import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print("\n" + Fore.YELLOW + "🎉 Welcome to Guess The Number Game!")
print(Fore.GREEN  + "Try to guess the secret number!")
print("-" * 50 + "\n")

while True:
    num = random.randint(1, 10)

    while True:
        user_input = input(Fore.CYAN + "\n👉 Enter a number between 1 and 10: ")

        if not user_input.isdigit():
            print(Fore.RED + "❌ Please enter numbers only!")
            continue

        num1 = int(user_input)
        differences = abs(num - num1)

        print()

        if differences == 0:
            print(Fore.LIGHTYELLOW_EX + "🎉 Yaaaa!!!! You're the winner!")
            print("-" * 50)
            break 

        elif differences <= 2:
            print(Fore.LIGHTRED_EX + "🔥 Very close!")
        elif differences <= 5:  
            print(Fore.LIGHTBLUE_EX + "🙂 Close!")
        else:
            print(Fore.WHITE + "❄️ Far, try again!")   

    print("\n" + "-" * 50)
    response = input(Fore.MAGENTA + "🔁 Do you want to play again? (yes/no): ")

    if response.lower() != "yes":
        print("\n" + Fore.GREEN + "👋 Thanks for playing! Goodbye!")
        print("-" * 50)
        break
