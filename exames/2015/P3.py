"""
Created on Fri Jan 10 17:08:16 2020

@author: antonio
"""




def gauss(A, b):
    for col in range(len(A) - 1):
        for line in range(col + 1, len(A)):
            m = A[line][col] / A[col][col]
            A[line] = [A[line][i] - m * A[col][i] for i in range(len(A))]
            b[line] -= m * b[col]
        m = 1 / A[col+1][col+1]
        A[col+1] = [A[col+1][i] * m for i in range(len(A))]
        b[col+1] *= m
    print("Triangular inferior:")
    print(A)
    print(b)
    print()
    for col in range(len(A) - 1):
        for line in range(col + 1, len(A)):
            m = A[len(A) - 1 - line][len(A) - 1 - col] / A[len(A) - 1 - col][len(A) - 1 - col]
            A[len(A) - 1 - line] = [A[len(A) - 1 - line][i] - m * A[len(A) - 1 - col][i] for i in range(len(A))]
            b[len(A) - 1 - line] -= m * b[len(A) - 1 - col]
    print("Solução:")
    print(A)
    print(b)
    print()
    return b.copy()

def est_ext(err):
    A = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]
    b = [-1, 1, 1]
    x = gauss(A.copy(), b.copy())
    dAx = [sum(err * x[j] for j in range(len(A))) for i in range(len(A))]
    dbdAdx = [err - dAx[i] for i in range(len(A))]
    gauss(A.copy(), dbdAdx.copy())