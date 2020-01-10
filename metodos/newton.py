#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:54:55 2019

@author: antonio
"""

from math import sqrt


def quad(a, b, c):
    det = b ** 2 - 4 * a * c
    if (det < 0):
        raise Exception("NO ROOTS!")
    if (det == 0):
        return -b / (2 * a)
    return ((-b + sqrt(det)) / (2 * a), (-b - sqrt(det)) / (2 * a))


def f(x):
    return 2 * x ** 2 - 5 * x - 2


def df(x):
    return 4 * x - 5


def g(x):
    return x - f(x) / df(x)


print("ACTUAL ROOTS: {0}".format(quad(2, -5, -2)))


guess = int(input("Initial guess for root: "))


for i in range(20):
    guess = g(guess)


print(guess)
