# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:41:06 2023

Qudrat Abdurahimov darsligidan
masala qo'yilishi:
    n butun soni berilgan (n > 0). Quyidagi yigindini hisoblovchi 
    pragramma yarating
    S = n*2 + (n+1)*2 + (n+2)*2 + ...(2*n)*2

"""
print("S = n*2 + (n+1)*2 + (n+2)*2 + ...(2*n)*2 yig'indini aniqlash dasturi")
n = int(input("n ga butun son kiriting (n > 0) : "))
yigindi = 0
for S in range(n,(2*n+1),1):
    yigindi = yigindi + (S**2)
print(f"S = {yigindi}")

