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

class Enemy:
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM enemy WHERE EnemyID=1")
    hasil = mycursor.fetchall()

    def __init__(self, id):
        self.id = Enemy.hasil[0][0]
        self.nama = Enemy.hasil[0][1]
        self.power = Enemy.hasil[0][2]
        self.armor = Enemy.hasil[0][3]
        self.level = Enemy.hasil[0][4]
        self.health = Enemy.hasil[0][5]

    # def serang:
    #     pass
satu = Enemy(1)    
print(satu.health)
# class Player:


