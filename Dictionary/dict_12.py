# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:40:17 2023

foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
"""

Davlatlar = {
    
    'uzbekiston' : {
        
        'aholi_soni': '32000',
        'iqlimi': 'quruqlik'
        },
    
    'turkiya': {
        
        'aholi_soni': '80000',
        'iqlimi': 'quyoshli'
        },
    
    'rasiya': {
       
        'aholi_soni': '98000',
        'iqlimi': 'nam'
        }
        }
foydalanuvchi = input("\n Biror davlat nomini kiriting : ")


for davlat, info in Davlatlar.items():
    
    if foydalanuvchi == davlat:
       print(f"{davlat.title()}ning aholi soni {info['aholi_soni']}, Iqlimi {info['iqlimi']}")
print("\n Bizda bu davlat haqida ma'lumot yo'q")