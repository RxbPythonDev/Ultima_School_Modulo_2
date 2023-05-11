import sqlite3

conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()

def criar_tarefa():
    nome = input('Digite o nome da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    resultados = cursor.execute('select id, nome from categoria')
    for resultado in resultados:
        print(f'ID: {resultado[0]}| Nome: {resultado[1]}')
    categoria_id = int(input('Digite o ID da categoria da tarefa: '))
    data = input('Digite a data para realizar a tarefa (DD/MM/AAAA):')
    sql = 'insert into tarefa (nome, descricao, categoria_id, data, conclusao) values (?, ?, ?, ?, False)'
    valores = [nome, descricao, categoria_id, data]
    cursor.execute(sql, valores)
    print('Tarefa criada com sucesso!')

def atualizar_tarefa():
    resultados = cursor.execute('select id, nome from tarefa')
    for resultado in resultados:
        print(f'ID: {resultado[0]}| Nome: {resultado[1]}')
    id = int(input('Digite o ID da tarefa que deseja atualizar: '))
    nome = input('Digite o novo nome da tarefa: ')
    descricao = input('Digite a nova descrição da tarefa: ')
    resultados = cursor.execute('select id, nome from categoria')
    for resultado in resultados:
        print(f'ID: {resultado[0]}| Nome: {resultado[1]}')
    categoria_id = int(input('Digite o ID da nova categoria da tarefa: '))
    data = input('Digite a nova data para realizar a tarefa (DD/MM/AAAA):')
    sql = 'update tarefa set nome = ?, descricao = ?, categoria_id = ?, data = ? where id = ?'
    valores = [nome, descricao, categoria_id, data, id]
    cursor.execute(sql,valores)
    print('Tarefa atualizada com sucesso!')

def excluir_tarefa():
    resultados = cursor.execute('select id, nome from tarefa')
    for resultado in resultados:
        print(f'ID: {resultado[0]}| Nome: {resultado[1]}')
    id = int(input('Digite o ID da tarefa que deseja excluir: '))
    sql = 'delete from tarefa where id = ?'
    cursor.execute(sql,[id])
    print('Tarefa excluída com sucesso!')

while True:
    print('Bem-vindo ao programa de manipulação de tarefas, suas opções são:')
    print('1) Criar Tarefa')
    print('2) Atualizar Tarefa')
    print('3) Excluir Tarefa')
    print('0) Voltar')
    acao = int(input('Digite o número da opção escolhida: '))
    if acao == 1:
        criar_tarefa()
    elif acao == 2:
        atualizar_tarefa()
    elif acao == 3:
        excluir_tarefa()
    elif acao == 0:
        break
    else:
        print('Opção inválida! \n')

conexao.commit()
conexao.close()