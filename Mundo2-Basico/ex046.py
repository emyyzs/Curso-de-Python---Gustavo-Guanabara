from time import sleep

print('Vai iniciar uma contagem regressiva para os fogos: ')
for c in range(10, 0, -1): # se colocar -1 no meio a contagem vai até 0
    print( c)
    sleep(1)

print('🎆 POOOWWW! 🎆')