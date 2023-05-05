import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

id = input('Digite o ID da empresa que deseja apagar: ')

sql = 'delete from fornecedor where id = ?'
valores = [id]

cursor.execute(sql,valores)

conexao.commit()
conexao.close()