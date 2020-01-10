"""
f(x) = (x-4)^2 + x^4

Como a função tem uma só variável independente, é possível utilizar um
método de pesquisa unidimensional para encontrar o seu mínimo. Foram estudados
3 métodos deste tipo: método dos terços, da secção áurea e da interpolação
quádrica.
Esta resolução recorre ao método da seção áurea.
Recorrendo ao maxima, definiu-se como intervalo de partida x = (1, 1.2), por
análise do gráfico da função.

Chamando a função sec_aurea_min(f,[1,1.2]) obrém-se os resultados:

x1: 1.07639 | x2: 1.20000 | fx1: 9.88988 | fx2: 9.91360
x1: 1.07639 | x2: 1.15279 | fx1: 9.88988 | fx2: 9.87264
x1: 1.10557 | x2: 1.15279 | fx1: 9.87170 | fx2: 9.87264
x1: 1.10557 | x2: 1.13475 | fx1: 9.87170 | fx2: 9.86772
x1: 1.11672 | x2: 1.13475 | fx1: 9.86847 | fx2: 9.86772
x1: 1.12361 | x2: 1.13475 | fx1: 9.86752 | fx2: 9.86772
x1: 1.12361 | x2: 1.13050 | fx1: 9.86752 | fx2: 9.86739
x1: 1.12624 | x2: 1.13050 | fx1: 9.86738 | fx2: 9.86739
x1: 1.12624 | x2: 1.12887 | fx1: 9.86738 | fx2: 9.86735
x1: 1.12724 | x2: 1.12887 | fx1: 9.86735 | fx2: 9.86735
x1: 1.12786 | x2: 1.12887 | fx1: 9.86735 | fx2: 9.86735
x1: 1.12786 | x2: 1.12849 | fx1: 9.86735 | fx2: 9.86735
x1: 1.12786 | x2: 1.12825 | fx1: 9.86735 | fx2: 9.86734
x1: 1.12801 | x2: 1.12825 | fx1: 9.86735 | fx2: 9.86734
x1: 1.12810 | x2: 1.12825 | fx1: 9.86734 | fx2: 9.86734
x1: 1.12810 | x2: 1.12819 | fx1: 9.86734 | fx2: 9.86734

Pelo que a função tem valor mínimo em x = 1.128.
"""

from math import sqrt


def f(x):
    return (x-4) ** 2 + x ** 4


def sec_aurea_min(f, interval):
    x1 = interval[0]
    x2 = interval[1]
    B = (sqrt(5) - 1) / 2
    A = B**2
    while (abs(x1 - x2) > 0.0001):
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        fx3 = f(x3)
        fx4 = f(x4)
        if fx3 < fx4:
            x2 = x4
        else:
            x1 = x3
        print("x1: {0:.5f} | x2: {1:.5f} | fx1: {2:.5f} | fx2: {3:.5f}".format(x1, x2,f(x1),f(x2)))
