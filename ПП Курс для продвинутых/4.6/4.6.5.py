n = int(input())
mat = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][i] = 1
        mat[i][n - i - 1] = 1

[print(*row) for row in mat]
