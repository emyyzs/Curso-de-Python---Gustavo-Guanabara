# Jogo da adivinhação
from random import randint
from time import sleep

computador = randint(0, 10)  # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))  # Jogador tenta adivinha
print('PROCESSANDO...')
sleep(3)
t = 0
while jogador != computador:

    jogador = int(input('Você errou! Tente novamente acertar o n° de 0 a 10:'))
    t += 1

print(f'PARABÉNS, você acertou! Eu pensei no número {computador} e Você fez {t} tentativas ')


