n = int(input())
mat = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i > j and i < n - j - 1) or (i < j and i > n - j - 1):
            mat[i][j] = 0

[print(*row) for row in mat]
