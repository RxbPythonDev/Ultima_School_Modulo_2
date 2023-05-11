import sqlite3

conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()

data = input('Digite a data para consultar as tarefas do dia (DD/MM/AAAA): ')
sql = '''
select t.id, t.nome, t.descricao, c.nome, conclusao 
from tarefa t, categoria c where c.id = t.categoria_id and t.data = ?
 '''
resultados = cursor.execute(sql,[data])
for resultado in resultados:
    print(f'ID: {resultado[0]}| Nome: {resultado[1]}| Descrição: {resultado[2]}| Categoria: {resultado[3]}| Conclusão: {resultado[4]}')

conexao.close()