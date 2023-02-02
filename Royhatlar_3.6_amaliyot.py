
"""
Created on Thu Jan 19 13:06:51 2023
O'zingizga malum davlatlar ro'yhatini tuzing va ro'yhatni konsolga chiqaring

"""
#davlatlar = ["O'zbekiston", "Turkmaniston", "Qirgiziston", "Arabiston", "Turkiya"]

#print(davlatlar) 

# ro'yhatning uzunligi

#print("Ro'yhat uzunligi : " + str(len(davlatlar)))

# tartiblangan ro'yhat

#print("Tartiblangan ro'yhat : " + str(sorted(davlatlar)))

# Teskari tartibda saralash

#davlat1 = davlatlar[:]
#davlatlar.reverse()

#print(f"Teskari tartibda saralash {davlatlar}")
#print(f"Asl ro'yhat {davlat1}")

#davlatlar.sort(reverse=True)
#print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar

#a = list(range(120,1200))
#print(f"120 dan 1200 gacha bo'lgan sonlar ro'yhati \n {a}")
#max = max(a)
#min = min(a)
#len(a)


#print(f"120 dan 1200 sonlari yo'yhatidagi eng kata son {max} ga teng \n eng kichkinasi {min} ga teng \n ularning ayirmasi {max - min} ga teng")
#print("Elementlar soni : " + str(len(a)))


# Ro'yhatning boshidan, o'rtasidan, oxiridan 20 ta elementini chiqaring

a = list(range(120,1200))
bosh = a[:20]
orta = a[540:560]
oxiri = a[1060:]

print(f"Ro'yhatning boshidan 20 elementi \n {bosh} \n ")
print(f"Ro'yhatning o'rtasidan 20 elementi \n {orta} \n")
print(f"Ro'yhatning oxiridan 20 elementi \n {oxiri} \n")
