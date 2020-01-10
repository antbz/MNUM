#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:58:00 2019

@author: antonio
"""

from math import *

def f(x,y):
    return 2*x**2-x*y-5*x+1

def g(x,y):
    return x + 3 * (log(x) / log(10)) - y**2

def dfx(x,y):
    return -y + 4*x -5
    
def dfy(x,y):
    return -x
    
def dgx(x,y):
    return (3/(log(10)*x)) + 1
    
def dgy(x,y):
    return -2*y

def jacobian(x,y):
    return dfx(x,y)*dgy(x,y) - dfy(x,y) * dgx(x,y)

def h(x,y):
    return (f(x,y) * dgy(x,y) - g(x,y) * dfy(x,y))/jacobian(x,y)

def k(x,y):
    return (g(x,y) * dfy(x,y) - f(x,y) * dgx(x,y))/jacobian(x,y)

guess_x = 1.46
guess_y = -1.41
old_x = 1.46
old_y = -1.41

    
for i in range(40):
    guess_x = old_x - h(old_x, old_y)
    guess_y = old_y - k(old_x, old_y)
    old_x = guess_x
    old_y = guess_y

print(guess_x, guess_y)