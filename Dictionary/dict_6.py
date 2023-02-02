# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:21:13 2023

Foydalanuvchidan istalgan davlatni kiritishni so'rang  
va shu davlatning poytaxtini konsolga chiqaring. 
Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
"""
davlatlar = {'turkiya':'istanbul',"uzbekiston":'toshkent','Rassiya':'maskva','xitoy':'pekin'}

f = input("\n  Istalgan davlatingizni kiriting : ")


if f in davlatlar:
   
    print(f"{f}ning poytahti {davlatlar[f]}")
else:    
   print("Bizda bunday ma'lumot yo'q")

