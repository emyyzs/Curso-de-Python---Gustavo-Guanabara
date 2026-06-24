#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
numero = 0
cont = 0
for c in range(1, 500+1):
    if c % 3 == 0:
        print(f'O numero {c} é DIVISIVEL por 3')
        cont = cont + 1
        numero += c
    else:
        print(f'{c} NÃO É ')
print(f'A soma dos {cont} numeros DIVISIVEIS por 3 é: {numero}')




