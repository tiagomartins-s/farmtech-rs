from data.data_manager import inserir_dados, atualizar_dados, deletar_dados, mostrar_dados, exportar_dados_para_xlsx

def show_menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualização de dados")
        print("4. Deleção de dados")
        print("5. Exportar dados")
        print("6. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            mostrar_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dados()
        elif opcao == "5":
            exportar_dados_para_xlsx()
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")
