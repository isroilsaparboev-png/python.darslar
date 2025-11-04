# 1. Davlatlar ro'yxatini tuzamiz
davlatlar = ["O'zbekiston", "Qozog'iston", "Turkiya", "Rossiya", "AQSh", "Yaponiya", "Germaniya"]
print("Davlatlar ro'yxati:", davlatlar)

# 2. Ro'yxat uzunligini chiqaramiz
print("Ro'yxat uzunligi:", len(davlatlar))

# 3. sorted() yordamida tartiblangan ro'yxat
print("Tartiblangan ro'yxat:", sorted(davlatlar))

# 4. sorted() yordamida teskari tartibda
print("Teskari tartibda:", sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qaytadan chiqaramiz
print("Asl ro'yxat:", davlatlar)

# 6. reverse() yordamida ro'yxatni teskari chiqaramiz
davlatlar.reverse()
print("reverse() dan keyin:", davlatlar)

# 7. sort() yordamida alifbo bo'yicha va teskari tartibda
davlatlar.sort()
print("sort() - alifbo bo'yicha:", davlatlar)

davlatlar.sort(reverse=True)
print("sort() - teskari tartibda:", davlatlar)



