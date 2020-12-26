class persegi:
    def __init__(self, sisi=5, sisilagi=0):
        self.sisi = sisi

    def luas(self):
        print(self.sisi * self.sisilagi)


satu = persegi()
satu.luas()

dua = persegi(7)
dua.luas()