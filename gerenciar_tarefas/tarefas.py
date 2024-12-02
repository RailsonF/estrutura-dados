tarefas = []
estados = []

def add_tarefa(nome_tarefa):
    if nome_tarefa.lower() in tarefas:
        return "Erro: Tarefa já existe na lista!"
    else:
        tarefas.append(nome_tarefa.lower())
        estados.append("Pendente")
        return "Tarefa adicionada com sucesso"

def marcar_concluida(nome_tarefa):
    if nome_tarefa.lower() in tarefas:
        indice = tarefas.index(nome_tarefa.lower())
        estados[indice] = "Concluída"
        return "Tarefa marcada como concluída"
       
    else:
        return "Tarefa não encontrada"

def remover_tarefas(nome_tarefa):
    if nome_tarefa.lower() in tarefas:
        indice = tarefas.index(nome_tarefa.lower())
        estados.pop(indice)
        tarefas.pop(indice)
        return "Tarefa removida com sucesso"
    else:
        print("Tarefa não encontrada")

def listar_tarefas():
    print("Lista de Tarefas: ")
    print("\nTarefas Pendentes: ")
    for i in range(len(tarefas)):
        if estados[i] == "Pendente":
            print(f"- {tarefas[i]}")
    
    print("\nTarefas Concluídas")
    for i in range(len(tarefas)):
        if estados[i] == "Concluída":
            print(f"{tarefas[i]}")

def pesquisar_tarefas(nome_tarefa):
    if nome_tarefa.lower() in tarefas: #Verifica se o nome da tarefa está na lista
        indice = tarefas.index(nome_tarefa.lower()) #Retorna o índice da tarefa na lista tarefas
        estado = estados[indice] #Recupera o estado correspondente à tareaf usando o índice
        print(f"Tarefa encontrada: {nome_tarefa} - Estado: {estado}")
    else:
        print("Tarefa não encontrada")
    
def menu_principal():
    while True:
        print("\n--Escolha uma opção de 1 à 6--\n")
        print("1. Adicionar Tarefas")
        print("2. Concluir Tarefas")
        print("3. Excluir tarefas")
        print("4. Listar todas as tarefas")
        print("5. Pesquisar Tarefas")
        print("6. Sair do sistema")

        opcao = input("Escolha uma opção de 1 à 6:\n")
        if opcao == "1":
            nome_tarefa = input("Informe o nome da tarefa:\n")
            mensagem = add_tarefa(nome_tarefa)
            print(mensagem)
        elif opcao == "2":
            nome_tarefa = input("Informe o nome da tarefa:\n")
            mensagem = marcar_concluida(nome_tarefa)
            print(mensagem)
        elif opcao == "3":
            nome_tarefa = input("Informe o nome da tarefa:\n")
            mensagem = remover_tarefas(nome_tarefa)
            print(mensagem)
        elif opcao == "4":
            listar_tarefas()
        elif opcao == "5":
            nome_tarefa = input("Informe o nome da tarefa:\n")
            pesquisar_tarefas(nome_tarefa)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida, tenta novamente")

menu_principal()
        
    







