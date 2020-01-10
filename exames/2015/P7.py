"""

"""


from math import sin


def f(x):
    return x**3 - 10*sin(x) + 2.8


def bissecao(a, b, n):
    print("{0}: {1:.7f} | {2:.7f}".format(0, a, b))
    for i in range(n):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        print("{0}: {1:.7f} | {2:.7f}".format(i+1, a, b))
