kitoblar = []

while True:
    nom = input("Yaxshi ko'rgan kitobingizni kiriting (to'xtatish uchun 'stop' yozing): ")

    if nom.lower() == "stop":
        break
    
    kitoblar.append(nom)

print("\nSiz kiritgan kitoblar:")
for k in kitoblar:
    print("-", k)
while True:
    yosh = input("Yoshingizni kiriting (yoki 'exit'/'quit' deb yozing): ")

    # Dasturdan chiqish sharti
    if yosh.lower() == 'exit' or yosh.lower() == 'quit':
        print("Dastur tugadi.")
        break

    # Kiritilgan qiymatni sondan iboratligini tekshiramiz
    if not yosh.isdigit():
        print("Iltimos, yoshni raqam bilan kiriting!")
        continue

    yosh = int(yosh)

    # Chipta narhini aniqlash
    if yosh < 7:
        narx = 2000
    elif 7 <= yosh < 18:
        narx = 3000
    elif 18 <= yosh < 65:
        narx = 10000
    else:
        narx = 0  # 65 dan katta — bepul

    if narx == 0:
        print("Sizga chipta bepul!")
    else:
        print(f"Chipta narxi: {narx} so'm")
