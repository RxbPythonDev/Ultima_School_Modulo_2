import sqlite3

conexao = sqlite3.connect('Loja.db')

cursor = conexao.cursor()

id = input('Digite o ID da loja cujo produto deseja alterar: ')
produtos = input('Digite o tipo de produto que a loja vende: ')

sql = 'update loja set produtos = ? where id = ?'
valores = [produtos, id]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()