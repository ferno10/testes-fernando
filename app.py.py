def exibir_menu():
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Sair")

def gerenciar_tarefas():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-3): ")
        if opcao == "1":
            nova_tarefa = input("Digite a nova tarefa: ")
            tarefas.append(nova_tarefa)
            print(f"✔️ Tarefa '{nova_tarefa}' adicionada!")
        elif opcao == "2":
            if not tarefas:
                print("📭 Nenhuma tarefa cadastrada.")
            else:
                print("\n📋 Suas Tarefas:")
                for i, tarefa in enumerate(tarefas, 1):
                    print(f"{i}. {tarefa}")
        elif opcao == "3":
            print("👋 Saindo... Bom treino de Git!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    gerenciar_tarefas()
