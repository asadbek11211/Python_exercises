# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 00:06:34 2023

max qiymat
"""

son = list(range(0,20,2))

print(max(son))
print(min(son))
print(sum(son))

# ro'yhatni kesib olish

print(son[0:5])
print(son[3:])

# ro'yhatdan nusha olish

son1 = son[:]
son1.remove(12)
print(son1)