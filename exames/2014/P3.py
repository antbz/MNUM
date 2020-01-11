"""

"""


A = [[0.1, 0.5, 3, 0.25],
     [1.2, 0.2, 0.25, 0.2],
     [-1, 0.25, 0.3, 2],
     [2, 1e-5, 1, 0.4]]

b = [0, 1, 2, 3]


def gauss(A, b):
    dim = len(A)
    for col in range(dim - 1):
        if (abs(A[col][col] - 1) > 1e-6):
            m = 1 / A[col][col]
            A[col] = [A[col][i] * m for i in range(dim)]
            b[col] *= m
        for line in range(col + 1, dim):
            m = A[line][col] / A[col][col]
            A[line] = [A[line][i] - m*A[col][i] for i in range(dim)]
            b[line] -= m*b[col]
    if (abs(A[dim-1][dim-1] - 1) > 1e-6):
            m = 1 / A[dim-1][dim-1]
            A[dim-1] = [A[dim-1][i] * m for i in range(dim)]
            b[dim-1] *= m
    print("Triangular inferior:")
    print(A)
    print(b)
    print()
    for col in range(dim - 1):
        for line in range(col + 1, dim):
            m = A[dim - 1 - line][dim - 1 - col] / A[dim - 1 - col][dim - 1 - col]
            A[dim - 1 - line] = [A[dim - 1 - line][i] - m*A[dim - 1 - col][i] for i in range(dim)]
            b[dim - 1 - line] -= m*b[dim - 1 - col]
    print("Solução:")
    print(A)
    print(b)
    print()
    return b


def est_ext(A, b, err):
    dim = len(A)
    x = gauss(A.copy(), b.copy())
    dAx = [sum(err * x[i] for i in range(dim)) for j in range(dim)]
    dbdAx = [err - dAx[i] for i in range(dim)]
    return gauss(A.copy(), dbdAx.copy())
