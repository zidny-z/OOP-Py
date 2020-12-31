import os
clear = lambda: os.system('cls')
pagar = str(48 * '#')
import tesdb
print(tesdb.a)
print(tesdb.nama)


def mulai():
    def login():
        print("1. admin\n2. adminlagi")

    def daftar():
        nama = str(input('Nama = '))

    print("")
    pilihan = int(input('pilihan = '))
    if pilihan == 1:
        login()
    elif pilihan == 2:
        daftar()
    else:
        print('Intruksi tidak dikenali')


def menu():
    print("\n" + pagar + "\n\t\tThe Geluds Game\n" + pagar +
          "\n1. Mulai\n2. Cara Main\n3. Tentang Game\n4. Keluar")
    pilihan = int(input("Pilihan = "))
    if pilihan == 1:
        clear()
        mulai()
    elif pilihan == 2:
        clear()
        print(pagar + "\n\t\tCara Main\n" + pagar)
    elif pilihan == 3:
        clear()
        print(pagar + "\n\t\tThe Geluds Game\n" + pagar)
    elif pilihan == 4:
        clear()
        exit()


while True:
    clear()
    menu()