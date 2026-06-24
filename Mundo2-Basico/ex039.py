#Alistamento Militar
from time import sleep
from datetime import date

atual = date.today().year
nome = str(input('Digite seu nome:'))
nasc = int(input('Digite seu ano de nascimento: '))
idade = atual - nasc
tempo =  18 - idade

print(f'Olá {nome}, você tem {idade} anos hoje.')
print('Vou calcular os dados para seu alistamento militar!')
print('PROCESSANDO...')
sleep(4)
print('-=-' * 20)

if idade < 18:
    print(f'Você ainda não chegou no tempo de se alistar!ed Falta {tempo} ano(s) para seu alistamento!. ')
    ano = atual + tempo
    print(f'Seu alistamento será em {ano}')
elif idade == 18:
    print('Você está na hora de se alistar!')
else:
    ano = atual - tempo
    print(f'Você ja passou do tempo de se alistar faz {tempo} ano(s)!')
    print(f'Seu alistamento foi em {ano}')


