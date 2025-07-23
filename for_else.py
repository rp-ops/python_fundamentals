numbers=[7,12,34,67,89]

for num in numbers:
    if num%8==0:
        #reject the list
        print("Numbers are unacceptable")
        break
    
else:
    print("The Numbers are fine")