name=input("Please Enter your Name:")
age=int(input("Please Enter your age:"))

if 18<=age<=30:
    print("Welcome to the 18-30 party,{}".format(name))
else:
    print("You are not allowed in the party")