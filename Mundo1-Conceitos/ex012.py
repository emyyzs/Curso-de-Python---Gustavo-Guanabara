#Calculando descontos
preco = float(input('Digite um preco: R$'))

desconto = preco - (preco * 5  / 100)

print('O valor com o desconto de 5% fica {:.2f}:'.format(desconto,))