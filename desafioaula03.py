nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome = str(input('Digite seu nome: '))
        if len(nome) == 0:
            raise ValueError("Vão não digitou nada.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome nao deve conter números.")
        elif nome.isspace() == True:
            raise ValueError("Voce digitou somente espaço.")
        else:
            print('Nome válido.')
            nome_valido = True
    except ValueError as e:
        print(e)

while salario_valido is not True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario <= 0:
            raise ValueError("O salário não pode ser negativo.")
        else:
            print("Salário registrado.")
            salario_valido = True
    except ValueError as e:
        print(e)

while bonus_valido is not True:
    try:
        bonus = float(input("Digite o bôunus: "))
        if bonus < 0:
            raise ValueError("O bônus não pode ser negativo.")
        else:
            print("Bônus registrado.")
            bonus_valido = True
    except ValueError as e:
        print(e)