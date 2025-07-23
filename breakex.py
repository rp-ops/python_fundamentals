grocerylist=["sauce","rice","bread","jam","eggs","spam"]

find_item="albatross"
found_at= None

# for item in grocerylist:
#     if item==find_item:
#        found_at=grocerylist.index(item)


# print("Item found at:{}".format(found_at))


for index in range(len(grocerylist)):
    if grocerylist[index]==find_item:
        found_at=index
        break

if found_at is not None:
    print("Item found at {}".format(found_at))
else:
    print("Item not found")



    
       

        