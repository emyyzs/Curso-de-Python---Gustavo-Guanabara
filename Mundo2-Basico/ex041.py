#Classificação de categoria de atletas
from time import sleep
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print('De acordo com a sua idade sua categoria é...')
sleep(3)

if idade <=9:
    print(f'Com {idade} anos você é um atleta MIRIM!')
elif idade <= 14:
    print(f'Com {idade} anos você é um atleta INFANTIL!')
elif idade <= 19:
    print(f'Com {idade} anos você é um atleta JUNIOR!')
elif idade <= 125:
    print(f'Com {idade} anos você é um atleta SENIOR!')
else:
    print(f'Com {idade} anos você é um atleta MASTER!')


