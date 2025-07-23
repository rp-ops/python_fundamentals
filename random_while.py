import random

highest=10
randomno= random.randint(0,highest)

guess=0

print("Guess a number between 0 to {}".format(highest))

while guess != randomno:
    guess=int(input())
    if guess==0:
       break
    if guess==randomno:
        print("Congrats! You guessed it right")
        break
    elif guess> randomno:
        print("Guess Lower ")
    else:
        print("Guess Higher ")
        
    
    
