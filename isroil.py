# 1. Oila a'zolari haqida lug'at
otam = {
    "ism": "Mavlutdin",
    "tugilgan_yil": 1954,
    "shahar": "Samarqand"
}

onam = {
    "ism": "Gulbahor",
    "tugilgan_yil": 1960,
    "shahar": "Toshkent"
}

akam = {
    "ism": "Rustam",
    "tugilgan_yil": 1985,
    "shahar": "Samarqand"
}

# Lug'atdagi ma'lumotni matn shaklida chiqarish
print(f"Otamning ismi {otam['ism']}, {otam['tugilgan_yil']}-yilda, {otam['shahar']} shahrida tug'ilgan.")
print(f"Onamning ismi {onam['ism']}, {onam['tugilgan_yil']}-yilda, {onam['shahar']} shahrida tug'ilgan.")
print(f"Akamning ismi {akam['ism']}, {akam['tugilgan_yil']}-yilda, {akam['shahar']} shahrida tug'ilgan.")

print("\n" + "="*50 + "\n")

# 2. Oila a'zolarining sevimli taomlari
sevimli_taomlar = {
    "Ali": "osh",
    "Sara": "manti",
    "Olim": "shashlik",
    "Nodira": "lag'mon",
    "Rustam": "somsa"
}

# Kamida uch kishining sevimli taomini chiqarish
print(f"Alining sevimli taomi: {sevimli_taomlar['Ali']}")
print(f"Saraning sevimli taomi: {sevimli_taomlar['Sara']}")
print(f"Olimning sevimli taomi: {sevimli_taomlar['Olim']}")

print("\n" + "="*50 + "\n")

# 3. Python atamalarining izohli lug'ati
python_lugat = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "if": "Shartni tekshirish",
    "else": "Aks holda",
    "elif": "Boshqa shart",
    "list": "Ro'yxat",
    "dict": "Lug'at",
    "for": "Takrorlash tsikli",
    "while": "Shart asosida tsikl"
}

# Foydalanuvchidan so'z kiritishni so'raymiz
soz = input("Tarjimasini bilmoqchi bo'lgan Python atamasini kiriting: ")

# If-else orqali tekshirish va natijani chiqarish
if soz in python_lugat:
    print(f"{soz} so'zining tarjimasi: {python_lugat[soz]}")
else:
    print("Bunda so'z mavjud emas.")
