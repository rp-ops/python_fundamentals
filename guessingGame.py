answer=34

print("Guess a number between 1 to 50:")
guess=int(input())

# if guess<answer:
#     print("Guess Higher")
#     guess1=int(input())
#     if guess1==answer:
#         print("You guessed it right")
#     else:
#         print("Your guess is wrong")
        
# elif guess>answer:
#     print("Guess Lower")
#     guess1=int(input())
#     if guess1==answer:
#         print("You guessed it right")
#     else:
#         print("Your guess is wrong")
        
# else:
#     print("Got it the first time")

# if guess!=answer:
#     if(guess<answer):
#         print("Guess Higher")
#     else:                     
#         print("Guess Lower")   #guess must be higher than answer
#     guess=int(input())
#     if guess==answer:
#         print("You guessed it right")
#     else:
#         print("Sorry,wrong guess")
            
# else:
#     print("You guessed it right")

if guess==answer:
    print("You guessed it right in first go")

elif guess<answer:
    print("Please Guess Higher")
    guess=int(input())
    if(guess==answer):
        print("You guessed it right")
    else:
        print("Sorry,Wrong Guess")
        
else:
    print("Please Guess Lower")
    guess=int(input())
    if(guess==answer):
        print("You guessed it right")
    else:
        print("Sorry,Wrong guess")
    