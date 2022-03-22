n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]
counter = 0
for i in range(m):
    for j in range(n):
        counter += 1
        mat[j][i] = str(counter).ljust(3)
[print(*row) for row in mat]
