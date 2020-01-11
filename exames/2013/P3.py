"""

"""


def z(x, y):
    return 3*x**2 - x*y + 11*y + y**2 - 8*x


def dzdx(x, y):
    return 6*x - y - 8


def dzdy(x, y):
    return 2*y - x + 11


def gradiente(x, y, h, n):
    print("{0}: {1:.2f} | {2:.7f} | {3:.7f} | {4:.7f} | {5:.7f}".format(0, x, y, z(x, y), dzdx(x, y), dzdy(x, y)))
    for i in range(n):
        xo = x
        yo = y
        x -= h * dzdx(xo, yo)
        y -= h * dzdy(xo, yo)
        if z(x, y) < z(xo, yo):
            h *= 2
        else:
            x = xo
            y = yo
            h /= 2
        print("{0}: {1:.2f} | {2:.7f} | {3:.7f} | {4:.7f} | {5:.7f}".format(i+1, x, y, z(x, y), dzdx(x, y), dzdy(x, y)))
