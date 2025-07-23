for i in range(1, 13):
    print("The number {0:2} is {1:4} squared and {2:4} cubed".format(i,i**2,i**3))
    
print()

for i in range(1,13):
    print("The number {0:<2} is {1:<3} squared and {2:<4} cubed".format(i,i**2,i**3))
    
print()

for i in range(1,13):
    print("The number {0:>2} is {1:>3} squared and {2:>4} cubed".format(i,i**2,i**3))
    
print()

for i in range(1,13):
    print("The number {0:>2} is {1:>3} squared and {2:^4} cubed".format(i,i**2,i**3))
    
print()

for i in range(1,13):
    print("The number {} is {} squared and {:^4} cubed".format(i,i**2,i**3))
    
print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))



