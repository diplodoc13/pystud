n, m = map(int, input().split())
mat = [[0] * m for _ in range(n)]
counter = 0
for i in range(n):
    for j in range(m):
        counter += 1
        mat[i][j] = str(counter).ljust(3)

for r in range(n):
    if r % 2 == 1:
        print(*reversed(mat[r]))
    else:
        print(*mat[r])
