# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:38:26 2023

Ihtiyoriy sonning 3-darajasini hisoblovchi POWER3 nomli funksiya hosil qiling

"""
def POWER3(son):
    '''Ihtiyoriy sonning 3-darajasini hisoblovchi POWER3 nomli funksiya'''
    son1 = pow(son,3)
    natija = F"{son} sonining 3-darajasi {son1} ga teng"
    return natija

print(POWER3(7))