eng = input()
fruits = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for i in range(len(fruits)):
    if (fruits[i][2] == eng) or (fruits[i][3] == eng):
        print(fruits[i])
        cnt += 1

print(cnt)