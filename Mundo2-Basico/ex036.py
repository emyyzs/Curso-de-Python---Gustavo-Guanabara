#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salario do comprador e em quantos anos ele vai pagar
# A prestação mensal, não pode execer 30% do salario ou então o emprestimo será negado

casa = float(input('Qual o valor da casa: R$ '))
salario = float(input('Qual o seu salário: R$ '))
anos = int(input('Quantos anos de financiamento? '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100

print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}.')

if prestacao <= minimo:
    print(f'Seu empréstimo foi CONCEDIDO!')

else:
    print('Seu empréstimo foi NEGADO! A prestação exedeu 30% do seu salário ')