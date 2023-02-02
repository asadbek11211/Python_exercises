# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 07:57:31 2023

Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

"""
def hisobla(son):
    '''Sonning kvadratini va kubini hisoblovchi function'''
    kvadrat = son * son
    kub = kvadrat * son
    
    print(f"{son} ning kvadrati : {kvadrat} \n "
         f"{son} ning kubi : {kub}")
    return kvadrat, kub

print(hisobla(4))