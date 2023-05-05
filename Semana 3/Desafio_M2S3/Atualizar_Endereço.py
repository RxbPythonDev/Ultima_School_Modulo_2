import sqlite3

conexao = sqlite3.connect('Loja.db')

cursor = conexao.cursor()

id = input('Digite o ID da loja cujo endereço deseja alterar: ')
endereco = input('Digite o novo endereço da loja: ')

sql = 'update loja set endereco = ? where id = ?'
valores = [endereco, id]

cursor.execute(sql,valores)

conexao.commit()

conexao.close()