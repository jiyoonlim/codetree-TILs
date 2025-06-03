y = int(input())
if y % 4 == 0:
    # 윤년
    print("true")
    if y % 100 == 0 and y % 400 != 0:
        print("false")
else:
    # 평년
    print("fasle")
