# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 01:00:43 2023

Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
"""

menyular_r = { 
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000,
    'shashlik':15000,
    'lagmon':24000,
    'osh':30000,
    'shourma':12000
        }
print("\n  3 ta ovqat buyurtma bering  \n")
buyurtma = []
for a in range(3):
    buyurtma.append(input(f"\n {a+1}-buyurtmani kiriting : "))

for b in buyurtma:
    if b in menyular_r:
        print(f"\n {b}ning narxi : {menyular_r[b]}")
    else:
        print(f"bizda {b} yo'q")