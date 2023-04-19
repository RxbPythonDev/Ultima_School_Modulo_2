import sqlite3
conexao = sqlite3.connect('banco.sqlite3')
cursor = conexao.cursor()
sql = '''
create table categoria (
    id integer not null primary key autoincrement,
    descricao text(100)
)
'''
cursor.execute(sql)
conexao.commit()
conexao.close()
