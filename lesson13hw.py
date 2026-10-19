mehsullar = {
    "laptop": 1800,
    "telefon": 1200,
    "monitor": 500,
    "mouse": 50
}


def sifaris_tarixcesini_goster():
    try:
        with open("orders.txt", "r", encoding="utf-8") as fayl:
            melumat = fayl.read()
    except FileNotFoundError:
        print("Hələ heç bir sifariş tarixçəsi yoxdur.")
    else:
        print("\n--- Sifariş tarixçəsi ---")
        print(melumat)


try:
    mehsul = input("Məhsul: ").strip().lower()
    qiymet = mehsullar[mehsul]
    miqdar_metn = input("Miqdar: ")
    try:
        miqdar = int(miqdar_metn)
    except ValueError:
        raise ValueError("Miqdar rəqəm olmalıdır.")

    if miqdar <= 0:
        raise ValueError("Miqdar 0-dan böyük olmalıdır.")

    umumi_qiymet = qiymet * miqdar

except KeyError:
    print("Belə məhsul mövcud deyil.")

except ValueError as xeta:
    print(xeta)

else:
    print("\nSifariş uğurla yaradıldı.")
    print(f"Məhsul: {mehsul}")
    print(f"Miqdar: {miqdar}")
    print(f"Ümumi qiymət: {umumi_qiymet} AZN")

    with open("orders.txt", "a", encoding="utf-8") as fayl:
        fayl.write(f"{mehsul},{miqdar},{umumi_qiymet}\n")

    sifaris_tarixcesini_goster()

finally:
    print("\nSifariş əməliyyatı tamamlandı.")