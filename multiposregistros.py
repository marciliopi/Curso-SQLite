import sqlite3

dados = [("Joao", "98901-0109"),
         ("Andre", "98902-8900"),
         ("Maria", "97891-3321")]
conexao = sqlite3.connect("bancoagenda.db")
cursor = conexao.cursor()
cursor.executemany('''INSERT INTO agenda (nome, telefone) VALUES(?, ?)''', dados)
conexao.commit()
cursor.close()
conexao.close()