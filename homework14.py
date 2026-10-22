
class Telebe:
    tehsil_merkezi = "High Code"

    def __init__(self, ad, kurs, bal):
        if bal < 0 or bal > 100:
            raise ValueError("Bal 0 ilə 100 arasında olmalıdır.")

        self.ad = ad
        self.kurs = kurs
        self.bal = bal

    def melumat_goster(self):
        print(f"Ad: {self.ad}")
        print(f"Kurs: {self.kurs}")
        print(f"Bal: {self.bal}")

    def bal_artir(self, miqdar):
        if miqdar <= 0 or self.bal + miqdar > 100:
            return False

        self.bal += miqdar
        return True

    def ugurludur(self):
        return self.bal >= 51


telebe1 = Telebe("Ramin", "Python Backend", 45)
telebe2 = Telebe("Tural", "Python Backend", 90)

telebe1.melumat_goster()

print(telebe1.ugurludur())
print(telebe1.bal_artir(10))
print(telebe1.ugurludur())

print(telebe2.bal_artir(20))
print(telebe2.bal)

print(Telebe.tehsil_merkezi)

try:
    telebe3 = Telebe("Test", "Python Backend", -10)
except ValueError as xeta:
    print("Xəta:", xeta)
