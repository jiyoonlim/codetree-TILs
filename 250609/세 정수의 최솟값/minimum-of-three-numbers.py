a,b,c = map(int, input().split())
minimum = 0
if a > b:
    if b > c:
        minimum = c
    elif c > a:
        minimum = b
    else:
        minimum = a

if b > a:
    if a > c:
        minimum = c
    elif c > b:
        minimum = a
    else:
        minimum = b

print(minimum)