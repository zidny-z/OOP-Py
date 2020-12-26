import sqlite3
con = sqlite3.connect('db/database.sqlite')
cursor = con.cursor()

# Query = "Insert into player(PlayerName,PlayerPassword,PlayerWeapon) Values('adminlagi','adminssaak','1')"
# # (\'%s\', \'%s\');'
# kueri = 'select * from player'
# cursor.execute(Query)
# con.commit()

nama = 'select PlayerName from player WHERE PlayerID=1'
cursor.execute(nama)
hasilnama = cursor.fetchone()
con.commit()
print(hasilnama[0])
