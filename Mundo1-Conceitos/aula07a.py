nome = input('Qual seu nome?')
print('Seja bem vindo(a) {:20}!' .format(nome))
print('Seja bem vindo(a) {:>20}!' .format(nome))
print('Seja bem vindo(a) {:<20}!' .format(nome))
print('Seja bem vindo(a) {:^20}!' .format(nome))
print('Seja bem vindo(a) {:=^20}!' .format(nome))

n1 = int(input('Digite um número: '))
n2 =int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' A soma é {}\n O produto é {}\n A divisão é {:.2f}\n' .format(s, m, d), end='')
print(' A divisão inteira é {}\n A potência é {}\n'.format(di, e))
