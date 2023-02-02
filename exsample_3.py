# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 22:46:41 2023

@author: Lenovo
"""

# K soni 0-365 oraliqida yotuvchi yil kunlaridan biri
# 1-yanvar yakshanba bo'lsa kiritilgan K haftaning qaysi kuni ekanligini aniqlovchi dastur
# 0- yakshanba, 1- dushanba, 2- seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba
K = int(input("0-365 oraliqidan ixtiyoriy butun son kiriting : "))
# =============================================================================
# dushanba = 1
# seshanba = 2
# chorshanba = 3
# payshanba = 4
# juma = 5
# shanba = 6
# yakshanba = 7
# =============================================================================

haftaKunlari_raqmlarda = [0,1,2,3,4,5,6]
haftaKunlari_yozuvda = ['Yakshanba', 'Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']

kun = (K % 7)-1
indexx = haftaKunlari_raqmlarda.index(kun)
print(f"Yilning {K} - kun haftaning {haftaKunlari_yozuvda[indexx]} - kuniga to'gri keladi!")

