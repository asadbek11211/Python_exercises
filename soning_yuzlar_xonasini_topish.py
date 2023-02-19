# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:54:33 2023
 masalaning qo'yilishi:
     999 dan katta bo'lgan son berilgan. Bir marta bo'lib butunini va bo'lib qoldiqini olish
     operatsiyasidan foydalanib berilgan sonni yuzlar xonasidagi sonni aniqlovchi pragramma tuzilsiz
"""
son = int(input("999 dan katta bo'lgan son kiriting : "))

son1 = int(son/100)

son2 = son1%10

print(f"{son} sonining yuzlar xonasidagi soni : {son2} ga teng")