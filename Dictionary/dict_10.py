# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:48:09 2023

Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
"""
dost_1 = {
    
    'ism':'Anvar',
    'kino-serial':['Osmon','Kurtlar vadisi','Afsungar']
        }
dost_2 = {
    
    'ism':'Bobur',
    'kino-serial':['Dunyo','Boburiylar','Afsungar','Inqilob']
    }

onam = {
        'ism':'Dilorom',
        'kino-serial':['Shaytanat','Saroy javohiri','Opas singilar']
        }

seriallar = [dost_1, dost_2, onam]

for a in seriallar:
    print(f"Lugat elementlari : {a.items()} \n")