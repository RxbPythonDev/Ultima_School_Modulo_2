import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

produto = input('Digite o produto da empresa que deseja consultar: ')

sql = 'select * from fornecedor where produto = ?'
valores = [produto]

resultados = cursor.execute(sql,valores)

for resultado in resultados:
    print(f'ID:{resultado[0]}')
    print(f'Nome:{resultado[1]}')
    print(f'Endereço:{resultado[2]}')
    print(f'Produto:{resultado[3]}')
    
conexao.commit()

conexao.close()