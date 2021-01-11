from tabulate import tabulate
import mysql.connector
import os
from classes import *
# from fight import *

clear = lambda: os.system('cls')
pagar = str(48 * '#')

class start:
     def __init__(self):
          try:
               self.mydb = mysql.connector.connect(
               host="localhost",
               user="root",
               database="the geluds game"
               )
               self.cursor = self.mydb.cursor()          
          except mysql.connector.Error as e:
               print(e)
          #mulai
          self.menu()

     def displayProfil(self):
          #pront profil sendiri
          print("\n" + pagar + "\n\t\tSelamat Datang!\n" + pagar+"\n\nProfil Anda")
          self.cursor.execute("SELECT * FROM player")
          hasil = self.cursor.fetchall()
          header = ['ID', 'Nama Anda', 'Health', 'Level','HeroID', 'WeaponID']
          self.myplayer = Player(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5])
          print("\n"+tabulate(hasil, headers=header))
          #print hero user
          self.cursor.execute("SELECT * FROM Hero Where HeroID={}".format(self.myplayer.getHero()))
          hasil = self.cursor.fetchall()
          header = ['ID','Nama Hero','Health','Power','Armor']
          self.myhero = Hero(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4])
          print("\n"+tabulate(hasil, headers=header))

          # print senjata user
          self.cursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(self.myplayer.getWeapon()))
          hasil = self.cursor.fetchall()
          header = ['ID',"Nama Senjata","Power"]
          self.myweapon = Weapon(hasil[0][0],hasil[0][1],hasil[0][2])
          print("\n"+tabulate(hasil, headers=header))
          
          return self.myplayer, self.myweapon, self.myhero

     def displayMusuh(self):
          # inisilisasi player
          self.cursor.execute("SELECT * FROM player")
          hasil = self.cursor.fetchall()
          header = ['ID', 'Nama Anda', 'Health', 'Level','HeroID', 'WeaponID']
          self.myplayer = Player(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5])

          #profil musuh
          self.cursor.execute("SELECT * FROM Enemy Where EnemyID={}".format(self.myplayer.level))
          hasil = self.cursor.fetchall()
          # print(hasil)
          header = ['ID',"Nama Musuh","Health","Level","Power","Armor", "Weapon"]
          self.myenemy = Enemy(hasil[0][0],hasil[0][1],hasil[0][2],hasil[0][3],hasil[0][4],hasil[0][5],hasil[0][6])
          print("\n\nProfil Musuh\n")
          print(tabulate(hasil, headers=header))


          #senjata musuh
          self.cursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(self.myplayer.weapon))
          hasil = self.cursor.fetchall()
          header = ['ID',"Nama Senjata Musuh","Power"]
          self.myenemyweapon = Weapon(hasil[0][0],hasil[0][1],hasil[0][2])
          print("\n"+tabulate(hasil, headers=header))
          return self.myenemyweapon, self.myplayer, self.myenemy

     def fight(self):
          print('\nPertarungan Dimulai !')
          myMainDamage = self.myhero.getPower() + self.myweapon.getPower()
          myMainHealth = self.myplayer.getHealth() + self.myhero.getHealth()
          myMainArmor = self.myhero.getArmor()

          eMainDamage = self.myenemyweapon.getPower() + self.myenemy.getPower()
          eMainHealth = self.myenemy.getHealth()
          eMainArmor = self.myenemy.getArmor()

          while myMainHealth>0 and eMainHealth>0:

               eMainHealth = eMainHealth - (myMainDamage - eMainArmor)
               if myMainHealth <= 0:
                    myMainHealth = 0
               elif eMainHealth <= 0:
                    eMainHealth = 0
               print("Anda Menyerang\nHP Musuh :",eMainHealth)

               myMainHealth = myMainHealth - (eMainDamage - myMainArmor)
               if myMainHealth <= 0:
                    myMainHealth = 0
               elif eMainHealth <= 0:
                    eMainHealth = 0
               print("Musuh Menyerang\nHP Anda :",myMainHealth)

               if myMainHealth <= 0:
                    myMainHealth = 0
                    print("\n" + pagar + "\n\t\tAnda Kalah :(\n" + pagar)
                    self.login()

               elif eMainHealth <= 0:
                    eMainHealth = 0
                    print("\n" + pagar + "\n\t\tAnda Menang!\n" + pagar)
                    self.nambahHP()
                    self.nambahLevel()
                    self.login()

     def nambahLevel(self):
          self.myplayer.level += 1
          if self.myplayer.level>=10 :
               self.myplayer.level = 1
               print(pagar+"\nSelamat Anda telah Menyelesaikan Game ini\n"+pagar)
          self.cursor.execute("UPDATE `player` SET `PlayerLevel`={} WHERE PlayerID=1".format(self.myplayer.level))
          self.mydb.commit()

     def nambahHP(self):
          self.myplayer.health += 20
          if self.myplayer.level>=10 :
               self.myplayer.health = 100
          print('nambah')
          self.cursor.execute("UPDATE `player` SET `PlayerHealth`= {} WHERE playerID=1".format(self.myplayer.health))
          self.mydb.commit()

     def login(self):
          self.displayProfil()
          print('\n1. Fight\n2. Menu\n')
          pilihan = input('Pilihan = ')
          if pilihan=="1":
               self.displayProfil()
               self.displayMusuh()
               self.fight()
          elif pilihan=="2":
               self.menu()
          else:
               print("salah input")

     def mulai(self):
          while True:
               print('1. Melanjutkan\n2. Mengulangi Kembali')
               pilihan = input('pilihan = ')
               if pilihan == "1":
                    self.login()
                    break
               elif pilihan == "2":
                    self.reset()
                    break
               else:
                    print("salah input menu")
                    self.menu()

     def reset(self):
          nama = str(input('\nNama = '))
          nama = nama.lower()
          print()

          self.cursor.execute("SELECT * FROM hero")
          hasil = self.cursor.fetchall()
          header = ['ID','Nama','Health','Power','Armor']
          print(tabulate(hasil, headers=header))
          pilihHero = int(input('\nPilih Hero = '))
          if pilihHero not in range(1,len(hasil)+1):
               print('salah input')
               self.menu()

          print()
          self.cursor.execute("SELECT * FROM weapon")
          hasil = self.cursor.fetchall()
          header = ['ID',"Nama","Power"]
          print(tabulate(hasil, headers=header))
          pilihSenjata = int(input('\nPilih Senjata = '))
          if pilihSenjata not in range(1,len(hasil)+1):
               print('salah input')
               self.menu()   

          try:
               sql= "UPDATE `player` SET `PlayerName`= %s,`PlayerHealth`= 100,`PlayerLevel`= 1,`PlayerHero`=%s,`PlayerWeapon`=%s"
               val = (nama, pilihHero, pilihSenjata)
               self.cursor.execute(sql, val)
               self.mydb.commit()
               print("Main Ulang Berhasil\nSilahkan login kembali")         
               clear() 

          except mysql.connector.Error:
               print("Salah Input")

     def menu(self):
          while True:
               try:
                    print("\n" + pagar + "\n\t\tThe Geluds Game\n" + pagar +"\n1. Mulai\n2. Cara Main\n3. Tentang Game\n4. Keluar")
                    pilihan = input("Pilihan = ")
                    
                    if pilihan == "1":
                         clear()
                         self.mulai()
                         break
                    elif pilihan == "2":
                         clear()
                         print(pagar + "\n\t\tCara Main\n" + pagar+"\nCara Memainkan Game ini ialah dengan cara menekan pilihan sesuai yang ada.")
                         kembali = input('\nTekan enter untuk kembali')
                         clear()
                         self.menu()
                         break
                    elif pilihan == "3":
                         clear()
                         print(pagar + "\n\t\tThe Geluds Game\n" + pagar+ "\nGame ini dikembangankan menggunakan bahasa pemograman Python 3 selangkapnya bisa dilihat di www.github.com/zidny-z")
                         kembali = input('\nTekan enter untuk kembali')
                         clear()
                         self.menu()
                         break
                    elif pilihan == "4":
                         clear()
                         exit()
                         break
                    else:
                         print("salah Input")
               except KeyboardInterrupt:
                    print("KeyboardInterrupt")
                    break


start()