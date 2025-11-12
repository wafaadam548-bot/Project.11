import random
import colorama
from colorama import Fore, Style
colorama.init()
print(Fore.BLACK+"Hellooo in Guess the Number Game!")
while True:
    num = random.randint(1, 10)
    while True:
        num1 = int(input(Fore.CYAN +"Enter a number between 1 and 10: "))

        differences = abs(num - num1)

        if differences == 0:
            print(Fore.LIGHTYELLOW_EX+"🎉 Yaaaa!!!! You're the winner!")
            break 

        elif differences <= 5:
            print(Fore.LIGHTRED_EX+"🔥 You are close!")
        elif differences < 10:  
            print(Fore.LIGHTBLUE_EX+"😐 So far, think again!") 
        else:
            print(Fore.LIGHTWHITE_EX+"❄️ You are very far, think again!")   
            

    if num==num1:        
        response = input(Fore.BLACK+"Do you want to start again? (yes or no): ") 
        if response.lower() == "yes" :
            continue
        else:
            print(Fore.MAGENTA+"👋 Thanks for playing! Goodbye!")
            break 

            
                
        