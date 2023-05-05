import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

nome = input('Digite o nome da empresa: ')
endereco = input('Digite o endereço da empresa: ')
produto = input('Digite o produto da empresa: ')

sql = 'insert into fornecedor (nome, endereco, produto) values (?, ?, ?)'
valores = [nome, endereco, produto]

cursor.execute(sql, valores)

conexao.commit()

conexao.close()