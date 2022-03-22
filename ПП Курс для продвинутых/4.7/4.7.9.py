# Функция создания Матрицы n*m (Наполнение: Строки с цифрами через пробел)
def make_matrix(row, col):
    return [[*map(int, input().split())] for _ in range(row)]

n, m = map(int, input().split())
matrix1 = make_matrix(n, m)
input()
m, k = map(int, input().split())
matrix2 = make_matrix(m, k)
matrix_res = [[0] * k for _ in range(n)]

# Основная программа
for i in range(n):
    for j in range(k):
        el = 0
        for r in range(m):
            el += matrix1[i][r] * matrix2[r][j]
        matrix_res[i][j] = el


[print(*r) for r in matrix_res]