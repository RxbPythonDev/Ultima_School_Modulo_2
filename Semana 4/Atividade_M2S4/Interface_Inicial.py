while True:
    print('Bem-vindo ao programa do Rafael de lista de tarefas! Essas são suas opções:')
    print('1) Manipular Categorias')
    print('2) Manipular Tarefas')
    print('3) Listar Tarefas do dia')
    print('4) Lista de Categorias')
    print('5) Concluir Tarefa')
    print('0) Sair do Programa')

    acao = int(input('Digite o número da opção escolhida: '))

    if acao == 1:
        import Manipular_Categoria
    elif acao == 2:
        import Manipular_Tarefa
    elif acao == 3:
        import Listar_Tarefas
    elif acao == 4:
        import Listar_Categorias
    elif acao == 5:
        import Concluir_Tarefa
    elif acao == 0:
        print('FIM DO PROGRAMA')
        break
    else:
        print('Opção Inválida! \n')