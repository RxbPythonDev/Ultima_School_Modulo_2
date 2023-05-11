import sqlite3 

conexao = sqlite3.connect('todo.sqlite3')
cursor = conexao.cursor()

def criar_categoria():
    nome = input('Digite o nome da categoria: ')
    descricao = input('Digite a descrição da categoria: ')
    sql = 'insert into categoria (nome, descricao) values (?, ?)'
    valores = [nome, descricao]
    cursor.execute(sql,valores)
    print('Categoria criada com sucesso!')

def atualizar_categoria():
    resultados = cursor.execute('select id, nome from categoria')
    for resultado in resultados:
        print(f'ID: {resultado[0]}| Nome: {resultado[1]}')
    id = int(input('Digite o ID da categoria que deseja atualizar: '))
    nome = input('Digite o novo nome da categoria: ')
    descricao = input('Digite a nova descrição da categoria: ')
    sql = 'update categoria set nome = ?, descricao = ? where id = ?'
    valores = [nome, descricao, id]
    cursor.execute(sql,valores)
    print('Categoria atualizada com sucesso!')

def excluir_categoria():
    resultados = cursor.execute('select id, nome from categoria')
    for resultado in resultados:
        print(f'ID: {resultado[0]}| Nome: {resultado[1]}')
    id = int(input('Digite o ID da categoria que deseja excluir: '))
    sql = 'delete from categoria where id = ?'
    cursor.execute(sql,[id])
    print('Categoria excluída com sucesso!')

while True:
    print('Bem-vindo ao programa de manipulação de categorias, suas opções são:')
    print('1) Criar Categoria')
    print('2) Atualizar Categoria')
    print('3) Excluir Categoria')
    print('0) Voltar')
    acao = int(input('Digite o número da opção escolhida: '))
    if acao == 1:
        criar_categoria()
    elif acao == 2:
        atualizar_categoria()
    elif acao == 3:
        excluir_categoria()
    elif acao == 0:
        break
    else:
        print('Opção inválida! \n')

conexao.commit()
conexao.close()