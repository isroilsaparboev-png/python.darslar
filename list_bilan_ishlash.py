# 1. O'zingizga ma'lum davlatlarning ro'yxatini tuzing
davlatlar = ["O'zbekiston", "AQSh", "Rossiya", "Turkiya", "Xitoy", "Janubiy Koreya", "Fransiya", "Germaniya"]
print("Davlatlar ro'yxati:", davlatlar)

# 2. Ro'yxatning uzunligini konsolga chiqaring
print("Ro'yxat uzunligi:", len(davlatlar))

# 3. sorted() yordamida tartiblangan ro'yxat
print("Tartiblangan ro'yxat:", sorted(davlatlar))
        
# 4. sorted() yordamida teskari tartibda ro'yxat
print("Teskari tartiblangan ro'yxat:", sorted(davlatlar, reverse=True))

# 5. Asl ro'yxatni qaytadan konsolga chiqaring
print("Asl ro'yxat:", davlatlar)

# 6. reverse() metodi yordamida ro'yxatni teskari o'zgartirish
davlatlar.reverse()
print("Teskari qilib o'zgartirilgan ro'yxat:", davlatlar)

# 7. sort() yordamida alifbo bo'yicha va teskari tartibda
davlatlar.sort()
print("Alifbo bo'yicha tartiblangan:", davlatlar)
davlatlar.sort(reverse=True)
print("Alifboga teskari tartib:", davlatlar)

# 8. 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzish
juft_sonlar = list(range(120, 1201, 2))
print("Juft sonlar:", juft_sonlar)

# 9. Ro'yxatdagi sonlar yig'indisini hisoblash
print("Juft sonlar yig'indisi:", sum(juft_sonlar))

# 10. Eng katta va eng kichik sonlar ayirmasi
ayirma = max(juft_sonlar) - min(juft_sonlar)
print("Eng katta va eng kichik son ayirmasi:", ayirma)

# 11. Elementlar soni
print("Elementlar soni:", len(juft_sonlar))

# 12. Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymat
print("Boshidan 20 ta:", juft_sonlar[:20])
print("O'rtasidan 20 ta:", juft_sonlar[len(juft_sonlar)//2 : len(juft_sonlar)//2 + 20])
print("Oxiridan 20 ta:", juft_sonlar[-20:])

# 13. taomlar ro'yxati
taomlar = ["osh", "sho'rva", "manti", "somsa", "shashlik"]
print("Taomlar:", taomlar)

# 14. nonushta ro'yxati (nusxa olish)
nonushta = taomlar[:]

# 15. Faqat nonushtalik taomlarni qoldirish va 2 ta qo'shish
nonushta.append("tuxum")
nonushta.append("qaynatilgan sut")

# 16. Ikkala ro'yxatni konsolga chiqaring
print("Asl taomlar:", taomlar)
print("Nonushta ro'yxati:", nonushta)

# 17. Nonushta ro'yxatini o'zgarmas ro'yxat (tuple) ga aylantirish
nonushta = tuple(nonushta)
print("O'zgarmas nonushta ro'yxati:", nonushta)

# 18. Tuple elementini o'zgartirishga urinish
try:
    nonushta[0] = "qaymoq va non"
except TypeError:
    print("Xatolik: Tuple (o'zgarmas ro'yxat) elementlarini o'zgartirib bo'lmaydi!")

