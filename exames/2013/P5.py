"""

"""

from math import sin, cos


def f(x):
    return (x - 3.7) + (cos(x + 1.2))**3


def df(x):
    return 1 - 3 * (cos(x + 1.2))**2 * sin(x + 1.2)


def newton(x, n):
    print("{0}: {1:.7f} | {2:.7f}".format(0, x, f(x)))
    for i in range(n):
        x -= f(x)/df(x)
        print("{0}: {1:.7f} | {2:.7f}".format(i+1, x, f(x)))
