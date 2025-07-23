low=0
high=1000

print("Think of a number between {} and {}".format(low,high))
input("Press ENTER to start")

guesses=0

while True:
    guess=low+(high-low)//2
    print("My guess is between {} and {}".format(low,high))
    hi_lo=input("My guess is {}.Please enter h if i need to guess higher," 
          "l if i need to guess lower and c if i guessed correctly".
          format(guess))
    
    if hi_lo=="h":
        low=guess+1
    elif hi_lo=="l":
        high=guess-1
    elif hi_lo=="c":
        print("I guessed it right in {} guesses".format(guesses))
        break
    else:
        print("Please enter a valid input h,l,c")
        
        
    guesses=guesses+1
        
    