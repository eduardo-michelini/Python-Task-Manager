tarefas_concluidas = []
tarefas_pendentes = []

print("Gerenciador de Tarefas Simples")

nome = input("Digite o seu nome usuário: ").upper()
print(f"Bem-vindo usuário {nome} ao nosso Gerenciador de Tarefas Simples")

while True:
    print(" \n Opções")
    print(" 1 -  Adicionar Tarefa")
    print(" \n 2 - Ver tarefas pendentes")
    print(" \n 3 - Ver tarefas concluídas")
    print(" \n 4 - Marcar como concluída")
    print(" \n 5 - Sair \n")
    
    opcao_usuario = int(input(f"Digite a opção usuário {nome}: "))
    
    if opcao_usuario == 1:
        nome_tarefa = input(f"Digite a tarefa usuário {nome}: ").upper()
        tarefas_pendentes.append(nome_tarefa)
    
    elif opcao_usuario == 2:
        print(f"Usuário {nome}, as tarefas pendentes até agora são: {tarefas_pendentes}")
        
    elif opcao_usuario == 3:
        print(f"Usuário {nome}, as tarefas concluídas até agora são: {tarefas_concluidas}")
        
    elif opcao_usuario == 4:
        marcar_concluida = input(f"Qual tarefa você deseja marcar como concluída usuário {nome}: ").upper()
        
        if marcar_concluida in tarefas_pendentes:
            print(f"Tarefa {marcar_concluida} foi marcada como concluída usuário {nome}!")
            tarefas_concluidas.append(marcar_concluida)
            tarefas_pendentes.remove(marcar_concluida)
            
        elif marcar_concluida not in tarefas_pendentes:
            print(f"Tarefa {marcar_concluida} não existe em tarefas usuário {nome}!")
            
    elif opcao_usuario == 5:
        print(f"Obrigado por usar o nosso Gerenciador de Tarefas Simples, usuário {nome}!")
        break
    
    else:
        print(f"Opção inválida usuário {nome}, tente novamente!")