# Функция создания Матрицы n*m (Наполнение: Строки с цифрами через пробел)
def make_matrix(row, col):
    return [[*map(int, input().split())] for _ in range(row)]


# Ввод данных и Вызов функции
n, m = map(int, input().split())
matrix1 = make_matrix(n, m)
a = input()
matrix2 = make_matrix(n, m)
matrix_res = [[0] * m for _ in range(n)]

# Основная программа
for i in range(n):
    for j in range(m):
        matrix_res[i][j] = matrix1[i][j] + matrix2[i][j]

[print(*r) for r in matrix_res]
