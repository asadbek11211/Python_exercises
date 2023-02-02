
"""
Created on Sat Jan 21 19:07:14 2023

"""
# 1,2-masala Kamida 5 ta elementdan iborat isimlar degan ro'yhat tuzing
# va ro'yhatdagi har bir isimga takrorlanuvchi habar yozing
#Yuqoridagi sikl tugagach kod n marta bajarildi degan habar chiqaring

#ismlar = ['Anvar', 'Bobur', 'Ilhom', 'Asad']
#n = 0
#print(ismlar)
#for bek in ismlar:
  # n = n + 1
   #print(f"Siz {bek}bek siz")
#print(f"Sikl {n} marta bajarildi")  
 
 # 3-masala 10 dan 100 gacha bo'lgan toq sonlar ro'yhatini tuzing.
#Ro'yhatning har bir elementini kubini aniqlab ko'nsolga chiqaring

#son = list(range(11,100,2)) 
#kub = []  
#for list in son:
 #   kub.append(list**3)
#print(f"Toq sonlar ro'yhati \n {son} \n Shu sonlarning kubi \n {kub} \n")

# 4 - masala Foydalanuvchidan 5 ta eng sevimli kinosini kiritishini so'rang va kinlar 
#degan ro'yhatga saqlab oling Natijani ko'nsolga chiqaring

#kino = []
#print("Eng sevimli 5 ta kinongizni kiriting ")
#for n in range(5):
#    kino.append(input(f"{n+1} - kino : "))
#print(f"\n Kinolar ro'yhati \n {kino} \n ")

# 5-masala Foydalanuvchidan bugun nechta odam bilan uchrashganini so'rang va
#har bir suhbatlashgan insonni birma-bir sorab ro'yhatga yozing

n = int(input("Bugun nechta odam bilan uchrashdingiz : "))
print("Ular kimlar edi ? ")
ism = []

for k in range(n):
    ism.append(input(f"{k+1}-"))
print(ism)    
    
    