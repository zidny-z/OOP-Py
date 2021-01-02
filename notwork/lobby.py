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