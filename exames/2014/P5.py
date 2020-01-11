"""

"""


from math import cos, sin, sqrt


def f(x):
    return 5*cos(x) - sin(x)


def aurea(x1, x2, n):
    B = (sqrt(5) - 1) / 2
    A = B**2
    for i in range(n):
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        fx1 = f(x1)
        fx2 = f(x2)
        fx3 = f(x3)
        fx4 = f(x4)
        print("""{0}: {1:.7f} | {2:.7f} | {3:.7f} | {4:.7f} | {5:.7f} | {6:.7f} | {7:.7f} | {8:.7f}""".format(i+1, x1, x2, x3, x4, fx1, fx2, fx3, fx4))
        if fx3 < fx4:
            x2 = x4
        else:
            x1 = x3
    print("Intervalo: {0:.7f} - {1:.7f}".format(x1, x2))
    print("Amplitude: {0:.7f}".format(abs(x1-x2)))
