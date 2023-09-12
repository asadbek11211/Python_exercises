# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 02:56:31 2023
Amaliyot Class
@author: Lenovo
"""


# class Users:
#     def __init__(self,name,familiya,email):
#         self.name = name
#         self.familiya = familiya
#         self.email = email
        
#     def tanishtr(self):
#         print(f" {self.familiya} {self.name} elektron manzili {self.email}")
    

# user1 = Users('Asadbek', 'Roziboyev', 'roziboyev614@gmail')
# print(user1.name)
# user1.tanishtr()

class Transport:
    """Transport nomli class"""
    def __init__(self, model, name, ishlab_yil, rangi, pozitsiya, narxi):
        """Transfportning xususiyatlari"""
        self.model = model
        self.name = name
        self.yil = ishlab_yil
        self.color = rangi
        self.pozitsiya = pozitsiya
        self.price = narxi
    
    def get_model(self):
        print(self.model)
    
    def get_name(self):
        print(self.name)
    
    def get_year(self):
        print(self.yil)
    
    def get_color(self):
        print(self.color)
        
    def get_acursy(self):
        print(self.pozitsiya)
        
    def get_price(self):
        print(self.price)
        
    def get_info(self):
        print(f"{self.model} markali {self.name}. {self.yil}-yilda ishlab chiqarilgan, rangi {self.color} pozitsiyasi {self.pozitsiya}, narxi {self.price} $")


avto1 = Transport('Audi', 'Audi x5', '2000', 'oq', 'avtomat', '24 000')
avto2 = Transport('GM', 'Cobalt', '2023', 'qora', 'mexanik', '12 000')
avto3 = Transport('Tayota', 'Prado', '2023', 'Beliy', 'Gibrid', '23 000')

avto1.get_price()
avto1.get_model()

avto2.get_info()
avto2.get_name()

avto3.get_acursy()
avto3.get_year()


