a,b = map(int, input().split())

if a > 0:
    while b>0:
        print(a, end="")
        b -= 1
else:
    print(0)