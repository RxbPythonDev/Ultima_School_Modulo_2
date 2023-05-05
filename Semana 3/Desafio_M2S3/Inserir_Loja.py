import sqlite3

conexao = sqlite3.connect('Loja.db')

cursor = conexao.cursor()

id = input('Digite o ID da loja: ')
nome = input('Digite o Nome da loja: ')
endereco = input('Digite o Endereço da loja: ')
produtos = input('Digite os produtos da loja: ')

sql = 'insert into loja (id, nome, endereco, produtos) values (?, ?, ?, ?)'
valores = [id, nome, endereco, produtos]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()