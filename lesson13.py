try:
    yas = int(input("Yasinizi daxil edin: "))
    ad = input("Adinizi daxil edin: ")

    if yas < 0:
       raise ValueError("Yas menfi eded ola bilmez!")

    with open("users.txt","a",encoding="utf-8") as file:
        file.write(f"Yas: {yas}\n")
        file.write(f"Ad: {ad}\n")
        
except ValueError as error:
    print(f"Xeta: {error}")

except FileNotFoundError:
    print("Users.txt fayli tapilmadi.")

else:
    print("Istifadeci ugurla qeydiyyatdan kecdi!")
    print(f"Yas: {yas}")
    print(f"Ad: {ad}")

finally:
    print("Proqram basa catdi!")

