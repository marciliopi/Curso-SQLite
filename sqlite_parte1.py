import sqlite3

try:
    banco = sqlite3.connect('primeiro_banco.db') #objeto de conecao com o DB

    cursor = banco.cursor()


    cursor.execute("DELETE FROM pessoas WHERE idade = 45")

    banco.commit()
    banco.close()
    print("Os dados foram removidos com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao excluir: ",erro)
