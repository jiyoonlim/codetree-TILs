a,b,c = map(int, input().split())
middle = 0
if a > b:
    if b > c:
        middle = b
    elif c > a:
        middle = a
    else:
        middle = c

if b > a:
    if a > c:
        middle = a
    elif c > b:
        middle = b
    else:
        middle = c


print(middle)
