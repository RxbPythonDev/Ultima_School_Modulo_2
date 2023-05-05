import sqlite3

conexao = sqlite3.connect('Fornecedor.db')

cursor = conexao.cursor()

sql = '''
create table if not exists fornecedor (
    id integer primary key autoincrement not null,
    nome text not null,
    endereco text not null,
    produto text not null
);
'''

cursor.execute(sql)

conexao.commit()
conexao.close()