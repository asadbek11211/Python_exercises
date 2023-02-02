# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 20:07:56 2023

Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
"""
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
print("Buyurtmalar ro'yhati")
k = 0
for a in buyurtmalar:
  k += 1
  print(f"{k} : {a}")  