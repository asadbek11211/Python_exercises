# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 00:07:34 2023

Qudrat Abdurahimov masalalaridan
masala sharti:
    A va B butun soni berilgan (A < B). A va B sonlari orasidagi
    barcha butun sonlarni chiqaruvchi pragramma tuzilsin. 
    Bunda A soni 1 marta, (A + 1) soni 2 marta va xokozo
"""
A = int(input("A butun sonini kiriting (A < B) : "))
B = int(input("B butun sonini kiriting : "))


for a in range(A,B+1,1):
    for b in range(a):
        print(a)