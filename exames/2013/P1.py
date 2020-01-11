"""

"""


def dydt(t, y, z):
    return z


def dzdt(t, y, z):
    return 0.5 + t**2 + t*z


def euler(t, y, z, h, n):
    print("{0}: {1:.2f} | {2:.7f} | {3:.7f}".format(0, t, y, z))
    for i in range(n):
        yo = y
        zo = z
        y += h * dydt(t, yo, zo)
        z += h * dzdt(t, yo, zo)
        t += h
        print("{0}: {1:.2f} | {2:.7f} | {3:.7f}".format(i+1, t, y, z))


def rk4(t, y, z, h, n):
    print("{0}: {1:.2f} | {2:.7f} | {3:.7f}".format(0, t, y, z))
    for i in range(n):
        d1 = h * dydt(t, y, z)
        l1 = h * dzdt(t, y, z)
        d2 = h * dydt(t + h/2, y + d1/2, z + l1/2)
        l2 = h * dzdt(t + h/2, y + d1/2, z + l1/2)
        d3 = h * dydt(t + h/2, y + d2/2, z + l2/2)
        l3 = h * dzdt(t + h/2, y + d2/2, z + l2/2)
        d4 = h * dydt(t + h, y + d3, z + l3)
        l4 = h * dzdt(t + h, y + d3, z + l3)

        y += d1/6 + d2/3 + d3/3 + d4/6
        z += l1/6 + l2/3 + l3/3 + l4/6
        t += h

        print("{0}: {1:.2f} | {2:.7f} | {3:.7f}".format(i+1, t, y, z))
