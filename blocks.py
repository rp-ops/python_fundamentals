# for i in range(1,13):
#     print("No. {} squared is {} and cubed is {:4}".format(i,i**2,i**3))
# print("*"*80)

name=input("Please Enter your Name: ")
age=int(input("What is your age,{0} ?".format(name)))
print(age)

# if age>=18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18-age))
    
# if(age<18):
#     print("Please come back in {0} years".format(18-age))
# else:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
    
if(age<18):
    print("Please come back in {0} years".format(18-age))
elif age==900:
    print("Sorry,Yoda,You Die In The return Of Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")