# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:15:23 2023
Asadbek Ro'ziboyev
Issue condition:
     Ask the user to enter two numbers,
     compare the numbers and find that they are equal or
     seniority/minority notification software
"""


number = []
n = 0
print("Enter two numbers ")
for a in range(2):
    n = n + 1
    number.append(input(f"{n}-number : "))
    
if number[0] > number[1]:
    print("\n The first number is greater than the second number")
elif number[0] < number[1]:
    print("\n The second number is greater than the first number")
else:
    print("\n The numbers equal")  
    
