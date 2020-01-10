"""
Critérios de paragem:
    Aplica-se - para quando está perto de 0
    Não se aplica - o valor não variar não garante que estamos perto de um 0
    Aplica-se - para quando o x deixa de variar pois estamos perto de um 0
    Aplica-se - se o intervalo está muito pequeno estamos perto de um 0
"""


def f(x):
    return x**7 + 0.5*x - 0.5


def zero(a, b):
    return (a * f(b) - b * f(a)) / (f(b) - f(a))


def corda(a, b, n):
    c = zero(a, b)
    print("{0}: {1:.7f} | {2:.7f} | {3:.7f}".format(0, a, b, c))
    for i in range(n):
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = zero(a, b)
        print("{0}: {1:.7f} | {2:.7f} | {3:.7f}".format(i + 1, a, b, c))
