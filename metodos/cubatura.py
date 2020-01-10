#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:50:06 2019

@author: antonio
"""


def trapezios_duplo(matriz, hx, hy):
    integral = 0
    for i, z_line in enumerate(matriz):
        for j, z in enumerate(z_line):
            if (i == 0 and (j == 0 or j == 2)) or (i == 2 and (j == 0 or j == 2)):
                integral += z
            elif (j == 1 and (i == 0 or i == 2)) or (i == 1 and (j == 0 or j == 2)):
                integral += 2*z
            else:
                integral += 4*z
    return ((hx*hy)/4) * integral


def simpson_duplo(matriz, hx, hy):
    integral = 0
    for i, z_line in enumerate(matriz):
        for j, z in enumerate(z_line):
            if (i == 0 and (j == 0 or j == 2)) or (i == 2 and (j == 0 or j == 2)):
                integral += z
            elif (j == 1 and (i == 0 or i == 2)) or (i == 1 and (j == 0 or j == 2)):
                integral += 4*z
            else:
                integral += 16*z
    return ((hx*hy)/9) * integral


matriz = [[1.1, 1.4, 7.7], [2.1, 3.1, 2.2], [7.3, 1.5, 1.2]]
