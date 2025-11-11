#criar um programa de gereciador de notas e mostrar o uso  de len(), append(), sum(), remove()
#lista vazia para armazenar notas 

notas = []
login_admin = "adm"
senha_admin = "2530@"

login_user = input("\nInforme seu login: ")
login_password = input("Informe sua senha: ")

def menu_admin():
    while True:
        print("\n\t==== Gerenciador de Notas (Admin) ====")
        print("1 - Adicionar nota")
        print("2 - Remover nota")
        print("3 - Mostrar todas as notas")
        print("4 - Mostrar quantidade e média das notas")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nota = float(input("Digite a nota: "))
            notas.append(nota)
            print("Nota adicionada com sucesso!")

        elif opcao == "2":
            if len(notas) == 0:
                print("Não há notas para remover.")
            else:
                print("Notas atuais:", notas)
                remove = float(input("Informe a nota que deseja remover: "))
                if remove in notas:
                    notas.remove(remove)
                    print(f"Nota {remove} removida com sucesso!")
                else:
                    print("Essa nota não está na lista.")

        elif opcao == "3":
            mostrar_notas()

        elif opcao == "4":
            mostrar_media()

        elif opcao == "5":
            print("Encerrando o programa. Tchau!")
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario():
    while True:
        print("\n\t==== Visualizador de Notas (Usuário) ====")
        print("1 - Mostrar todas as notas")
        print("2 - Mostrar quantidade e média das notas")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_notas()

        elif opcao == "2":
            mostrar_media()

        elif opcao == "3":
            print("Saindo... até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

def mostrar_notas():
    if len(notas) == 0:
        print("Não há notas registradas.")
    else:
        print("Notas atuais:", notas)

def  mostrar_media():
    if len(notas) == 0:
        print("Não há notas para calcular média.")
    else:
        quantidade = len(notas)
        soma = sum(notas)
        media = soma / quantidade
        print(f"Quantidade de notas: {quantidade}")
        print(f"Soma das notas: {soma:.2f}")
        print(f"Média da turma: {media:.2f}")

        if media >= 7:
            print("A turma está com bom desempenho!")
        else:
            print("A turma precisa melhorar.")

# ===== Verificação de login =====
if login_user == login_admin and login_password == senha_admin:
    print("\nLogin de administrador reconhecido!")
    menu_admin()
else:
    print("\nLogin de usuário comum reconhecido.")
    menu_usuario()
