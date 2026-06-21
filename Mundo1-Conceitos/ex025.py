#Procurando uma string dentro de outra
nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome tem Silva? {'silva' in nome.lower()}')