# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:07:14 2023

Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
Har bir davlat haqida ma'lumotni konsolga chiqaring.
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
    
    'rassiya': {
       
        'aholi_soni': '98000',
        'iqlimi': 'nam'
        }
        }

for davlat, info in Davlatlar.items():
    davlat = davlat.capitalize()
    print(f"\n {davlat} davlatining aholi soni {info['aholi_soni']}, Iqlimi esa {info['iqlimi']}")
        

