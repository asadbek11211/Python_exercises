# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:47:40 2023

Asadbek Ro'ziboyev
Masalaning qo'yilishi:
    Foydalanuvchidan biror butun son kiritishni so'rang. 
    Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
"""
son = int(input("Biror butun son kiriting : "))
qoldiq = []
for a in range(2,11):
    if son % a == 0:
        qoldiq.append(a) 
        
print(f"{son} soni {qoldiq} sonlarga qoldiqsiz bo'linadi")
