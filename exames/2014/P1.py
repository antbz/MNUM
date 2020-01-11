"""
Passo: 0.1
Valor inicial: 1
Testando para os vários k conclui-se que o valor é 20.
"""


def dxdt(t, x, y):
    return y


def dydt(t, x, y, k):
    return (-k*x - y) / 20


def euler(t, x, y, k, h, n):
    print("{0}: {1:.2f} | {2:.7f}".format(0, t, x))
    for i in range(n):
        xo = x
        yo = y
        x += h * dxdt(t, xo, yo)
        y += h * dydt(t, xo, yo, k)
        t += h
        print("{0}: {1:.2f} | {2:.7f}".format(i+1, t, x))
