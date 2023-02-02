# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:33:58 2023

Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
"""
print("Muzeyga kirish yoshga qarab narhlanadi \n")


while True:
    yosh = int(input("\n  Yoshni kiriting : "))
    
    if 0 < yosh < 7 :
        narh = "2_000 so'm"
    elif 7 <= yosh < 18 :
        narh = "3_000 so'm"
    elif 18 <= yosh < 65 :
        narh = "10_000 so'm"
    else:
        narh = 'bepul'
    print(f"Bu yoshdagilar uchun muzeyga kirish narhi {narh}")
    sikl = input("Boshqa yoshdagi narxlarni bilishni xohlaysizmi (ha / yo'q) : ")

    if sikl == "yo'q":
       break
print("Hayr omon bo'ling")