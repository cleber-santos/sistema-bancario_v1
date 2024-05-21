
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    #### DEPOSITO
    if opcao == "d":

        valor_deposito = float(input("Informe o valor que deseja deposita: ")) # armazena o input e converte em float

        if valor_deposito > 0: # Garante que só receba valores positivos
            saldo += valor_deposito
            extrato += f"\nDeposito + R$ {valor_deposito:.2f}\n" # Salva no extrato
            print("====== Deposito realisado! =======\n")
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
            print("==================================\n")
            print("O que deseja fazer a seguir:")
        else:
            print("Valor informado é inválido, por favor tente novamente.")
        

    #### SAQUE              
    elif opcao == "s":
        
        valor_saque = float(input("Informe o valor que deseja sacar: ")) # armazena o input e converte em float

        # Regras para saque
        saldo_insuficiente = valor_saque > saldo # Quando o saque é maior que o saldo em conta
        excedeu_valor_saque = valor_saque > limite # Quando o saque é maior que o limite de valor para saque
        excedeu_limite_saque = numero_saques >= LIMITE_SAQUES # Quando a quantidades de saques utrapassa o limite de saques diarios

        if saldo_insuficiente:
            print("Saldo insuficiente, tente um valor menor.")
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
        
        elif excedeu_valor_saque:
            print("Valor de saque maior que o limite permitido, tente um valor menor")
            print(f"Seu limite de saque é de R$ {limite:.2f}")

        elif excedeu_limite_saque:
            print("Você excedeu seu limite diario de saques. Tente sacar amanhã ou entre em contato com seu gerente")

        elif valor_saque > 0: # Garante que só receba valores positivos
            
            saldo -= valor_saque # Faz o saque e atualiza o valor do saldo
            numero_saques += 1 # Atualiza o numero de saques
            extrato += f"\nSaque - R$  {valor_saque:.2f}\n" # Salva no extrato
            
            print("==== Saque realizado com sucesso! ====\n")
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
            print("E seu numero de saques diarios é de " + str(LIMITE_SAQUES - numero_saques))
            print("======================================\n")
            print("O que deseja fazer a seguir:")

        else:
            print("Valor informado é inválido, por favor tente novamente.")

    #### EXTRATO
    elif opcao == "e":
        print("\n============= Extrato ===============")
        print("\nNão foram realizados movimentações.\n" if not extrato else extrato)        
        print(f"Seu saldo atual é de R$ {saldo:.2f}.".upper())
        print("\n=====================================")

    #### SAIR
    elif opcao == "q":
        break

    #### ERRO
    else:
        print("Operação inválida, por favor selecione a operação desejada.")

print("Obrigado por usar nosso banco!")