a,b,c = map(int, input().split())
maxi = 0

if a >= b and a >= c:
    maxi = a
elif c >= b:
    maxi = c
else:
    maxi = b

print(maxi)