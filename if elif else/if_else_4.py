# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 18:28:46 2023
created by Asadbek ro'ziboyev
Masalaning qo'yilishi:
    mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
    Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
    Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
    aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
"""
mahsulotlar = ["anor","uzum","anjir","olma","gilos","o'rik","nashvoti","qulupnay","ananas","behi"]

savat = []

print(f"{mahsulotlar} \n Savatga kamida 5 ta mahsulot kiriting\ n")

n = int(input("Nechta mahsulot olmoqchisiz : "))

for a in range(n):
    
    savat.append(input(f"{a+1}-mahsulotni kiriting : "))

for b in savat:

    if b in mahsulotlar:
        print(f"{b} mahsuloti do'konimizda bor")
    else:
        print(f"{b} mahsuloti do'konimizda yo'q")
