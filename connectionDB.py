import mysql.connector, os

class connection:
    def __init__(self):
        try:
            self.__con = mysql.connector.connect(
            host="localhost",
            user="root",
            database="the geluds game"
            )
            self.__cursor = self.__con.cursor()
            
        except mysql.connector.Error as e:
            View.errors(e)

     def displayProfil():
          print("\n" + pagar + "\n\t\tSelamat Datang!\n" + pagar+"\n\nProfil Anda")
          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM player")
          hasil = mycursor.fetchall()
          header = ['ID', 'Nama Anda', 'Health', 'Level','HeroID', 'WeaponID']
          print()
          print(tabulate(hasil, headers=header))

          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM Hero Where HeroID={}".format(myplayer.hero))
          hasil = mycursor.fetchall()
          header = ['ID','Nama Hero','Health','Power','Armor']
          print()
          print(tabulate(hasil, headers=header))

          mycursor = mydb.cursor()
          mycursor.execute("SELECT * FROM Weapon Where WeaponID={}".format(myplayer.weapon))
          hasil = mycursor.fetchall()
          header = ['ID',"Nama Senjata","Power","CritRate", "CritDamage"]
          print()
          print(tabulate(hasil, headers=header))
