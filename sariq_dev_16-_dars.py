shaxslar = [
    {"ism": "Alisher Navoiy", "soha": "adabiyot", "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub ul-Qulub"]},
    {"ism": "Leonardo da Vinci", "soha": "san'at", "asarlar": ["Mona Liza", "Oxirgi Oziq", "Vitruvian Man"]},
    {"ism": "Isaac Newton", "soha": "ilm-fan", "asarlar": ["Matematika asoslari", "Optika"]},
    {"ism": "Mark Zuckerberg", "soha": "internet", "asarlar": ["Facebook platformasi", "Meta konsepsiyasi"]}
]

for shaxs in shaxslar:
    print(f"{shaxs['ism']} – {shaxs['soha']} sohasidagi mashhur shaxs.")
for shaxs in shaxslar:
    print(f"\n{shaxs['ism']}ning mashhur asarlari:")
    for asar in shaxs['asarlar']:
        print(f" - {asar}")
kinolar = {
    "Ali": ["Interstellar", "Matrix", "Avatar"],
    "Dilshod": ["Breaking Bad", "El Camino", "Better Call Saul"],
    "Laylo": ["Harry Potter", "Narnia", "The Lord of the Rings"]
}

for dost, kino in kinolar.items():
    print(f"\n{dost}ning sevimli kinolari:")
    for k in kino:
        print(f" - {k}")
kinolar = {
    "Ali": ["Interstellar", "Matrix", "Avatar"],
    "Dilshod": ["Breaking Bad", "El Camino", "Better Call Saul"],
    "Laylo": ["Harry Potter", "Narnia", "The Lord of the Rings"]
}

for dost, kino in kinolar.items():
    print(f"\n{dost}ning sevimli kinolari:")
    for k in kino:
        print(f" - {k}")
davlatlar = {
    "Uzbekistan": {"poytaxt": "Toshkent", "hududi": "448,978 km²", "aholi": "36 million"},
    "Japan": {"poytaxt": "Tokyo", "hududi": "377,975 km²", "aholi": "125 million"},
    "USA": {"poytaxt": "Washington", "hududi": "9,833,520 km²", "aholi": "340 million"}
}

for nom, malumot in davlatlar.items():
    print(f"\n{nom}:")
    print(f" Poytaxt: {malumot['poytaxt']}")
    print(f" Hududi: {malumot['hududi']}")
    print(f" Aholisi: {malumot['aholi']}")
davlatlar = {
    "Uzbekistan": {"poytaxt": "Toshkent", "hududi": "448,978 km²", "aholi": "36 million"},
    "Japan": {"poytaxt": "Tokyo", "hududi": "377,975 km²", "aholi": "125 million"},
    "USA": {"poytaxt": "Washington", "hududi": "9,833,520 km²", "aholi": "340 million"}
}

for nom, malumot in davlatlar.items():
    print(f"\n{nom}:")
    print(f" Poytaxt: {malumot['poytaxt']}")
    print(f" Hududi: {malumot['hududi']}")
    print(f" Aholisi: {malumot['aholi']}")
davlat = input("Qaysi davlat haqida ma'lumot kerak? ")

if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat} haqida ma'lumot:")
    print(f" Poytaxt: {info['poytaxt']}")
    print(f" Hududi: {info['hududi']}")
    print(f" Aholisi: {info['aholi']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")
