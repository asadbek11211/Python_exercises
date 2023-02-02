# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 08:27:09 2023

Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
"""
def min_max_aniqla(son1, son2):
    if son1 < son2 :
        max = son2
    elif son1 == son2:
        max = 'equal'
    else:
        max = son1
    
    return f"maximum qiymat {max}"


