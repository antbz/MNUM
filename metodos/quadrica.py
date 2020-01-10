#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 10:56:30 2019

@author: antonio
"""


from math import cos, sin


def f(x, y):
    return y**2 - 2*x*y - 6*y + 2*x**2 + 15 + cos(10*x)


def dfdx(x, y):
    return 4*x - 2*y - 10*sin(10*x)


def dfdy(x, y):
    return 2*y - 2*x - 6


def grad(x, y):
    return [dfdx(x, y), dfdy(x, y)]


def inv_h(x, y):
    return [[-1 / (100*cos(10*x) - 2), -1 / (100*cos(10*x) - 2)],
            [-1 / (100*cos(10*x) - 2), (25*cos(10*x) * 1) / (50*cos(10*x) - 1)]]


def f1(x, y):
    return (5*sin(10*x) - x + 3) / (50*cos(10*x) - 1)


def f2(x, y):
    return (((50*cos(10*x) - 1)*y + 5*sin(10*x) + (-50*x - 150)*cos(10*x) + 6)
            / (50*cos(10*x) - 1))


def quadrica(x0, y0):
    for i in range(11):
        x1 = x0 - f1(x0, y0)
        y1 = y0 - f2(x0, y0)
        x0, y0 = x1, y1
        print(x0, y0)
    return (x0, y0)
