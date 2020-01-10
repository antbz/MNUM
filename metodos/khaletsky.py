#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:43:30 2019

@author: antonio
"""


def suml(A, U, L, i, j):
    result = 0
    for k in range(j):
        result += L[i][k]*U[k][j]
    return result


def sumu(A, U, L, i, j):
    result = 0
    for k in range(i):
        result += L[i][k]*U[k][j]
    return result


def empty(dim):
    m = []
    for i in range(dim):
        m.append([])
        for j in range(dim):
            if i == j:
                m[i].append(1)
                continue
            m[i].append(0)
    return m


A = [[1, 1, 1], [3, -1, 2], [2, 0, 2]]
b = [8, -1, 5]


def khaletsky(A, b):
    dim = len(A)
    L = empty(dim)
    U = empty(dim)

    for p in range(dim):
        for i in range(dim):
            if i < p:
                continue
            L[i][p] = A[i][p] - suml(A, U, L, i, p)
        for j in range(dim):
            if p == j:
                continue
            elif j < p:
                continue
            U[p][j] = (A[p][j] - sumu(A, U, L, p, j))/L[p][p]

    y = []
    x = [0, 0, 0]

    for i in range(dim):
        summa = 0
        for k in range(i):
            summa += L[i][k] * y[k]
        y.append((b[i] - summa) / L[i][i])

    for i in range(dim-1, -1, -1):
        summa = 0
        for k in range(i+1, dim):
            summa += U[i][k] * x[k]
        x[i] = (y[i] - summa) / U[i][i]

    return x
