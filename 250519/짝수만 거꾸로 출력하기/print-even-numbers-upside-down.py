n = int(input())
nn = list(map(int, input().split()))

nn = nn[::-1]

nn = [i for i in nn if i%2 == 0]


print(*nn)