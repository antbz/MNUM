"""
Usando o comando maxima realroots encontram-se 2 raízes para a função.

A menor raiz positiva é aproximadamente 3.98 logo:
    Sim
    Sim
    Não
    Sim

Usando como critério abs(g') < 1, observando as funções no intervalo (3.5,4.5):
    1 - converge
    2 - converge
    3 - não converge

"""


def g(x):
    return (4*x**3 - x + 3)**(1/4)


def picard_peano(x, n):
    print("{0}: {1:.7f}".format(0, x))
    for i in range(n):
        x = g(x)
        print("{0}: {1:.7f}".format(0, x))
