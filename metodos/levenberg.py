#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:45:56 2019

@author: antonio
"""


from math import cos, sin


def f1(x, y):
    return (x + 1)**2 - (y - 4)**2


def hLMx1(x, y, l):
    return x + 1 + l * (2 * (x + 1))


def hLMy1(x, y, l):
    return y - 4 + l * (-2 * (y - 4))

def f(x, y):
    return sin(y) + y**2/4 + cos(x) + x**2/4 - 1

def hLMx(x, y, l):
    return (x/2 - sin(x)) / (1/2 - cos(x)) + l * (x/2 - sin(x))

def hLMy(x, y, l):
    return (cos(y) + y/2) / (1/2 - sin(y)) + l * (cos(y) + y/2)


def levenberg_marquardt(x0, y0):
    x1 = x0 + 1
    y1 = y0 + 1
    l = 0.1
    for i in range(13):
        x1 = x0 - hLMx(x0, y0, l)
        y1 = y0 - hLMy(x0, y0, l)
        if (f(x1, y1) < f(x0, y0)):
            l /= 2
        elif (f(x1, y1) > f(x0, y0)):
            l *= 2
        x0 = x1
        y0 = y1
        print(x0, y0, f(x0, y0))
        