n1 = int(input('Digite um número:'))
opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()

q = 0
while opcao == 'S':

    soma += n1
    q +=1
    media = soma / q

    print (f'A soma dos numeros é {soma}, sua media é {media} e voce digitou {q} numeros ')
