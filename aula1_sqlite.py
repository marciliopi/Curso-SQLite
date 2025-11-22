import sqlite3

banco = sqlite3.connect('primeiro_banco.db') #objeto de conecao com o DB

cursor = banco.cursor()

cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

cursor.execute("INSERT INTO pessoas VALUES('Maria', 40,'maria_123@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('Joao', 38,'joao_123@gmail.com')")
cursor.execute("INSERT INTO pessoas VALUES('jose', 45,'jose_123@gmail.com')")

cursor.execute("INSERT INTO pessoas VALUES('Tony', 30,'tony@gmail.com')")

banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())