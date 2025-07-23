day="Friday"
temperature=28
raining=False

# if day=="Saturday" and temperature>27 and not raining:
#     print("Go Swimming")
# else:
#     print("Learn Python")

if day=="Saturday" and temperature > 27 or not raining:  #and operator precedence is greater than or
    print("Go Swimming")
else:
    print("Learn Python")
    
    