import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
print('Insira os dados do cliente: ')
nome = input('Qual o nome do cliente? ')
cpf = input('Qual o cpf do cliente? ')
valores = [nome, cpf]
sql_inserir = 'insert into cliente (nome, cpf) values (?, ?)'
cursor = conexao.cursor()
cursor.execute(sql_inserir, valores)
conexao.commit()
conexao.close()