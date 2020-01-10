#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:04:26 2019

@author: antonio
"""


def gauss_jacobi(coef_mtx, ind, guess, stop):
    dim = len(guess)
    recurr = [g + stop + 1 for g in guess]
    while (all(abs(guess[n] - recurr[n]) < stop for n in range(dim))):
        recurr = guess.copy()
        for i in range(dim):
            a = 0
            for j in range(dim):
                if (i != j):
                    a += coef_mtx[i][j]*recurr[j]
            guess[i] = (ind[i] - a) / coef_mtx[i][i]
    return [round(guess, 3) for guess in guess]
