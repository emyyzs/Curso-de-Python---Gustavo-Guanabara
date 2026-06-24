n1 = int(input('Digite um número:'))
n2 = int(input('Digite um número:'))

opcao = 0

while opcao != 5:

    opcao = int (input('''---- MENU DE OPÇÕES ----
    [1] somar
    [2] multiplicar
    [3] maior
    [4] digitar outros numeros
    [5] sair do programa
    Digite uma das opções acima: '''))


    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O numero maior é {n1}')
        else:
            print(f'O numero maior é {n2}')
    elif opcao == 4:
        print('Digite novamente os numeros:')
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite um número:'))

    elif opcao == 5:
        print('Programa encerrado')
    else:
        print('Opção inválida!')
