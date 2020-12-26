import sqlite3
con = sqlite3.connect('database1.db')
cursor = con.cursor()


class weapon:
    def __init__(self, w_nama, w_attack):
        self.w_nama = w_nama
        self.w_attack = w_attack

    def masukdatabase(self):
        q_weapondb = 'INSERT INTO WEAPON(WeaponName, WeaponAttack)VALUES(\'%s\', \'%s\');'
        q_weapondb = q_weapondb % (self.w_nama, self.w_attack)
        cursor.execute(q_weapondb)
        con.commit()


keris = weapon('catutkuku', 1)
keris.masukdatabase()
