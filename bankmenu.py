while True:

    while True:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == "admin" and senha == "12345":
            print("Logado com sucesso!")
            break
        else:
            print("Credenciais erradas")
            
    saldo = 1000

    while True:

        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            print(saldo)

        elif opcao == "2":
            deposito = float(input("Digite o valor a ser depositado: "))
            saldo = saldo + deposito
            print(f"Novo saldo: {saldo}")

        elif opcao == "3":
            saque = float(input("Valor do saque: "))
            saldo = saldo - saque
            print(f"Novo saldo: {saldo}")

        elif opcao == "4":
            print("Voltando ao menu de login...")
            break

