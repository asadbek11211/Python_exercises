# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:25:53 2023

e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
"""
print("Bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dasturi")
savol = "Ismingizni kiriting : "
mahsulotlar = {}

while True:
    ism = input(savol)
    mahsulot = input(f"Salom {ism.title()} mahsulot turini kiriting(dasturni to'xtatish 'exit') : ")
    if mahsulot == 'exit':
        break
    else:
       mahsulotlar[ism] = mahsulot
print(mahsulotlar)
    

