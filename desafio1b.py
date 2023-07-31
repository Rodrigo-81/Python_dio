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

def depositar(saldo, valor, op_extrato):
    if valor > 0:
        saldo += valor
        op_extrato += f"Depósito:\t R$: {valor:.2f}\n"
        print("Depósito concluído")
    else:
        print("Depósito cancelado, valor não processado.")
        
    return saldo, op_extrato
    
def sacar(valor,saldo, op_extrato, numero_saques):
    if valor == 0:
        print("Erro, verifique valor desejado para saque")
    elif valor > 500:
        print("Saque não autorizado, verifique limite para operação")
    elif (saldo - valor) < 0:
        print("Saque não autorizado, verifique saldo disponível")
    else:
        saldo -= valor
        op_extrato += f"Retirada:\t R$: {valor:.2f}\n"
        numero_saques += 1
        print("Saque autorizado com sucesso")
    return saldo, op_extrato, numero_saques
            
    
def extrato(saldo, op_extrato):
    if op_extrato == "":
        print("Não há transações para extrato")
    else:
        print(f"Saldo atual: {saldo:.2f}\n Extrato:\n{op_extrato}")

def novo_usuario(usuarios):
    cpf = input("Insira CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já consta na base de dados")
        return
    
    nome = input("Informe o nome:")
    dt_nasc = input("Informe data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe endereço (logradrouro, numero - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data nascimento": dt_nasc, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado")


def filtrar_usuario(cpf, usuarios):
    filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtro[0] if filtro else None

def nova_conta(agencia, num_conta, usuarios):
    cpf = input("Informe cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta cadastrada com sucesso")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": usuario}
    
    print("Usuário não encontrado, cadastramento cancelado.")

def listar_contas(contas):
    if contas == []:
        print("Não há contas registradas!")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Endereço:\t{conta['usuario']['endereco']}
        """
        print("=" * 100)
        print(linha)

def sair():
    print("Encerrando programa.")
    return False

def main():
    agencia = "001"
    saldo = 0
    limite = 500
    op_extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    operacoes = []
    usuarios = []
    contas = []
    
    
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

        elif op == 'n':
            num_conta = len(contas) + 1
            conta = nova_conta(agencia, num_conta, usuarios)

            if conta:
                contas.append(conta)

        elif op == 'u':
            novo_usuario(usuarios)

        elif op == 'l':
            listar_contas(contas)
            
        elif op == 'x':
            sair()
            break
            
main()

