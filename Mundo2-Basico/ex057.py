sexo =str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Valor inválido. Por favor, informe seu sexo [M/F]: ')).upper()

print(f'Você é do sexo {sexo}')


