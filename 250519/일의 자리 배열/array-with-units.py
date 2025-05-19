arr = list(map(int, input().split()))

a = arr
for i in range(2,10):
    a.append((arr[i-2] + arr[i-1]) % 10)
print(*a)
    