"""

"""


def dTdt(t, T):
    return -0.25 * (T - 37)


def euler(t, T, h, n):
    print("{0}: {1:.7f} | {2:.7f}".format(0, t, T))
    for i in range(n):
        T += h * dTdt(t, T)
        t += h
        print("{0}: {1:.7f} | {2:.7f}".format(i+1, t, T))
