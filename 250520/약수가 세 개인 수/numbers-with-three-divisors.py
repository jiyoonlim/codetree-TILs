start, end = map(int, input().split())

count = 0

# Please write your code here.
for i in range(start,end+1):
    divisor_count = 0
    for j in range(1, i+1):
        if i%j == 0:
            divisor_count += 1
    if divisor_count == 3:
        count += 1


print(count)