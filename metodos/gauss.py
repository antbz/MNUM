#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:01:43 2019

@author: antonio
"""

# AUXILIARY FUNCTIONS
def swap(l, a, b):
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp


def sublist(l1, l2):
    if len(l1) != len(l2):
        raise Exception("Lists of different dimensions!")
    for i in range(len(l1)):
        l1[i] = l1[i] - l2[i]


def multlist(l, a):
    res = []
    for elem in l:
        res.append(elem * a)
    return res


def inner(u, v):
    result = 0
    for i in range(len(u)):
        result += u[i]*v[i]

    return result


coef_mtx = [[2, -1, 2], [1, -2, 1], [3, -1, 2]]
ind_mtx = [0, 6, 11]


def gauss(coef_mtx, ind_mtx):
    dim = len(ind_mtx)
    
    # Swap matrix lines so the 1st element is an unit
    for i, line in enumerate(coef_mtx):
        if abs(line[0]) == 1 and i == 0:
            break
        elif abs(line[0]) == 1:
            swap(coef_mtx, 0, i)
            swap(ind_mtx, 0, i)
            break
    
    print(coef_mtx)
    print(ind_mtx)
    print()
    
    # Eliminar elementos de cima para baixo
    for k in range(len(coef_mtx) - 1):
        for i in range(k + 1, len(coef_mtx)):
            a = coef_mtx[i][k] / coef_mtx[k][k]
            sublist(coef_mtx[i], multlist(coef_mtx[k], a))
            ind_mtx[i] -= a*ind_mtx[k]
            b = 1 / coef_mtx[i][k+1]
            coef_mtx[i] = multlist(coef_mtx[i], b)
            ind_mtx[i] *= b
    
    
    print(coef_mtx)
    print(ind_mtx)
    print()
    
    
    # Eliminar elementos de baixo para cima
    for k in range(len(coef_mtx) - 1):
        for i in range(k + 1, len(coef_mtx)):
            a = coef_mtx[dim - 1 - i][dim - 1 - k] / coef_mtx[dim - 1 - k][dim - 1 - k]
            sublist(coef_mtx[dim - 1 - i], multlist(coef_mtx[dim - 1 - k], a))
            ind_mtx[dim - 1 - i] -= a*ind_mtx[dim - 1 - k]
            b = 1 / coef_mtx[dim - 1 - i][dim - 1 - k - 1]
            coef_mtx[dim - 1 - i] = multlist(coef_mtx[dim - 1 - i], b)
            ind_mtx[dim - 1 - i] *= b

    print(coef_mtx)
    print(ind_mtx)
    print()


gauss(coef_mtx, ind_mtx)


# ESTABILIDADE EXTERNA GAUSS
coef_err = [[0.1, 0.1, 0.1], [0.1, 0.1, 0.1], [0.1, 0.1, 0.1]]
ind_err = [0.1, 0.1, 0.1]
coef_mtx = [[18, -1, 1], [3, -5, 4], [6, 8, 29]]
ind_mtx = [0.552949, -0.15347, -0.10655]
dAx = []

for i in range(len(coef_err)):
    dAx.append(inner(ind_mtx,coef_err[i]))

print(dAx)

sublist(ind_err, dAx)
    
print(ind_err)

gauss(coef_mtx, ind_err)
