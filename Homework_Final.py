"""
TAPŞIRIQ:
"Restoran Menyu və Sifariş Sistemi" hazırlayın.

Məqsəd:
İndiyə qədər keçdiyimiz Python mövzularını bir proqram daxilində birlikdə istifadə etmək.
 
     
İstifadə etməli olduğunuz mövzular:

- Variables və Data Types
- Operators
- if / elif / else
- for və while
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Functions
- input()
- Validation

Aşağıdakı restoran menyusu sizin üçün hazır verilib:

KATEQORIYALAR = (
    "Pizza",
    "Burger",
    "Salat",
    "İçki",
    "Desert"
)

menu = [
    {
        "ad": "Margherita Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 12.50,
        "movcuddur": True
    },
    {
        "ad": "Pepperoni Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 15.00,
        "movcuddur": True
    },
    {
        "ad": "Chicken Burger",
        "kateqoriya": "Burger",
        "qiymet": 9.50,
        "movcuddur": True
    },
    {
        "ad": "Cheeseburger",
        "kateqoriya": "Burger",
        "qiymet": 11.00,
        "movcuddur": False
    },
    {
        "ad": "Caesar Salat",
        "kateqoriya": "Salat",
        "qiymet": 8.50,
        "movcuddur": True
    },
    {
        "ad": "Cola",
        "kateqoriya": "İçki",
        "qiymet": 3.00,
        "movcuddur": True
    },
    {
        "ad": "Ayran",
        "kateqoriya": "İçki",
        "qiymet": 2.00,
        "movcuddur": True
    },
    {
        "ad": "Cheesecake",
        "kateqoriya": "Desert",
        "qiymet": 6.50,
        "movcuddur": True
    },
    {
        "ad": "Chocolate Cake",
        "kateqoriya": "Desert",
        "qiymet": 7.00,
        "movcuddur": False
    }
]

yorumlari silmeden hazir bunun icine kodu yaz ve mene ver burda verilen serte uyqun yaz
"""

KATEQORIYALAR = (
    "Pizza",
    "Burger",
    "Salat",
    "İçki",
    "Desert"
)

menu = [
    {
        "ad": "Margherita Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 12.50,
        "movcuddur": True
    },
    {
        "ad": "Pepperoni Pizza",
        "kateqoriya": "Pizza",
        "qiymet": 15.00,
        "movcuddur": True
    },
    {
        "ad": "Chicken Burger",
        "kateqoriya": "Burger",
        "qiymet": 9.50,
        "movcuddur": True
    },
    {
        "ad": "Cheeseburger",
        "kateqoriya": "Burger",
        "qiymet": 11.00,
        "movcuddur": False
    },
    {
        "ad": "Caesar Salat",
        "kateqoriya": "Salat",
        "qiymet": 8.50,
        "movcuddur": True
    },
    {
        "ad": "Cola",
        "kateqoriya": "İçki",
        "qiymet": 3.00,
        "movcuddur": True
    },
    {
        "ad": "Ayran",
        "kateqoriya": "İçki",
        "qiymet": 2.00,
        "movcuddur": True
    },
    {
        "ad": "Cheesecake",
        "kateqoriya": "Desert",
        "qiymet": 6.50,
        "movcuddur": True
    },
    {
        "ad": "Chocolate Cake",
        "kateqoriya": "Desert",
        "qiymet": 7.00,
        "movcuddur": False
    }
]



sifaris = []



while True:
    masa = input("Masa nömrəsi: ").strip()

    if masa.isdigit():
        masa = int(masa)

        if 1 <= masa <= 20:
            break
        else:
            print("Masa nömrəsi 1-20 arasında olmalıdır.")
    else:
        print("Yanlış masa nömrəsi.")



def menyunu_goster():
    print("MENYU")

    for mehsul in menu:
        if mehsul["movcuddur"] == True:
            print(
                mehsul["ad"],
                "|",
                mehsul["kateqoriya"],
                "|",
                f'{mehsul["qiymet"]:.2f} AZN'
            )



