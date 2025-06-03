a,b,c = map(int, input().split())

if a > b:
    if b > c:
        print(a)
    if c > a:
        print(c)
else:
    if a > c:
        print(b)
    if c > b:
        print(c)