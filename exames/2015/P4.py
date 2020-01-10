"""
Pelos gráficos conclui-se que as expressões 1 e 3 convergem nos intervalos
1 e 2 e que a expressão 3 não converge em nenhum intervalo.

Nota sobre o resíduo: supostamente seria a diferença entre o termo independente
da equação e o resultado obtido quando se substitui a solução calculada na
eq, mas na correção consideram o resíduo a diferença entre a primeira iteração
e o valor inicial
"""


from math import log


def f(x):
    return 2 * log(2*x)


def picard_peano(x, n):
    print("{0}: {1:.7f}".format(0, x))
    for i in range(n):
        x = f(x)
        print("{0}: {1:.7f}".format(i+1, x))
