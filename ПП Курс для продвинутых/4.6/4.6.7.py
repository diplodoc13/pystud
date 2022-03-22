n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mat[i][j] = (i + j) % m + 1

[print(*row) for row in mat]