def yemek_axtar():
    axtaris = input("Axtarış: ").strip().lower()

    tapildi = False

    for mehsul in menu:
        if axtaris in mehsul["ad"].lower():
            print(
                mehsul["ad"],
                "|",
                mehsul["kateqoriya"],
                "|",
                f'{mehsul["qiymet"]:.2f} AZN'
            )

            tapildi = True

    if tapildi == False:
        print("Məhsul tapılmadı.")



def sifaris_elave_et():
    mehsul_adi = input("Məhsulun adı: ").strip().lower()

    tapilan_mehsul = None

    for mehsul in menu:
        if mehsul["ad"].lower() == mehsul_adi:
            tapilan_mehsul = mehsul
            break

    if tapilan_mehsul is None:
        print("Məhsul tapılmadı.")
        return

    if tapilan_mehsul["movcuddur"] == False:
        print("Məhsul hazırda mövcud deyil.")
        return

    while True:
        miqdar = input("Miqdar: ").strip()

        if miqdar.isdigit():
            miqdar = int(miqdar)

            if miqdar > 0:
                break

        print("Yanlış miqdar.")

    yeni_mehsul = {
        "ad": tapilan_mehsul["ad"],
        "qiymet": tapilan_mehsul["qiymet"],
        "miqdar": miqdar
    }

    sifaris.append(yeni_mehsul)

    print(f'{tapilan_mehsul["ad"]} sifarişə əlavə edildi.')



def sifarisi_goster():
    if len(sifaris) == 0:
        print("Sifariş boşdur.")
        return

    print(f"Masa: {masa}")
    print("SİFARİŞ")

    for mehsul in sifaris:
        umumi_qiymet = mehsul["qiymet"] * mehsul["miqdar"]

        print(f'\n{mehsul["ad"]}')
        print(
            f'{mehsul["miqdar"]} x '
            f'{mehsul["qiymet"]:.2f} AZN = '
            f'{umumi_qiymet:.2f} AZN'
        )

    umumi_meblegi_hesabla()



def umumi_meblegi_hesabla():
    if len(sifaris) == 0:
        print("Sifariş boşdur.")
        return

    ara_mebleg = 0

    for mehsul in sifaris:
        umumi_qiymet = mehsul["qiymet"] * mehsul["miqdar"]
        ara_mebleg += umumi_qiymet

    if ara_mebleg < 50:
        endirim = 0

    elif ara_mebleg < 100:
        endirim = ara_mebleg * 0.05

    else:
        endirim = ara_mebleg * 0.10

    yekun_mebleg = ara_mebleg - endirim

    print(f"\nAra məbləğ: {ara_mebleg:.2f} AZN")
    print(f"Endirim: {endirim:.2f} AZN")
    print(f"Yekun məbləğ: {yekun_mebleg:.2f} AZN")


\
def kateqoriyalari_goster():
    unikal_kateqoriyalar = set()

    for mehsul in menu:
        unikal_kateqoriyalar.add(mehsul["kateqoriya"])

    print("\nUnikal kateqoriyalar:")
    print(unikal_kateqoriyalar)



while True:
    print(" RESTORAN SİSTEMİ")
    print("1. Menyunu göstər")
    print("2. Yemək axtar")
    print("3. Sifariş əlavə et")
    print("4. Sifarişi göstər")
    print("5. Hesabı göstər")
    print("6. Çıxış")

    secim = input("Seçiminiz: ").strip()

    if secim == "1":
        menyunu_goster()

    elif secim == "2":
        yemek_axtar()

    elif secim == "3":
        sifaris_elave_et()

    elif secim == "4":
        sifarisi_goster()

    elif secim == "5":
        umumi_meblegi_hesabla()

    elif secim == "6":
        print("Proqram bağlandı.")
        break

    else:
        print("Yanlış seçim.")