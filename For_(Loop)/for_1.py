# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 20:17:07 2023
Qudrat Abdullayev darsligidan

Masala sharti:
k va n butun sonlari berilgan (n > 0). k sonini n marta chiqaruvchi pragramma tuzing.
    
"""
print("k sonini n marta chiqarish dasturi")
k = int(input("k soniga biror qiymat kiriting : "))
n = int(input("n qiymatiga yana biror son kiriting : "))
j = 0

for son in range(1,n+1):
    j = j +1
    print(f"\n{j}-marta : {k}")