import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

id = input('Digite o ID da empresa que deseja atualizar: ')
produto = input('Digite o novo produto da empresa: ')

sql = 'update fornecedor set produto = ? where id = ?'
valores = [produto, id]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()