ans = 25
mybool = True
while mybool:
    user_input = int(input())
    if user_input > 25:
        print("Lower")
    elif user_input < 25:
        print("Higher")
    else:
        print("Good")
        mybool=False