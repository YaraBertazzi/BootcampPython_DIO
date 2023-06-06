# Sistema de banca v.1
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>"""

saldo = 0
limite = 500
extrato = ''
n_saque = 0
limite_saque = 3

while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito R$ {valor:.2f}\n'

        else:
            print('Valor inválido')

    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = n_saque >= limite_saque

        if excedeu_saldo:
            print('Saldo insuficiente')

        elif excedeu_limite:
            print('Limite insuficiente')

        elif excedeu_saque:
            print('Excedeu limite de saque')

        elif valor > 0:
            saldo -= valor
            extrato += f'\nSaque: R$ {valor:.2f}\n'
            n_saque += 1

        else:
            print('Valor inválido')

    elif opcao == '3':
        print('\n************** EXTRATO *************')
        print('Não foram realizados movimentações.\n' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('*************************************')

    elif opcao == '4':
        break
    else:
        print('Operação inválida.')





