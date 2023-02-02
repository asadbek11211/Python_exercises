# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:08:47 2023

Qudrat Abdullayev darsligidan

Masala sharti:
a va b butun sonlari berilgan(a < b). a va b sonlari orasidagi barcha butun sonlari
(a va b ni ham) chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi pragramma tuzilsin.
(a va b xam chiqarilsin)

"""
a = int(input("a qiymatiga biror butun son kiriting : "))
b = int(input("b soniga ham butun son kiriting \n (a < b) bo'lishi kerak : "))
butun = []

for m in range(a,b+1):
    butun.append(m)
print(f"\n a va b sonlari orasidagi barcha butun sonlari \n {butun}")

