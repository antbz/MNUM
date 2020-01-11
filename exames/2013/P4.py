"""

"""


from math import exp


def f(x):
    return exp(1.5*x)


def simpson(a, b, h):
    n = int(abs(b - a) / h)
    integral = f(a) + f(b)
    for i in range(1, n):
        if (i % 2 == 0):
            integral += 2 * f(a + h*i)
        else:
            integral += 4 * f(a + h*i)
    integral *= h/3
    return integral


def quo_err(a, b, h):
    S = simpson(a, b, h)
    print("{0:.5f} | {1:.7g}".format(h, S))
    hh = h / 2
    SS = simpson(a, b, hh)
    print("{0:.5f} | {1:.7g}".format(hh, SS))
    hhh = h / 4
    SSS = simpson(a, b, hhh)
    print("{0:.5f} | {1:.7g}".format(hhh, SSS))
    QC = (SS - S) / (SSS - SS)
    err = (SSS - SS) / 15
    print("QC: {0:.7f} | err: {1:.7e}".format(QC, err))
