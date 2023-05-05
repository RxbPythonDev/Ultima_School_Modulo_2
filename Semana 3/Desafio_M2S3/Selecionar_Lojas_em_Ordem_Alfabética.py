import sqlite3

conexao = sqlite3.connect('Loja.db')

cursor = conexao.cursor()

resultados = cursor.execute('select * from loja where endereco >= "Rua Principal" order by nome asc')

for resultado in resultados:
    print(resultado)