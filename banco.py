menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

'''
saldo = 0
saques = 0
VALOR_LIMITE = 500
LIMITE_DE_SAQUE = 3
extrato = ""

while True :
    opcao = input(menu)
    
    if opcao == '1' :
        deposito = float(input('\nInforme o valor que deseja depositar: '))
        if deposito > 0 :
            saldo += deposito
            extrato += (f'\nDepositou R${float(deposito):.2f}')
            print(f'\nSeu deposito de R${float(deposito):.2f} foi concluído. \nVoltando ao menu...')
        else :
            print(f'\nSeu deposito tem que ser maior que 0. \nVoltando ao menu...')
        
    elif opcao == '2' :
        if saques  <= LIMITE_DE_SAQUE:
            sacar = float(input(f'\nSeu saldo atual é: R${float(saldo):.2f}. Quanto gostaria de sacar? '))
            if sacar <= saldo and sacar <= VALOR_LIMITE and sacar != 0 : 
                saldo -= sacar
                extrato += (f'\nSacou R${float(sacar):.2f}')
                saques += 1
                print(f'\nSaque realizado com sucesso! Seu saldo restante é de: R${float(saldo):.2f} \nVoltando ao menu...')
            else :
                print('\nSaldo insuficiente, valor nulo ou o valor de saque maior que R$500! \nVoltando ao menu...')
        else :
            print('\nVocê já atingiu o limite de saque diário. \nVoltando ao menu...')
        
    elif opcao == '3' :
        print(f'\nSeu extrato:\n{extrato.lstrip()} \nSeu saldo atual é de: R${float(saldo):.2f}. \nVocê tem {3 - saques} saques restantes hoje. \nVoltando ao menu...')
    
    else :
        print('\nSaindo...')
        break