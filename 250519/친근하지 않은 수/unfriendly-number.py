n = int(input())
cnt = 0
while n>=1:
    if n%2==0 or n%3 == 0 or n%5 ==0:
        n -= 1
        continue
    else:
        cnt += 1
        n -= 1
        continue
    
print(cnt)