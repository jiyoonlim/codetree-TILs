a,b = map( int, input().split())
mysum =0

for i in range(a,b+1):
    if i%2 == 0:
        mysum += i
print(mysum)