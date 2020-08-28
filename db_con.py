import sqlite3


con = sqlite3.connect('db.db')
cursor = con.cursor()
print(cursor.execute('SELECT SALARY FROM employee').fetchone()[0][0])
con.close()

