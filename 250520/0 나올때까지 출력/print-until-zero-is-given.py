mybool = True
mylist = []
while mybool:
    user_input = int(input())
    if user_input != 0:
        mylist.append(user_input)
    else:
        mybool = False

for i in range(len(mylist)):
    print(mylist[i])
        
