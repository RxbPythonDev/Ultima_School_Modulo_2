import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

sql = 'select * from fornecedor'

resultados = cursor.execute(sql)

for resultado in resultados:
    print(f'ID:{resultado[0]}')
    print(f'Nome:{resultado[1]}')
    print(f'Endereço:{resultado[2]}')
    print(f'Produto:{resultado[3]}')
    
conexao.commit()

conexao.close()