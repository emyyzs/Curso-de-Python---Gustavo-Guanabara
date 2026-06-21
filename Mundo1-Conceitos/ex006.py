#Dobro, triplo e raiz quadrada
n1 =int(input('Digite um numero: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)
print('O dobro do numero é {} \nO triplo é {} \nE a raiz quadrada é {:.2f}' .format(dobro, triplo, raiz))

'''Outra forma'''
n1 =int(input('Digite um numero: '))
print('O dobro do numero é {} \nO triplo é {} \nE a raiz quadrada é {:.2f}' .format((n1*2), (n1*3), (n1**(1/2), pow(n1, (1/2)))))
