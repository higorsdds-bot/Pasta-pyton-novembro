name: list = []

while True:
    names: str = input("Informe o nome do usuário: ")
    print("Escreva -> sair <- para finalizar o programa")

    if names.lower() == "sair":
        print("Alunos registrados:")
        break

    name.append(names)
    print(f"A quantidade de alunos: {len(name)}")
    print(f"Os alunos registrados são: {name}")