#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:43:49 2019

@author: antonio
"""


def gauss_seidel(coef_mtx, ind, guess, stop):
    dim = len(guess)
    recurr = [g + stop + 1 for g in guess]
    while (all(abs(guess[n] - recurr[n]) < stop for n in range(dim))):
        recurr = guess.copy()
        for i in range(dim):
            a = 0
            for j in range(dim):
                if (j > i):
                    a += coef_mtx[i][j]*recurr[j]
                elif (j < i):
                    a += coef_mtx[i][j]*guess[j]
            guess[i] = (ind[i] - a) / coef_mtx[i][i]
        break
    return [round(guess, 5) for guess in guess]
