import sqlite3

banco = sqlite3.connect('primeiro_banco.db') #objeto de conecao com o DB

cursor = banco.cursor()


cursor.execute("INSERT INTO pessoas VALUES('Tony', 30,'tony@gmail.com')")

banco.commit()

