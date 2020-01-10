#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Também não sei de quando é que isto é.
"""


import math

def dCdt(t, C, T):
    return -math.exp(-0.5/(T+273)) * C

def dTdt(t, C, T):
    rez = 20 * math.exp(-0.5 / (T+273)) * C - 0.5 * (T - 20)
    return rez

def euler(t, C, T, h, n, dCdt, dTdt):
    print(0, ":", t, C, T)
    for i in range(1, n+1):
        old_C = C
        old_T = T
        C += h * dCdt(t, old_C, old_T)
        T += h * dTdt(t, old_C, old_T)
        t += h
        print(i, ":", t, C, T)
    return C
        
def rk4(t, C, T, h, n, dCdt, dTdt):
    print(0, ":", t, C, T)
    for i in range(1, n+1):
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
        print(i, ":", t, C, T)
        
def quoconv(t, C, T, h, n):
    hh = h/2
    hhh = h/4
    S = euler(t,C,T,h,2,dCdt, dTdt)
    SS = euler(t,C,T,hh,2,dCdt, dTdt)
    SSS = euler(t,C,T,hhh,2,dCdt, dTdt)
    print((SS - S) / (SSS - SS), S, SS, SSS)
    

def simpson(tab, h, mult):
    t = [tab[i] for i in range(0, len(tab), mult)]
    result = 0
    for i, val in enumerate(t):
        if (i != 0 and i != len(t) - 1 and i % 2 != 0):
            result += 4 * val
        elif (i != 0 and i != len(t) - 1 and i % 2 == 0):
            result += 2 * val
        else:
            result += val
    return (h * mult/3) * result

def simpson_err(tab, h):
    return (simpson(tab, h, 2) - simpson(tab, h, 1)) / 15

def fT(t, T):
    return -0.25 * (T - 42)

def novo_euler(f, t, T, h, n):
    print(0, ":", t, T)
    for i in range(1, n+1):
        T += h * fT(t, T)
        t += h
        print(i, ":", t, T)


def gauss_seidel(A, b, guess):
    dim = len(b)
    recurr = guess.copy()
    for i in range(dim):
        soma = 0
        for j in range(dim):
            if (j < i):
                soma += A[i][j] * guess[j]
            if (j > i):
                soma += A[i][j] * recurr[j]
        guess[i] = ((b[i] - soma)/A[i][i])
    return guess
