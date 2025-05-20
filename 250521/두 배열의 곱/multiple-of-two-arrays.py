# 첫 번째 3x3 행렬 입력
matrix1 = []
for _ in range(3):
    matrix1.append(list(map(int, input().split())))

# 빈 줄 처리
while True:
    line = input()
    if line.strip() == '':
        break

# 두 번째 3x3 행렬 입력
matrix2 = []
for _ in range(3):
    matrix2.append(list(map(int, input().split())))

# 원소별 곱셈 결과 계산
result = []
for i in range(3):
    result_row = []
    for j in range(3):
        result_row.append(matrix1[i][j] * matrix2[i][j])
    result.append(result_row)

# 출력
for row in result:
    print(*row)
