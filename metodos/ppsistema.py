#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:24:42 2019

@author: antonio
"""

from math import sqrt, log


def g1(x,y):
    return sqrt((x*(y+5)-1)/2)


def g2(x,y):
    return -sqrt(x+log(x)/log(10))


guess_x = float(input("GUESS X: "))
guess_y = float(input("GUESS Y: "))

old_x = guess_x
old_y = guess_y

for i in range(20):
    guess_x = g1(old_x, old_y)
    guess_y = g2(old_x, old_y)
    old_x = guess_x
    old_y = guess_y
    
print("x: {0} y: {1}".format(guess_x, guess_y))
