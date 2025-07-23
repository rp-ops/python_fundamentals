import random

highest=20

randomNumber = random.randint(0,highest)

guess=int(input("Enter your guess"))
 
if guess==randomNumber:
    print("Congrats guessed it in first go")
    
else:
    if guess < randomNumber:
        print("Please guess higher")
        guess=input("Enter your guess again")
        if guess==randomNumber:
            print("You guessed it right")
        else:
            print("Sorry! Wrong guess")
            
    else:
        print("Please guess Lower")
        guess=input("Enter your guess again")
        if guess==randomNumber:
            print("You guessed it right")
        else:
            print("Sorry! Wrong guess")
            