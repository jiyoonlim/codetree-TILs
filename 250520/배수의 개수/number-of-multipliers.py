numbers = [int(input()) for i in range(10)]
# print(numbers)
n3cnt = 0
n5cnt = 0 
for i in range(10):
    if numbers[i] % 3 == 0:
        n3cnt += 1
    if numbers[i] % 5 == 0:
        n5cnt += 1

print(n3cnt, n5cnt)
