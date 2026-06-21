#Antecessor e Sucessor
n1 = int(input('Digite um número:'))
s = n1 + 1
a = n1 -1
print('O sucessor do numero {} é {} e seu antecessor é {}'.format(n1, s, a))

'''Outra forma:'''
n1 = int(input('Digite um número:'))
print('O sucessor do numero {} é {} e seu antecessor é {}'.format(n1, (n1+1), (n1-1)))
