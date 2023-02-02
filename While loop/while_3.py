# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:59:53 2023

Kiritilgan sonning ildizini qaytaruvchi dastur.
"""

print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat < '0':
        continue
    elif qiymat =='exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Byebye")