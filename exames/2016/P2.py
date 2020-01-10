"""

"""


def f(x, y):
    return x**2 - y - 1.2


def g(x, y):
    return -x + y**2 - 1


def dfdx(x, y):
    return 2*x


def dfdy(x, y):
    return -1


def dgdx(x, y):
    return -1


def dgdy(x, y):
    return 2*y


def h(x, y):
    return ((f(x, y) * dgdy(x, y) - g(x, y) * dfdy(x, y)) /
            (dfdx(x, y) * dgdy(x, y) - dgdx(x, y) * dfdy(x, y)))


def k(x, y):
    return ((g(x, y) * dfdx(x, y) - f(x, y) * dgdx(x, y)) /
            (dfdx(x, y) * dgdy(x, y) - dgdx(x, y) * dfdy(x, y)))


def newton(xi, yi, n):
    print("{0}: {1:.7f} | {2:.7f}".format(0, xi, yi))
    for i in range(n):
        xo = xi
        yo = yi
        xi = xo - h(xo, yo)
        yi = yo - k(xo, yo)
        print("{0}: {1:.7f} | {2:.7f}".format(i+1, xi, yi))
