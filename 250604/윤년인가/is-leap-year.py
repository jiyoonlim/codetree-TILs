y = int(input())
if y % 4 == 0:
    if y % 100 == 0 and y % 400 != 0:
        print("false")
    # 윤년
    else:
        print("true")

else:
    # 평년
    print("false")
