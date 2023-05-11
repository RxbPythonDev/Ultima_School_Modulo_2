import sqlite3

conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()

resultados = cursor.execute('select * from categoria')
for resultado in resultados:
    print(f'ID: {resultado[0]}| Nome: {resultado[1]}| Descrição: {resultado[2]}')

conexao.close()