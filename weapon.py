import sqlite3
con = sqlite3.connect('db/database.sqlite')
cursor = con.cursor()


class weapon:
    def __init__(self, w_nama, w_power):
        self.w_nama = w_nama
        self.w_power = w_power

    def masukdatabase(self):
        q_weapondb = 'INSERT INTO WEAPON(WeaponName, WeaponPower)VALUES(\'%s\', \'%s\');'
        q_weapondb = q_weapondb % (self.w_nama, self.w_power)
        cursor.execute(q_weapondb)
        con.commit()


keris = weapon('catutkuku', 1)
keris.masukdatabase()
