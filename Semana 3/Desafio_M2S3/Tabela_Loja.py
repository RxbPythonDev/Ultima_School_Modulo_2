import sqlite3

conexao = sqlite3.connect('Loja.db')

cursor = conexao.cursor()

sql = ''' CREATE TABLE loja ( id INT, nome VARCHAR(150) NOT NULL, endereco VARCHAR(150), produtos VARCHAR(20) ); '''

cursor.execute(sql)

conexao.commit()

conexao.close()