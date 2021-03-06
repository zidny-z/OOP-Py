from tabulate import tabulate
from getpass import getpass
import mysql.connector
import random
import os

clear = lambda: os.system('cls')
pagar = str(48 * '#')
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="test"
)

class Hero:
     def __init__(self, idnya, nama, health, power, armor):
          self.id = idnya
          self.nama = nama
          self.health = health
          self.power = power
          self.armor = armor

class Weapon:
     def __init__(self, idnya , nama, power, critRate, critDamage):
          self.id = idnya
          self.nama = nama
          self.power = power
          self.critRate = critRate
          self.critDamage = critDamage

class Player:
     def __init__(self, idnya, nama, health, exp, level, hero, weapon):
          self.id = idnya
          self.nama = nama
          self.health = health
          self.exp = exp
          self.level = level
          self.hero = hero
          self.weapon = weapon
          

class Enemy:
     def __init__(self, idnya, nama, power, armor, level, health):
          self.id = idnya
          self.nama = nama
          self.power = power
          self.armor = armor
          self.level = level
          self.health = health
        

#--- Declare Hero ---#
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM hero")
hasil = mycursor.fetchall()
for i in range(len(hasil)):
     if i==0:
          hero1 = Hero(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==1:
          hero2 = Hero(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==2:
          hero3 = Hero(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==3:
          hero4 = Hero(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==4:
          hero5 = Hero(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])

#--- Declare Weapon ---#
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM weapon")
hasil = mycursor.fetchall()
for i in range(len(hasil)):
     if i==0:
          weapon1 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==1:
          weapon2 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==2:
          weapon3 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==3:
          weapon4 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==4:
          weapon5 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==5:
          weapon6 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==6:
          weapon7 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==7:
          weapon8 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==8:
          weapon9 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])
     elif i==9:
          weapon10 = Weapon(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4])


#--- Declare Player ---#
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM player")
hasil = mycursor.fetchall()
for i in range(len(hasil)):
     if i==0:
          user1 = Player(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5],hasil[i][6])
     elif i==1:
          user2 = Player(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5],hasil[i][6])
     elif i==2:
          user3 = Player(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5],hasil[i][6])
     elif i==3:
          user4 = Player(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5],hasil[i][6])
     elif i==4:
          user5 = Player(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5],hasil[i][6])


#--- Declare Enemy ---#
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM enemy")
hasil = mycursor.fetchall()
for i in range(len(hasil)):
     if i==0:
          musuh1 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==1:
          musuh2 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==2:
          musuh3 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==3:
          musuh4 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==4:
          musuh5 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==5:
          musuh6 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==6:
          musuh7 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==7:
          musuh8 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==8:
          musuh9 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])
     elif i==9:
          musuh10 = Enemy(hasil[i][0],hasil[i][1],hasil[i][2],hasil[i][3],hasil[i][4],hasil[i][5])


def dashboard():
         pass

def mulai():
    print('1. Login\n2. Daftar')
    pilihan= int(input('pilihan = '))
    try:
        if pilihan==1:
            login()
        elif pilihan==2:
            daftar()
        else:
            print("salah input")
            menu()
    except KeyboardInterrupt:
        print("salah input")
        menu()

def login():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM player")
    hasil = mycursor.fetchall()
    header = ['ID', 'Nama', 'Health', 'EXP', 'Level', 'Level','HeroID', 'WeaponID']
    print()
    print(tabulate(hasil, headers=header))
    tempId = []
    for i in range(len(hasil)):
        tempId.append(hasil[i][0])
    print(tempId)
    pilihan =  int(input('\nPilih ID = '))

def daftar():
    nama = str(input('\nNama = '))
    nama = nama.lower()
    print()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM hero")
    hasil = mycursor.fetchall()
    header = ['ID','Nama','Health','Power','Armor']
    print(tabulate(hasil, headers=header))
    pilihHero = int(input('\nPilih Hero = '))
    if pilihHero not in range(1,len(hasil)+1):
        print('salah input')
        menu()

    print()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM weapon")
    hasil = mycursor.fetchall()
    header = ['ID',"Nama","Power","CritRate", "CritDamage"]
    print(tabulate(hasil, headers=header))
    pilihSenjata = int(input('\nPilih Senjata = '))
    if pilihSenjata not in range(1,len(hasil)+1):
        print('salah input')
        menu()   

    try:
        sql= "INSERT INTO `player`(`PlayerName`, `PlayerHealth`, `PlayerEXP`, `PlayerLevel`, `PlayerHero`, `PlayerWeapon`) VALUES (%s, 100, 0, 1, %s, %s)"
        val = (nama, pilihHero, pilihSenjata)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Pendaftaran Berhasil")
        dashboard()

    except mysql.connector.Error as e:
        # print("c")
        # print(format(e))
        print(e)

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

class Lobby:
     def __init__(self, username):
          self.username = username
     
     print("Profil Anda")
     mycursor = mydb.cursor()
     mycursor.execute("SELECT * FROM Player Wehe heroID={}".format(username))
     hasil = mycursor.fetchall()
     header = ['ID', 'Nama', 'Health', 'EXP', 'Level', 'Level','HeroID', 'WeaponID']
     print()
     print(tabulate(hasil, headers=header))

