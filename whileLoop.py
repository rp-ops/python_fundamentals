# for i in range(10):
#     print(i)


# i=0
# while i<11:
#     print("value of i is now {}".format(i))
# i+=1


# directions=["north","south","east","west"]
# exit_direction=""

# while exit_direction not in directions:
#     exit_direction=input("Enter the exit_direction")
    
# print("Aren't you glad you got out of it")


# available_exits = ["north", "south", "east", "west"]

# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game over")
#         break

# print("aren't you glad you got out of there")

available_exits=["North", "South", "East", "West"]
chosen_exit=""

while chosen_exit not in available_exits:
    chosen_exit=input("Enter your chosen exit: ")
    if chosen_exit.casefold()=="quit":
        print("Game Over")
        break
    
print("Aren't you glad got out of there")





