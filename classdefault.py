class persegi:
    def __init__(self, sisi=5):
        self.sisi = sisi

    def luas(self):
        print(self.sisi * self.sisi)


satu = persegi()
satu.luas()

dua = persegi(7)
dua.luas()