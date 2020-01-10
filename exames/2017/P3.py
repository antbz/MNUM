"""
Recorrendo ao maxima para desenhar o gráfico da função, é possível observar
duas raízes, uma em x = (1.8, 2) e outra em x = (-5,-4.8)

Uma fórmula de recorrência converge apenas se o valor absoluto da sua derivada
no intervalo considerado é inferior a 1. Usando esse critério:
No intervalo x = (-5,-4.8) apenas g1 converge.
No intervalo x = (1.8, 2) apenas g2 converge.

O outro método não intervalar estudado é o método de Newton.
A formula de recorrencia utilizada no picard-peano é a segunda.
O critério de paragem é que a diferença entre iterações consecutivas seja
menor do que 1e-7.
Usou-se em ambos os casos a guess inicial de 1.8.
Conclui-se que o método de newton apresenta melhor desempenho neste caso,
visto que demora menos uma iteração do que o picard-peano a satisfazer o
critério de paragem e no geral os valores estabilizam mais rápido - a diferença
entre iterações é menor.
"""


from math import exp, log


def f(x):
    return exp(x) - x - 5


def df(x):
    return exp(x)


def g(x):
    return log(5 + x)


def newton(f, df, guess):
    old_guess = guess + 1
    cnt = 0
    print("{0} : {1:.6f}".format(cnt, guess))
    while(abs(guess - old_guess) > 1e-7):
        old_guess = guess
        guess = old_guess - f(old_guess) / df(old_guess)
        cnt += 1
        print("{0} : {1:.7f} | {2:.7f}".format(cnt, guess, abs(guess-old_guess)))
    return guess


def picard_peano(g, guess):
    old_guess = guess + 1
    cnt = 0
    print("{0} : {1:.6f}".format(cnt, guess))
    while(abs(guess - old_guess) > 1e-7):
        old_guess = guess
        guess = g(old_guess)
        cnt += 1
        print("{0} : {1:.7f} | {2:.7f}".format(cnt, guess, abs(guess-old_guess)))
    return guess
