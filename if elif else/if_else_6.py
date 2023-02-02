# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:21:46 2023

created by Asadbek ro'ziboyev
Masalaning qo'yilishi:
    foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
    Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning 
    tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
    aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
"""
Foydalanuvchi = ["asadulloh1121","mohirdev_big","big_feature_","olimboy1334","gulhayo_dev8877","anvar_narz"]

login = input("Yangi login kiriting : ")

if login.lower() in Foydalanuvchi:
    print(f"{login} logini band, yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")


