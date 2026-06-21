#Radar eletrônico
velocidade = int(input('Digite a velocidade atual do seu carro:'))
if velocidade > 80:
    print('MULTADO! Você  excedeu o limite permitido que é de 80km/h !')
    multa = (velocidade - 80) * 7
    print (f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia ! Dirija com segurança =) ')
