# parrot="norwegian blue"

# for character in parrot:
#     print(character)


# numbers="1,234:456;678 908%567"
# separators=""

numbers=input("Enter a number with any separator you like: ")
separators="" #in order to use the variable we first have to define it and bind a value to it

for char in numbers:
    if not char.isnumeric():
        separators=separators+char
        
print(separators)