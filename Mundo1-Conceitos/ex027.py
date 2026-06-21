#Primeiro e ultimo nome de uma pessoa 
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu ultimo nome é {n[len(n)-1]}')

