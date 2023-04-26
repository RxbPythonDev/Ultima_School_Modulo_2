import sqlite3

conexao = sqlite3.connect('gerenciador_eventos.db')

conexao.execute('''CREATE TABLE organizador
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE);''')

conexao.execute('''CREATE TABLE eventos
                (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                titulo TEXT NOT NULL,
                data TEXT NOT NULL,
                local TEXT NOT NULL,
                organizador_id INTEGER NOT NULL,
                FOREIGN KEY(organizador_id) REFERENCES organizador(id));''')

conexao.close()