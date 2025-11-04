def informacoes():
    # 1. A variável 'quantidade' é definida DENTRO da função, 
    #    então não precisamos passá-la como parâmetro.
    try:
        quantidade = int(input("Quantas pessoas serão registradas:\n -> "))
    except ValueError:
        print("Erro: Você deve digitar um número inteiro.")
        return # Para a execução da função se a entrada for inválida
    pessoas = []
    # O loop 'for' para coletar os dados
    for i in range(quantidade):
        print(f"\n--- Registrando Pessoa {i + 1} ---")
        
        # 2. Havia um '1' sobrando no final desta linha, causando um erro de sintaxe.
        name = input("Informe o nome da pessoa: ")
        
        # Adicionei um loop 'try/except' para garantir que a idade seja um número
        idade = 0 # Valor padrão
        try:
            idade = int(input(f"Informe a idade de {name}: "))
        except ValueError:
            print("Idade inválida. Registrando como 0.")
            
        canal = input(f"Informe o nome do canal do {name}: ")
        naturalidade = input(f"Informe a naturalidade de {name}: ")
        
        # 3. É melhor guardar CPF como texto (string) para não perder zeros à esquerda.
        cpf = input(f"Informe o CPF de {name}: ")

        # 4. A criação do dicionário 'pessoa' e o 'append' 
        #    precisam estar DENTRO do loop 'for'.
        pessoa = {
            "Nome": name,
            "Idade": idade,
            "Canal": canal,
            "Naturalidade": naturalidade,
            "CPF": cpf
        }
        pessoas.append(pessoa)

    print("\n--- ✅ Pessoas Registradas ---")
    
    # 5. Este loop deve estar FORA do loop anterior (menos indentado).
    for pessoa in pessoas:
        
        # 6. Você deve iterar sobre os itens do 'pessoa' (o dicionário),
        #    e não da lista 'pessoas'.
        # 7. Faltava um ':' no final do 'for'.
        for chave, valor in pessoa.items():
            print(f"  {chave}: {valor}")
        print("-" * 20) # Adiciona um separador para melhor leitura

# Chama a função
informacoes()