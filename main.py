import random

print("Hellooo in Guess the Number Game!")
while True:
    num = random.randint(1, 10)
    while True:
        num1 = int(input("Enter a number between 1 and 10: "))

        differences = abs(num - num1)

        if differences == 0:
            print("🎉 Yaaaa!!!! You're the winner!")
            break 

        elif differences <= 5:
            print("🔥 You are close!")
        elif differences < 10:  
            print("😐 So far, think again!") 
        else:
            print("❄️ You are very far, think again!")   
            

    if num==num1:        
        response = input("Do you want to start again? (yes or no): ") 
        if response.lower() == "yes" :
            continue
        else:
            print("👋 Thanks for playing! Goodbye!")
            break 

            
                
        