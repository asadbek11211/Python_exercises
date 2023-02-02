# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 19:02:55 2023

X va Y sonlaridan kichigini X ga va kattasini Y ga yozuvchi minmax() finction hosil qilish

"""
print("X va Y sonlaridan kichigini X ga va kattasini Y ga yozuvchi minmax() finction")
def minmax(number1, number2):
    """X va Y sonlaridan kichigini X ga va kattasini Y ga yozuvchi minmax() finction"""
    if number1 < number2:
        x = number1
        y = number2
    
    print(f" X = {x},  Y = {y}")
    
    
print(minmax(4,2))