#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
par = 0
cont = 0
for c in range(1, 6+1):
    num = int(input('Digite um numero :'))
    if num % 2 == 0:
        par += num  # soma do total dos numeros
        cont += 1
print(f'A soma dos numeros pares é: {par}')