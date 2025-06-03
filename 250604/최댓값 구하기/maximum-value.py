a,b,c = map(int, input().split())

if a > b:
    if b > c:
        print(a)
    elif c > a:
        print(c)
    else:
        print(a)
elif b > a:
    if a > c:
        print(b)
    elif c > b:
        print(c)
    else:
        print(b)