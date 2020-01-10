"""

"""


def w(x, y):
    return -1.1 * x * y + 12 * y + 7 * x**2 - 8 * x


def dwdx(x, y):
    return -1.1*y + 14*x - 8


def dwdy(x, y):
    return -1.1*x + 12


def gradiente(xi, yi):
    xo = xi + 1
    yo = yi + 1
    h = 0.1
    cnt = 0
    print("{0} : {1:.5f} | {2:.5f} | {3:.5f}".format(cnt, xi, yi, w(xi, yi)))
    while (cnt < 10):
        xo = xi
        yo = yi
        xi = xo - h * dwdx(xo, yo)
        yi = yo - h * dwdy(xo, yo)
        cnt += 1
        print("{0} : {1:.5f} | {2:.5f} | {3:.5f}".format(cnt, xi, yi, w(xi, yi)))
        if w(xi, yi) < w(xo, yo):
            h *= 2
        else:
            xi = xo
            yi = yo
            xo += 1
            yo += 1
            h /= 2
