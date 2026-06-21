#Desenvolva um programa que pergunte a distãncia de uma viagem em Km.
# Calcule o preço da passagem,cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas
distancia = float(input('Qual é a distãncia da sua viagem? '))
print ('Você está prestes a começar uma viagem de {}Km.')
if distancia <= 200:
    preço =distancia * 0.50
else:
    preço =distancia * 0.45
    print(f'E o preco da sua passagem será de R${preço:.2f}')