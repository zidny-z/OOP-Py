import sqlite3
con = sqlite3.connect('db/database.sqlite')
cursor = con.cursor()


class Person:
    def __init__(self, p_nama, p_level, p_health, p_weapon):
        self.nama = p_nama
        self.level = p_level
        self.health = p_health
        self.weapon = p_weapon

    def serang(self):
        pass


class Enemy(Person):
    def __init__(self, p_nama, p_level, p_health, p_weapon):
        super().__init__(p_nama, p_level, p_health, p_weapon)

    def masukdatabase(self):
        q_enemydb = 'INSERT INTO ENEMY(EnemyName, EnemyLevel, EnemyHealth, EnemyWeapon) VALUES (\'%s\', \'%s\', \'%s\', \'%s\');'
        q_enemydb = q_enemydb % (self.nama, self.level, self.health,
                                 self.weapon)
        cursor.execute(q_enemydb)
        con.commit()


class Player(Person):
    def __init__(self,
                 p_nama=None,
                 p_level=1,
                 p_health=100,
                 p_weapon=None,
                 p_score=0,
                 p_energy=0,
                 p_exp=0):
        super().__init__(p_nama, p_level, p_health, p_weapon)
        self.score = p_score
        self.energy = p_energy
        self.exp = p_exp

    def masukdatabase(self):
        q_playerdb = 'INSERT INTO Player(PlayerName,PlayerWeapon) VALUES (\'%s\', \'%s\');'
        q_playerdb = q_playerdb % (self.nama, self.weapon)
        cursor.execute(q_playerdb)
        con.commit()


# kucingutan = Enemy('kucingutan', 1, 100, 2)
# kucingutan.masukdatabase()

admin3 = Player(p_nama='admin3', p_weapon=1)
admin3.masukdatabase()