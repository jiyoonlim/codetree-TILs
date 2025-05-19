n = int(input())
nn = list(map(int, input().split()))

new_nn = [elem * elem for elem in nn]
for i in range(n):
    print(new_nn[i], end=" ")
