# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:35:03 2023
Asadbek Ro'ziboyev
masalaning qo'yilishi:
    Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
    Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga,
    do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
    "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar 
    do'konimizda yo'q: ....." degan xabarni chiqaring.
"""
mahsulotlar = ["anor","uzum","anjir","olma","gilos","o'rik","nashvoti","qulupnay","ananas","behi"]

haridor = []
bor_mahsulotlar = []
yoq_mahsulotlar = []

print(f"\n Bizning do'kondagi mahsulotlar ro'yhati \n {mahsulotlar} \n Iltimos  5 ta mahsulot kiriting  ")


for a in range(2):   
    haridor.append(input(f"{a+1}-mahsulotni kiriting : "))
    haridor[a] = haridor[a].lower()

for b in haridor:

    if b in mahsulotlar:
        bor_mahsulotlar.append(b)
    else:
        yoq_mahsulotlar.append(b)
        
if yoq_mahsulotlar:
    print(f"{yoq_mahsulotlar} mahsulotlar do'konimizda yo'q \n")
else:
    print("Siz so'ragan barcha mahsulotlari do'konimizda bor \n")


