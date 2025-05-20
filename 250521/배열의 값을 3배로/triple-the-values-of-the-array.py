matrix = [list(map(int, input().split())) for _ in range(3)]

# 결과 계산
result = []
for row in range(3):
    result_row = []
    for col in range(3):
        result_row.append(matrix[row][col] * 3)
    result.append(result_row)

# 결과 출력
for row in result:
    print(*row)