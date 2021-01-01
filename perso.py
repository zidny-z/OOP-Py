from tabulate import tabulate
from getpass import getpass
import mysql.connector
import random
import os

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
        
    # def serang:
    #     pass

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

print(hero4.nama)

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

print(weapon10.nama)

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

print(user1.nama)

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

print(musuh10.nama)


