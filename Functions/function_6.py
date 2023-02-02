# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 08:50:48 2023

Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. 
Natijalarni konsolga chiqaring.
"""
def qoldiq_aniqla(son):
    '''Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya'''
    natija = []
    for a in range(2,11):
        if son % a == 0:
            natija.append(a)
    print(f"{son} soni {natija} larga qoldiqsiz bo'linadi")

