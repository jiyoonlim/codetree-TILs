n = int(input())
mysum = 0

for i in range(1,100):
    mysum += i
    if mysum >= n:
        print(i)
        break