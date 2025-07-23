parrot="norwegian blue"

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3-14])
print(parrot[4-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])

print(parrot[0:9])
print(parrot[10:14])
print(parrot[:9])
print(parrot[10:])
print(parrot[:])

print(parrot[:10]+parrot[10:])

print(parrot[-14:-5])
print(parrot[-14:12])

print(parrot[-4:2])

print(parrot[0:9:3])
print(parrot[0::3])

numbers="1,233,456,789,908,899"
print(numbers[1::4])

numbers="1,233;564 789,908:899"
separators=numbers[1::4]
print(separators)

values=" ".join(char if char not in separators else " " for char in numbers).split
print([int(val) for val in values])


