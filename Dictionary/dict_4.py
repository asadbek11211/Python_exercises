# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 23:58:14 2023

Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida 
chiroyli qilib konsolga chiqaring.
"""

talabalar = {
    
    'anvar':'2-kursda oqiydi',
    'bobur':'3-kursda oqiydi',
    'kamol':'1-kursda oqiydi',
    'sodiq':'4-kursda oqiydi',
    'ilhom':'4-kursda oqiydi',
    'shohruh':'3-kursda oqiydi',
    'gulhayo':'4-kursda oqiydi',
    'asadbek':'2-kursda oqiydi'
            }

for k, q in sorted(talabalar.items()):
    
    print(f"Kalit : {k}")
    print(f"Qiymat : {q}")