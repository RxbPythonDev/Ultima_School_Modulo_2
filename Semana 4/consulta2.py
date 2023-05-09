import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
pedido_id = input('Qual o ID do pedido? ')
sql = 'select sum(quantidade) from item_pedido where pedido_id = ?'
consulta = cursor.execute(sql, [pedido_id])
for resultado in consulta:
    print(resultado)