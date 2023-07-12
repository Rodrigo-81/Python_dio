def menu():
    print("""
Menu principal:

[d] depositar
[s] sacar
[e] extrato
          
[n] nova conta
[u] usuario 
[l] listar contas
          
[x] sair

=> """)
    return input("Informe opção desejada :")

def depositar(valor, saldo, op_extrato):
    if valor > 0:
        saldo += valor
        op_extrato += f"Depósito:\t R$: {valor:.2f}\n"
        print("Depósito concluído")
    else:
        print("Depósito cancelado, valor não processado.")
        
    return saldo, op_extrato
    
def sacar(valor,saldo, op_extrato, numero_saques):
    if valor > 500:
        print("Saque não autorizado, verifique limite para operação")
    elif (saldo - valor) < 0:
        print("Saque não autorizado, verifique saldo disponível")
    else:
        saldo -= valor
        op_extrato += f"Retirada:\t R$: {valor:.2f}\n"
        numero_saques -= 1
        print("Saque autorizado com sucesso")
    return saldo, op_extrato, numero_saques
            
    
def extrato(saldo, op_extrato):
    if op_extrato == "":
        print("Não há transações para extrato")
    else:
        print(f"Saldo atual: {saldo:.2f}\n Extrato:\n {op_extrato}")

def sair():
    print("Encerrando programa.")
    return False

def main():
    saldo = 0
    limite = 500
    op_extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    operacoes = []
    
    
    while True:
        op = menu()

        if op == 'd':
            print("Depósito")
            valor = float(input("Informe valor para depósito:"))
            saldo, op_extrato = depositar(saldo, valor, op_extrato)

        elif op == 's':
            if numero_saques == LIMITE_SAQUES:
                print("Limite de operações de retirada atingido")
            else:
                print("Retirada")
                valor = float(input("Informe valor de retirada:"))
                saldo, op_extrato, numero_saques = sacar(valor,saldo, op_extrato, numero_saques)

        elif op == 'e':
            extrato(saldo, op_extrato)
            
        elif op == 'x':
            sair()
            break
            
main()

