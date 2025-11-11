while True:
    print("==================================="
    "------------------------------------")
    print("Welcome to the games worls!!")
    print(" Please Choose What you want to Play")
    print("1. X,O (TIC TAC TOE )")
    print("2. Guess The number")
    choise=input("Enter Your choise(1,2) : ")
    if choise=="1":
        import XO
    elif choise=="2":
        import Guess  
    else:
        print("Sorry, make sure you follow the steps and write with the same letters and spelling.")            
    print("Please Press Enter to Exit the page")
    again = input("Do you want to PLay again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for Playing Game world!") 
        break
