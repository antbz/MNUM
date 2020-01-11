"""
Valores calculados usando as funções definidas
"""


from math import exp, sqrt


def df(x):
    return sqrt(1 + (2.5 * exp(2.5 * x)) ** 2)


def trapezios(f, a, b, h):
    n = int((b - a) / h)
    integral = f(a) + f(b)
    for i in range(1, n):
        integral += 2 * f(a + h*i)
    integral *= h/2
    return integral


def simpson(f, a, b, h):
    n = int((b - a) / h)
    integral = f(a) + f(b)
    for i in range(1, n):
        if (i % 2 == 0):
            integral += 2 * f(a + h*i)
        else:
            integral += 4 * f(a + h*i)
    integral *= h/3
    return integral


def quo_cnv(metodo, f, a, b, h):
    return (metodo(f, a, b, h/2) - metodo(f, a, b, h)) / (metodo(f, a, b, h/4) - metodo(f, a, b, h/2))


def erro(metodo, f, a, b, h, n):
    return (metodo(f,a,b,h/4) - metodo(f,a,b,h/2)) / n
