# activity = input("What would you like to do? ")

# if "cinema" not in activity.casefold():
#     print("But I want to go to the Cinemas")


parrot="norwegian blue"

substr=input("Enter any string: ")

if substr in parrot:
    print("The substring {} is present in the word {}".format(substr,parrot))
else:
    print("This {} is not required".format(substr))