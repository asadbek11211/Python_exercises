# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 12:24:08 2023
Asadbek Ro'ziboye tomonidan
Masalaning qo'yilishi:
    Foydalanuvchidan yoshini so'rang va muzeyga kirishi un chipta narxini quyidagicha so'rang.
    - Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan kata bo'lsa bepul
    - Agar foydalanuvchi 18 dan kichik bo'lsa, 10000 so'm.
    - Agar foydalanuvchi 18 dan katta bo'lsa, 20 000 so'm.
"""
yosh = int(input("Yoshingizni kiriting : "))

if yosh <= 4:
    print("Sizga kirish bepul")
elif yosh > 4 and yosh < 18:
    print("Sizga kirish 10 000 so'm")
elif yosh >= 18 and yosh < 60 :
    print("Sizga kirish 20 000 so'm")
else:
    print("Sizga kirish bepul")