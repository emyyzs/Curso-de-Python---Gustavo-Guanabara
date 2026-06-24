# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ano = date.today().year

maiores = 0
menores =0
for c in range(1, 8):
    nasc = int(input(f'Digite sua data de nascimento pessoa {c}:'))
    idade = ano - nasc
    if idade >= 18:

        maiores += 1 # contagem 0,1,2,3,4
    else:

        menores += 1  # contagem 0,1,2,3,4
print (f'{maiores} pessoas ja são maiores de idade.')
print(f'{menores} pessoas são menores de idade')
