'''
Crie uma tabela chamada “cliente”. É necessário que ela tenha as seguintes colunas:
ID
NOME
CPF
DATA_CADASTRO
ENDERECO
'''

import sqlite3

conexao = sqlite3.connect('clientes.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cliente (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    data_cadastro DATE,
    endereco VARCHAR(300) NOT NULL
);
''')

conexao.commit()
conexao.close()