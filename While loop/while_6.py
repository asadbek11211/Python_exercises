# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:54:43 2023

Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
"""

#dasturning birinchi qismi

e_bozor = {
    
    'kitoblar': 12_000,
    'kiyimlar': 340_000,
    'mashina': 30_200_000,
    'elektronika': 200_000,
    'mayishiy_texnika': 89_000,
    'mebellar': 2_000_000,
    'oshxona buyumlari': 100_000
    
    }

buyurtmalar = []
n = 0
ishora = True
print("Foydalanuvchidan buyurtma qabul qiluvchi dastur")

while ishora :
    buyurtma = input(f"{n+1}-buyurtmangizni kiriting(dasturni tugatish uchin 'exit') : ")
    if buyurtma == 'exit':
        ishora = False
    else:
        buyurtmalar.append(buyurtma)
        n += 1

for kalit, info in e_bozor.items():
    if kalit in buyurtmalar:
        print(f"{kalit.title()}ning narhi {info}")
    else:
        print("Bizda bu mahsulot yo'q")

 
  
  
 
  
