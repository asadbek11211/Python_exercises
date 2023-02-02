# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 08:19:19 2023

Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

"""
def juft_toq_aniqla(son):
    '''Juft yoki Toqlikni aniqlovchi function'''
    
    if son % 2 == 0:
        print(f"{son} soni juft")
    else:
        print(f"{son} soni toq")
print(juft_toq_aniqla(17))