import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

id = input('Digite o ID da empresa que deseja atualizar: ')
nome = input('Digite o novo nome da empresa: ')

sql = 'update fornecedor set nome = ? where id = ?'
valores = [nome, id]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()