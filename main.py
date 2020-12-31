import os
import mysql.connector
import random
from tabulate import tabulate

clear = lambda: os.system('cls')
pagar = str(48 * '#')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="test"
)

def mulai():
    print('1. Login\n2. Daftar')
    pilihan= int(input('pilihan = '))
    try:
        if pilihan==1:
            login()
        elif pilihan==2:
            daftar()
    except:
        pass

def login():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM player")
    hasil = mycursor.fetchall()
    header = ['ID', 'Nama', 'Health', 'EXP', 'Level', 'Level','HeroID', 'WeaponID']
    print()
    print(tabulate(hasil, headers=header))
    pilihan =  int(input('\nPilihan = '))

def daftar():
    nama = str(input('\nNama = '))
    print()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM hero")
    hasil = mycursor.fetchall()
    header = ['ID','Nama','Health','Power','Armor']
    print(tabulate(hasil, headers=header))
    pilihHero = int(input('\nPilih Hero = '))
    if pilihHero not in range(len(hasil)):
        print('salah input')
        menu()

    print()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM weapon")
    hasil = mycursor.fetchall()
    header = ['ID',"Nama","Power","CritRate", "CritDamage"]
    print(tabulate(hasil, headers=header))
    pilihSenjata = int(input('\nPilih Senjata = '))



def menu():
    print("\n" + pagar + "\n\t\tThe Geluds Game\n" + pagar +
          "\n1. Mulai\n2. Cara Main\n3. Tentang Game\n4. Keluar")
    pilihan = int(input("Pilihan = "))
    if pilihan == 1:
        clear()
        mulai()
    elif pilihan == 2:
        clear()
        print(pagar + "\n\t\tCara Main\n" + pagar+"\nCara Memainkan Game ini ialah dengan cara menekan pilihan sesuai yang ada.")
        kembali = input('\nTekan enter untuk kembali')
        clear()
        menu()
    elif pilihan == 3:
        clear()
        print(pagar + "\n\t\tThe Geluds Game\n" + pagar+ "\nGame ini dikembangankan menggunakan bahasa pemograman Python 3 selangkapnya bisa dilihat di www.github.com/zidny-z")
        kembali = input('\nTekan enter untuk kembali')
        clear()
        menu()
    elif pilihan == 4:
        clear()
        exit()

# while True:
menu()