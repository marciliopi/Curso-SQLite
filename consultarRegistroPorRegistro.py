import sqlite3

conexao = sqlite3.connect("bancoagenda.db")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM agenda")
while  True:
    resultado = cursor.fetchone()
    if resultado == None:
        break
    print("Nome: %s\nTelefone: %s" % (resultado))
cursor.close()
conexao.close()