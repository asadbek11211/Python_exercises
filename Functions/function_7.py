# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 09:12:19 2023

Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, 
lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. 
Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
"""

def lugat_yoz(ism, familya, t_yil, yosh, t_joyi, telefon_raqami='None', el_manzil='None' ):
    lugatlar = {
        'ismi':ism,
        'familiyasi':familya,
        'tugilgan yili':t_yil,
        'yoshi':yosh,
        'tugulgan joy':t_joyi,
        'tel_raqami':telefon_raqami,
        'el_manzil': el_manzil
        }
    for kalit, info in lugatlar.items():
        print(f"{kalit} : {info}")



print(lugat_yoz('asadbek', 'roziboyev', 1999, 24, 'xonqa'))
    