
n = (int(input('Digite um número: ')))
for c in range(0, n+1): #Faz funcionar exatamente de 0 ao numero digitado
    print(c)
print (30 * '=')
#==========================================
for c in range(6, 0, -1): #conta de forma decrescente
    print(c)
print('FIM')
#==========================================
for c in range(0, 6, 2): #pula de 2 em 2
    print(c)
#==========================================
i = int(input('Inicio: '))
p = int(input('Passo: '))
f = int(input('Fim: '))
if p == 0:
    print('Passo não pode ser zero')
for c in range(i, f + 1, p):# o numero digitado para o P, vai contar o tanto de casa vai pular entre o Inicio e Fim
    print(c)
#=========================================
s = 0
for c in range(0, 4):
   n = int(input('Digite um numero:'))
   s += n
print(f'A soma dos numeros digitados é: {s}')


