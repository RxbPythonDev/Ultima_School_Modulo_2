import sqlite3

conexao = sqlite3.connect('gerenciador_tarefas.db')

conexao.execute('''CREATE TABLE categorias
             (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             nome TEXT NOT NULL);''')

conexao.execute('''CREATE TABLE tarefas
             (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
             nome TEXT NOT NULL,
             data TEXT NOT NULL,
             categoria_id INTEGER NOT NULL,
             status BOOLEAN NOT NULL,
             FOREIGN KEY(categoria_id) REFERENCES categorias(id));''')

conexao.close()
