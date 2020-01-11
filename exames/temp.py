#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 18:58:27 2020

@author: antonio
"""

from math import sqrt

def f1(x):
    return sqrt(x**2 + 1) - x

def f2(x):
    return 1 / (sqrt(x**2 + 1) + x)

def compare():
    for i in range(20):
        print("{0:.20f} | {1:.20f}".format(f1(i*1e-7), f2(i*1e-7)))