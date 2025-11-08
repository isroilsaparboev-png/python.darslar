#1 - masala
ismlar = ["Ali", "Vali", "Hasan", "Husan", "Olim"]

for ism in ismlar:
    print(f"Salom, {ism}! Bugun qalaysan?")
    
    
    
    
#2 - masala
print(f"Kod {len(ismlar)} marta takrorlandi")


toq_sonlar = list(range(11, 100, 2))

for son in toq_sonlar:
    print(f"{son} ning kubi {son**3} ga teng")
    
    
    
    
    
#3 - masala
    kinolar = []

for i in range(5):
    kino = input(f"{i+1}-sevimli filmingizni kiriting: ")
    kinolar.append(kino)

print("Sizning sevimli kinolaringiz:")
for kino in kinolar:
    print(kino)
    
    
    
    
#4 - masala
n = int(input("Bugun nechta odam bilan uchrashdingiz? "))

odamlar = []
for i in range(n):
    ism = input(f"{i+1}-odamning ismini kiriting: ")
    odamlar.append(ism)

print("Siz bugun uchrashgan odamlardan ba'zilari:")
for ism in odamlar:
    print(ism)
    
    
    
    
#5 - masala
# Foydalanuvchidan bugun nechta odam bilan uchrashganini so'raymiz
n = int(input("Bugun nechta odam bilan uchrashdingiz? "))

# Bo'sh ro'yxat yaratamiz
odamlar = []

# Har bir odamning ismini birma-bir so'raymiz
for i in range(n):
    ism = input(f"{i+1}-odamning ismini kiriting: ")
    odamlar.append(ism)

# Natijani konsolga chiqaramiz
print("Siz bugun uchrashgan odamlardan ba'zilari:")
for ism in odamlar:
    print(ism)

