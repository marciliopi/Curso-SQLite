import sqlite3

# criando o bando de dados
conexao = sqlite3.connect("bancoagenda.db") 

# criação do cursor(objeto usado para criar comamndos e receber reultados do Db)
cursor = conexao.cursor() 

# criando tabela agenda
#cursor.execute("CREATE TABLE agenda (nome text, telefone text)")

#inserindo dados na tabela agenda
#cursor.execute("INSERT INTO agenda VALUES('Nilo', '86988316771')")
cursor.execute("INSERT INTO agenda VALUES('Keila', '86988486747')")

conexao.commit()
cursor.close()
conexao.close()
