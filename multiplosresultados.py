import sqlite3

conexao = sqlite3.connect("bancoagenda.db")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM agenda")
resultado = cursor.fetchall()
for registro in resultado:
    print("Nome: %s\nTelefone: %s" % (registro))
cursor.close()
conexao.close()