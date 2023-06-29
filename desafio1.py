menu = """

[d] depositar
[s] sacar
[e] extrato
[x] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
operacoes = []

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        valor=float(input("Informe valor:"))
        if valor > 0:
            saldo += valor
            operacoes.append(['Depósito: R$ ',valor])
        elif valor <= 0:
            print("Valor não aceito.")
        
    elif opcao == "s":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:
            valor=float(input("Informe valor:"))
            if valor > limite :
                print("Valor não autorizado, acima do limite permitido")
            elif valor > saldo :
                print("Saque não autorizado, sem saldo disponivel")
            else:
                saldo -= valor
                operacoes.append(['Saque: R$ ',valor])
                print("Saque realizado com sucesso.")
                numero_saques += 1
        elif numero_saques >= LIMITE_SAQUES:
            print("Saque não autorizado, limite dessa operação atingido")
        
    elif opcao == "e":
        print("Extrato")
        print(operacoes)
        extrato=float(saldo)
        print(f"Saldo atual: R${extrato:3.2f}")

        
    elif opcao == "x":
        print("Encerrando operações, até breve.")
        break
        
    else:
        print("Opção inválida, selecione novamente.")
        