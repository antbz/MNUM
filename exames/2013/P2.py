"""
A partir dos valores obtidos no maxima (ver P2-1.png), conclui-se que a
solução mais adequada é a obtida com pivotagem, pois o erro resultante é
menor.

Não se obtiveram resultados iguais devido às aproximações realizadas nos
cálculos pela máquina. No caso sem pivotagem, o facto de estarmos a usar
1e-5 como valor pivot para a primeira coluna, são introduzidos erros pelo
facto de se estar a operar com um número pequeno em V.F.

A sensibilidade de um sistema a erros nos dados/externos é determinada pela
sua estabilidade externa, que é calculada perturbando os coeficiente e
termos independentes com um parâmetro e resolvendo novamente o sistema usando
os parâmetros perturbados.
Este cálculo é equivalente a resolver o sistema:
    A.dx = db - dA.x
    Em que:
        A - matriz de coeficientes do sistema
        dx - erro resultante
        db - erro dos termos independentes (constante)
        dA - erro dos coeficientes (constante)
        x - soluções obtidas para o sistema
Usando pivotagem e um erro de 0.05, é possível observa que o parâmetro mais
sensível a erros externos é x1 e o menos sensível é x2.
"""

A = [[1, -0.2, 1],
     [1e-5, 2, 5],
     [3, 0.5, -4]]

b = [4, 200, 2]


def gauss(A, b):
    dim = len(A)
    for col in range(dim - 1):
        if (abs(1 - A[col][col]) > 1e-6):
            m = 1 / A[col][col]
            A[col] = [A[col][i] * m for i in range(dim)]
            b[col] *= m
        for line in range(col + 1, dim):
            m = A[line][col]
            A[line] = [A[line][i] - m * A[col][i] for i in range(dim)]
            b[line] -= m * b[col]
    if (abs(1 - A[dim-1][dim-1]) > 1e-6):
            m = 1 / A[dim-1][dim-1]
            A[dim-1] = [A[dim-1][i] * m for i in range(dim)]
            b[dim-1] *= m
    print("Triangular superior:")
    print(A)
    print(b)
    print()
    for col in range(dim - 1):
        for line in range(col + 1, dim):
            m = A[dim-1 - line][dim-1 - col]
            A[dim-1 - line] = [A[dim-1 - line][i] - m * A[dim-1 - col][i] for i in range(dim)]
            b[dim-1 - line] -= m * b[dim-1 - col]
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
