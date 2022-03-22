n, m = int(input()), int(input())
mat = [[0] * m for _ in range(n)]
counter = 0
for i in range(n):
    for j in range(m):
        counter += 1
        mat[i][j] = str(counter).ljust(3)
for row in mat:
    print(*row)