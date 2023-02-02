# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 18:44:13 2023

Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
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
    print(f"\n {lugat['ismi'].title()}ning eng yaxshi yutug'i {lugat['yutuqlari']}")
    
    
    
    
