# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 09:48:17 2023

Foydalanuvchi kiritgan sonning kvadratini va kubini ko'nsulga chiqarish dasturi'
"""
#a = input(f"Istalgan biror bir son kiriting : ")

#a = float(a)
#kvadrat = a * a
#kub = kvadrat * a

#print(f"{a} sonining kvadrati {kvadrat} ga teng kubi esa {kub} ga teng")

"""
Foydalanuvchining yoshini so'rab, uning tug'ulgan yilini hisoblab, konsolga chiqaruvchi dastur

"""

#yosh = input("Iltimos yoshingizni kiriting : ")

#yosh = int(yosh)
#a = 2023 - yosh

#print(f"siz {a} yilda tug'ulgansiz")

"""
Foydalanuvchidan ikki son kiritishini so'rab, kiritilgan yonlarning
yig'indisini,
ayirmasini,
ko'paytmasini,
bo'linmasini aniqlovchi dastur tuzing
"""
bir_son = float(input("Biror bir son kiriting : "))
ikki_son = float(input("Yana qandaydir son kiriting : "))

yigindi = bir_son + ikki_son
ayirma = bir_son - ikki_son
kopaytma = bir_son * ikki_son
bolinma = bir_son / ikki_son

print(f"{bir_son} va {ikki_son} ning \n yigindisi {yigindi} \n ayirmasi {ayirma} \n kopaytmasi {kopaytma} \n bolinmasi {bolinma} ga teng")
