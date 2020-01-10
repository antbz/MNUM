"""

"""


from math import exp


def dCdt(t, C, T):
    return -exp(-0.5/(T + 273)) * C


def dTdt(t, C, T):
    return 30 * exp(-0.5/(T + 273)) * C - 0.5 * (T - 20)


def euler(t, C, T, h, n):
    cnt = 0
    print("{0}: {1:.5f} | {2:.5f} | {3:.5f}".format(cnt, t, C, T))
    for i in range(n):
        Tn = T
        T += h * dTdt(t, C, T)
        C += h * dCdt(t, C, Tn)
        t += h
        cnt += 1
        print("{0}: {1:.5f} | {2:.5f} | {3:.5f}".format(cnt, t, C, T))
    print()
    return T


def rk4(t, C, T, h, n):
    cnt = 0
    print("{0}: {1:.5f} | {2:.5f} | {3:.5f}".format(cnt, t, C, T))
    for i in range(n):
        d1 = h * dCdt(t, C, T)
        l1 = h * dTdt(t, C, T)
        d2 = h * dCdt(t + h/2, C + d1/2, T + l1/2)
        l2 = h * dTdt(t + h/2, C + d1/2, T + l1/2)
        d3 = h * dCdt(t + h/2, C + d2/2, T + l2/2)
        l3 = h * dTdt(t + h/2, C + d2/2, T + l2/2)
        d4 = h * dCdt(t + h, C + d3, T + l3)
        l4 = h * dTdt(t + h, C + d3, T + l3)

        C += d1/6 + d2/3 + d3/3 + d4/6
        T += l1/6 + l2/3 + l3/3 + l4/6
        t += h
        cnt += 1

        print("{0}: {1:.5f} | {2:.5f} | {3:.5f}".format(cnt, t, C, T))


def quo_cnv(t, C, T, h, n):
    return (euler(t, C, T, h/2, n*2) - euler(t, C, T, h, n)) / (euler(t, C, T, h/4, n*4) - euler(t, C, T, h/2, n*2))


def erro(t, C, T, h, n):
    return (euler(t, C, T, h/4, n*4) - euler(t, C, T, h/2, n*2))
