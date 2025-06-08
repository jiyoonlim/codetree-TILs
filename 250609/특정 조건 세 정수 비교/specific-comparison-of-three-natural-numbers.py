a,b,c = map(int, input().split())

if a<=b and a<=c :
    mini = a
elif b<=c :
    mini = b
else:
    mini = c

if a == mini:
    print(1, end=" ")
else:
    print(0, end=" ")


if a == b == c:
    print(1)
else:
    print(0)


