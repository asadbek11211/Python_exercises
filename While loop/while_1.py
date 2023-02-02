# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:13:28 2023

Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
"""
print("\n  Yaxshi ko'rgan kitoblaringizni kiriting")
n = 0
list = []
while True :
    n += 1
    kitob = input(f"{n}-kitobingizni kiriting : " )
    sikl = input("Yana kitob kiritmoqchimisiz (ha/yo'q) : ")
    list.append(kitob)
    
    if sikl == "yo'q":
        break
print("\n  Foydalanuvchi yaxshi ko'rgan kitoblar ro'yhati")
for a in list:
    print(a)