#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:13:39 2019

@author: antonio
"""

from math import sin, pi


def f(x):
    return sin(x) / x ** 2


def trapezios(f, n, a, b):
    h = (b - a) / n
    soma = 0
    for i in range(n + 1):
        if (i != 0 and i != n):
            soma += 2 * f(a + i*h)
        else:
            soma += f(a + i*h)
    return (h / 2) * soma

tabela = [(0,1.04), (0.25,0.37), (0.5, 0.38), (0.75, 1.49), (1, 1.08), (1.25, 0.13), (1.5, 0.64), (1.75, 0.84), (2, 0.12)]

def trapezios_tab(tabela, h, mult):
    soma = 0
    tab = [tabela[i] for i in range(0, len(tabela), mult)]
    n = len(tab) - 1
    for i, pair in enumerate(tab):
        if (i != 0 and i != n):
            soma += 2 * pair[1]
        else:
            soma += pair[1]
    return (h*mult / 2) * soma


def simpson(f, n, a, b):
    h = (b - a) / n
    soma = 0
    for i in range(n + 1):
        if (i != 0 and i != n and i % 2 != 0):
            soma += 4 * f(a + i*h)
        elif (i != 0 and i != n and i % 2 == 0):
            soma += 2 * f(a + i*h)
        else:
            soma += f(a + i*h)
    return (h / 3) * soma

def simpson_tab(tabela, h, mult):
    soma = 0
    tab = [tabela[i] for i in range(0, len(tabela), mult)]
    n = len(tab) - 1
    for i, pair in enumerate(tab):
        if (i != 0 and i != n and i % 2 != 0):
            soma += 4 * pair[1]
        elif (i != 0 and i != n and i % 2 == 0):
            soma += 2 * pair[1]
        else:
            soma += pair[1]
    return (h*mult / 3) * soma


def quoconv(f, n, a, b, m):
    return ((m(f, n * 2, a, b) - m(f, n, a, b)) /
            (m(f, n * 4, a, b) - m(f, n * 2, a, b)))

def quoconv_tab(tabela, h, m, o):
    return((m(tabela, h, 2) - m(tabela, h, 4)) /
           (m(tabela, h, 1) - m(tabela, h, 2)))

def err(f, n, a, b, m, o):
    return (m(f, n * 4, a, b) - m(f, n * 2, a, b)) / (o - 1)

def err_tab(tabela, h, m, o):
    return (m(tabela, h, 1) - m(tabela, h, 2)) / o
