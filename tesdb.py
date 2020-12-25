import sqlite3
con = sqlite3.connect('database1.db')
cursor = con.cursor()
 
Query = "Insert into player(PlayerName,PlayerPassword,PlayerWeapon) Values('adminwkwk','adminwkwk','1')"
# (\'%s\', \'%s\');'
# Query = Query  % ('admin', 'admin')
cursor.execute(Query)
con.commit()
