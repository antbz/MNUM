#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 11:33:05 2019

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


def f1(x):
    return (2 / 5) * x ** 2 - (2 / 5)


def f2(x):
    return (5 / 2) + (1 / x)


def f3(x):
    return sqrt((5 / 2) * x + 1)


def f4(x):
    return -sqrt((5 / 2) * x + 1)


max_iter = 50


num_iter = 0
guess = float(input("INITIAL GUESS: "))
prev_val = guess + 1
while (abs(guess - prev_val) > 1e-5 and num_iter <= max_iter):
    prev_val = guess
    guess = f1(guess)
    num_iter += 1

print("Expression 1 found the value: {0} after {1} iterations".format(guess, num_iter))

num_iter = 0
guess = float(input("INITIAL GUESS: "))
prev_val = guess + 1
while (abs(guess - prev_val) > 1e-5 and num_iter <= max_iter):
    prev_val = guess
    guess = f2(guess)
    num_iter += 1

print("Expression 2 found the value: {0} after {1} iterations".format(guess, num_iter))

num_iter = 0
guess = float(input("INITIAL GUESS: "))
prev_val = guess + 1
while (abs(guess - prev_val) > 1e-5 and num_iter <= max_iter):
    prev_val = guess
    guess = f3(guess)
    num_iter += 1

print("Expression 3 found the value: {0} after {1} iterations".format(guess, num_iter))

num_iter = 0
guess = float(input("INITIAL GUESS: "))
prev_val = guess + 1
while (abs(guess - prev_val) > 1e-5 and num_iter <= max_iter):
    prev_val = guess
    guess = f4(guess)
    num_iter += 1

print("Expression 4 found the value: {0} after {1} iterations".format(guess, num_iter))



print("ACTUAL ROOTS: {0}".format(quad(2, -5, -2)))
