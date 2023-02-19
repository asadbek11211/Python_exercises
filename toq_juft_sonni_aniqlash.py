# -*- coding: utf-8 -*-
"""
Spyder Editor
Asadbek Ro'ziboyev

Masala qo'yilishi:
    Foydalanuvchidan juft son kiritishini so'rang. Agar foydalanuvchi juftson
    kiritsa "Rahmat", toq son kiritsa "Siz toq son kiritdingiz degan natija chiqarsin"
"""

juft_son = int(input("Juft son kiriting : "))
qoldiq = juft_son % 2
if qoldiq == 0:
    print("Rahmat")
else:
    print("Siz juft son kiritmadingiz")
