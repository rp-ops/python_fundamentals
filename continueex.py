grocery=["eggs","bread","sauce","jam","spam","pizza"]

# for item in grocery:
#     if item != "spam":
#         print("Buy {}".format(item))

for item in grocery:
    if item=="spam":
        continue
    
    print("Buy {}".format(item))