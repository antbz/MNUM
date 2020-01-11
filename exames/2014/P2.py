"""
Explorando o gráfico conclui-se que a função tem 3 zeros no intervalo (0, 50)

Os resultados são sempre aproximações portanto o número de casas decimais
exatas é 0.
"""


from math import cos, sin, sqrt


def g(x):
    return -x + 40*cos(sqrt(x)) + 3


def dg(x):
    return -1 - (20*sin(sqrt(x)) / sqrt(x))


def newton(x, n):
    print("{0}: {1:.7f} | {2:.7f}".format(0, x, g(x)))
    for i in range(n):
        x -= g(x) / dg(x)
        print("{0}: {1:.7f} | {2:.7f}".format(i+1, x, g(x)))
