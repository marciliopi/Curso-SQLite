import sqlite3

conexao = sqlite3.connect("bancoagenda.db")
cursor = conexao.cursor()
cursor.execute("SELECT * FROM agenda")
resultado = cursor.fetchone()
print("nome: %s\ntelefone: %s" % (resultado))
cursor.close()
conexao.close()