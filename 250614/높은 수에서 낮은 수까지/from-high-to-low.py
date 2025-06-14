a,b = map(int, input().split())

if a > b:
    while a>=b:
        print(a, end=" ")
        a -= 1
else:
    while b>=a:
        print(b, end=" ")
        b -= 1
