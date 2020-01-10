#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:16:00 2019

@author: antonio
"""

from math import exp

def f(x, y):
    return -0.25 * (y - 42)


def fy(x, y, z):
    return z


def fz(x, y, z):
    return 2 + x ** 2 + x * z


def fC(t, T, C):
    return -exp(-0.5/(T+273)) * C

def fT(t, T, C):
    return 20 * exp(-0.5/(T+273)) * C - 0.5 * (T - 20)

def euler(x, y, a, b, h, f):
    n = int((b-a)/h)
    print(n)
    print(0, ":", x, y)
    for i in range(1,n+1):
        y += h * f(x, y)
        x += h
        print (i, ":", x, y)
        
def euler_3var(x, y, z, h, n, f, g):
    print (0, ":", x, y, z)
    for i in range(1,n+1):
        yn = y
        zn = z
        y += h * f(x, yn, zn)
        z += h * g(x, yn, zn)
        x += h
        print (i, ":", x, y, z)
    

def rk2(x, y, a, b, h, f):
    n = int((b-a)/h)
    print(n)
    print(0, ":", x, y)
    for i in range(1, n+1):
        y += h * f(x + h/2, y + (h/2) * f(x, n))
        x += h
        print(i, ":", x, y)


def rk4(x, y, a, b, h, f):
    n = int((b-a)/h)
    print(n)
    print(0, ":", x, y)
    for i in range(1, n+1):
        d1 = h * f(x, y)
        d2 = h * f(x + h/2, y + d1/2)
        d3 = h * f(x + h/2, y + d2/2)
        d4 = h * f(x + h, y + d3)
        
        y += d1/6 + d2/3 + d3/3 + d4/6
        x += h
        print(i, ":", x, y)
        
        
def rk4_3var(x, y , z, h, n, f, g):
    print(0, ":", x, y, z)
    for i in range(1, n+1):
        d1 = h * f(x, y, z)
        l1 = h * g(x, y, z)
        d2 = h * f(x + h/2, y + d1/2, z + l1/2)
        l2 = h * g(x + h/2, y + d1/2, z + l1/2)
        d3 = h * f(x + h/2, y + d2/2, z + l2/2)
        l3 = h * g(x + h/2, y + d2/2, z + l2/2)
        d4 = h * f(x + h, y + d3, z + l3)
        l4 = h * g(x + h, y + d3, z + l3)
        
        z += l1/6 + l2/3 + l3/3 + l4/6
        y += d1/6 + d2/3 + d3/3 + d4/6
        x += h
        print(i, ":", x, y, z)
