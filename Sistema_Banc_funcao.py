import textwrap
import re
from datetime import datetime

def menu():
    menu = """\n
    
    ========= MENU =========
    [1]\t Depositar
    [2]\t Saque
    [3]\t Extrato
    [4]\t Novo Usuário
    [5]\t Nova Conta
    [6]\t Listar Contas
    [0]\t Sair
    => """
    
    return int(input(textwrap.dedent(menu)))

def depositar(saldo, valor, extrato):
    if valor >= 100:
        print("\nDepósito realizado!\n")
        saldo += valor
        extrato += f"Data: {datetime.now()} Depósito: R${valor:.2f} - Saldo: R${saldo:.2f}\n"

    else:
        print("\nValor inválido, este caixa aceita apenas depósitos mínimos de R$100. Tente novamente!\n"
                )
    return saldo, extrato


def sacar(saldo, valor, limite, num_saques, limite_saques, extrato):
      
     
    if 0 < valor <= limite and valor % 10 == 0:
        if valor <= saldo:
            saldo -= valor
            extrato += f"Data: {datetime.now()} Saque: R${valor:.2f} - Saldo: R${saldo:.2f}\n"
            if num_saques < limite_saques:
                print("\nSaque realizado com sucesso!\n")
            num_saques += 1
            if num_saques >= limite_saques:
                print("\nO número de tentativas de saques diários foi excedido, tente novamente amanhã ou ligue para a Central de Relacionamento no 4004-2020!")
        else:
            print("\nSaldo insuficiente!")
    else:
        print("\nVocê só pode realizar saques de até R$500 por saque.")

    return saldo, extrato


def exibir_extrato(saldo, extrato):
     
    if not extrato:
                print("\nNão foram realizadas movimentações.\n")
    else:
            print(f"\nExtrato: \n")
            extrato += f"Data: {datetime.now()} Saldo: R${saldo:.2f}\n"
            print(extrato)

def criar_usuario(usuarios):
     
     cpf = input("Informe seu CPF (Somente números): ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n Já existe usuário com esse CPF!")
          return
     
     nome = input("Digite o nome do titular da conta: ")
     data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
     endereco = input("Informe o endereço (logradouro, número - bairro - cidade/UF): ")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario
                           for usuario in usuarios
                           if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios, extrato):
     cpf = input("Informe o CPF do usuário: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n=== Conta criada com sucesso! ===")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario, "extrato": extrato}
     
     print("\n@@@ Usuário não encontradp, fluxo de criação de conta encerrado! @@@")
     

def listar_contas(contas):
     for conta in contas:
          linha = f"""\
          Agência:\t{conta["agencia"]}
          C/C:\t\t{conta["numero_conta"]}
          Titular:\t{conta["usuario" ]["nome"]}"""
          print("=" * 100)
          print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == 1:
            valor =  float(input("Informe o valor a ser depositado: R$"))
            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == 2:
            valor = float(input("\nInforme a quantia para o saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
                extrato=extrato)


        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)
                
        
        elif opcao == 4:
            criar_usuario(usuarios)
            

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios, extrato)

            if conta:
                 contas.append(conta)

           
        elif opcao == 6:
             listar_contas(contas)


        elif opcao == 0:
            print("\nSaindo do sistema...Tenha um bom dia!")
        

        else:
            print("\nOpção inválida, tente novamente!\n")



main()