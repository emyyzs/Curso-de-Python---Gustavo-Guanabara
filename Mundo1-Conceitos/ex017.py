#Catetos e Hipotenusa
import math
co = float(input("Comprimento do cateto oposto:"))
ca = float(input("Comprimento do cateto adjacente:"))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')

'''Outra forma '''

c_oposto = float(input('Digite um comprimento para o cateto oposto: '))
c_adjacente = float(input('Digite um comprimento para o cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(c_oposto, 2) + math.pow(c_adjacente, 2))

print(f'A hipotenusa é {hipotenusa:.2f}')
