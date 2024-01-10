menu = """ 
********ESCOLHA UMA DAS OPÇÕES PARA PROSSEGUIR*******

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
=====================================================

Digite aqui o numero da opção>>: """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Insira o valor de deposito: "))

    
        if valor > 0:
            saldo += valor
            extrato += (f"Depósito: R$ {valor:.2f}\n")
            

        else:
            print("Falha na operação!!! valor invalido")
    
    elif opcao == "2":
        valor = float(input("Insira o valor de saque: "))

        excedeu_o_saque = valor > saldo
        
        excedeu_o_limite = valor > limite

        excedeu_o_limite_de_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_o_saque:
            print("Falha na operação!!! Valor inserido não disponivel, tente novamente.")
            
        elif excedeu_o_limite:
            print("Falha na operação!!! Valor limite de saque excedido, tente novamente.")

        elif excedeu_o_limite_de_saque:
            print("Falha na operação!!! Limite de 3 depositos diarios excedidos, tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor
            extrato += (f"saque: R$ {valor:.2f}\n")
            numero_saques += 1

        else:
            print("Falha na operação!!! o valor que foi informado é invalido, tente novamente.")

    elif opcao == "3":
        print("\n###############################EXTRATO#############################")
        print("Não há depósito ainda" if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("###################################################################")

    elif opcao == "4":
        print("Volte sempre!!!")
        break

    else:
        print("Operação invalida!!! Tente novamente.")

    