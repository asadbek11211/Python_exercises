# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:40:15 2023

Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni 
          lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
"""

ilm_fan = {
    
    'ismi':'Anvar',
    'familiya':'Narzullayev',
    'kasbi':'IA mutahasis',
    'yutuqlari':"Mohirdev.uz platfo'rmasi"
    
          }
sanat = {
    
    'ismi':'Ozodbek',
    'familiya':'Nazarboyev',
    'kasbi':'Halq artisti',
    'yutuqlari':"yuzlagan qo'shiqlar to'plami"
    
    }

internet = {
    
    'ismi':'Bil',
    'familiya':'Gayts',
    'kasbi':'Pragrammis',
    'yutuqlari':"Micrasoft konponiyasi"
    
    }


sport = {
    
    'ismi':'Tyson',
    'familiya':'Mike',
    'kasbi':'Prafessional bokschi',
    'yutuqlari':"20 yil davomida chempion"
    
    }

mashhurlar = [ilm_fan, sanat, internet, sport]

for lugat in mashhurlar:
    print(f"{lugat['familiya'].title()} {lugat['ismi'].title()} {lugat['kasbi'].title()} yutug'i {lugat['yutuqlari']}")








