import sqlite3
con = sqlite3.connect('database1.db')
cursor = con.cursor()
 
Query = "Insert into player(PlayerName,PlayerPassword,PlayerWeapon) Values('adminwksswk','adminsswkwk','1')"
# (\'%s\', \'%s\');'
cursor.execute(Query)
con.commit()
