# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:48:08 2023

2 ta sonning o'rta arfimetigi, va o'rta grometirikini aniqlovchi function yaratish

"""
import math
def arf_geyometirik(son1, son2):
    """2 ta sonning o'rta arfimetigi, va o'rta grometirikini aniqlovchi function"""

    arf = (son1 + son2) / 2
    geyometrik = math.sqrt(son1 * son2)
    
    natija1 = f"{son1} va {son2} ning o'rta arfimetirigi {arf} teng"
    natija2 = f"{son1} va {son2} ning o'rta geometirigi {geyometrik} teng"
    
    return natija1, natija2