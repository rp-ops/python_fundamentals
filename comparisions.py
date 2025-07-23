age=int(input("Enter your age: "))

# if age>=16 and age<=65:
#     print("Have a Good Day at office")

# if 16<=age<=65:
#     print("Have a Good Day at office")
# else:
#     print("Enjoy your free time")

# if age<16 or age>65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day in office")

if age in range(16,66):
    print("Have a good day in office")
else:
    print("Enjoy your free time")