menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Qual valor deseja depositar: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R${valor:.2f}\n"
            print("Deposito Realizado!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Sacar")
        valor = float(input("Qual valor deseja Sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação Falhou! Valor do saque ultrapassou o limite.")
        elif excedeu_saques:
            print("Operação Falhou! Você já usou todos os saques diário.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação Falhou! O valor informado é inválido")

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas operações.")
        print("\n===== Extrato =====")
        print(extrato)
        print("===================")
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção Inválida, Por favor selecione novamente a operação desejada.")
