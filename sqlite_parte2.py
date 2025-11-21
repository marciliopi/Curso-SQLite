import sqlite3

#passando as variáveis

nome = "Juliana"
idade = 28
email = "juliana@gmail.com"

banco = sqlite3.connect('primeiro_banco.db') #Objeto de conecao com o DB

cursor = banco.cursor()

cursor.execute("INSERT INTO pessoas VALUES('"+nome+"',"+str(idade)+",'"+email+"')")

banco.commit()