import sqlite3

conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()

resultados = cursor.execute('select id, nome from tarefa')
for resultado in resultados:
    print(f'ID: {resultado[0]}| Nome: {resultado[1]}')
id = int(input('Digite o ID da tarefa que deseja marcar como concluída: '))
sql = 'update tarefa set conclusao = True where id = ?'
cursor.execute(sql,[id])
print('Tarefa marcada como concluída!')

conexao.commit()
conexao.close()