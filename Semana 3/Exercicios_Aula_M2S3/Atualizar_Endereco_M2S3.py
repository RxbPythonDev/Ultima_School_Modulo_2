import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

id = input('Digite o ID da empresa que deseja atualizar: ')
endereco = input('Digite o novo endereço da empresa: ')

sql = 'update fornecedor set endereco = ? where id = ?'
valores = [endereco, id]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()