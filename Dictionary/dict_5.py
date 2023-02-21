# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:08:52 2023
Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
"""

davlatlar = ['turkiya',"uzbekiston",'Rassiya','xitoy']
poytaxtlar = ['istanbul','toshkent','moskva','pekin']

print("\n  Davlatlar \n")
for davlat in sorted(davlatlar):
    print(davlat.title())

print("\n  Poytaxtlar \n")
for poytaxt in sorted(poytaxtlar):
    print(poytaxt.title())

