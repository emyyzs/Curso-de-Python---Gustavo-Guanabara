#MUNDO 2
nome = str(input('Qual é seu nome?'))
if nome == 'Emilly':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Ana' or nome == 'Julia':
    print('Seu nome é popular no Brasil!')
elif nome in 'Eduarda Laura Pedro Mateus':
    print('Que nome bonito!')
else:
    print('Seu nome é normal!')