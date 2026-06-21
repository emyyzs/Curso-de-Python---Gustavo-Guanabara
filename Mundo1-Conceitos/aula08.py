''' Utilizando módulos

import math -->  usa todas as funcionalidades
from math import factorial, ceil --> importa uma função especifíca

ceil --> arredonda para frente
floor --> arredonda para baixo
trunc --> elimina a virgula pra frente
pow --> potencia
sqrt --> fórmula da raiz quadrada
factorial --> factorial

'''
'1 - importanto o módulo inteiro'

import math
num=int(input('Digite um numero'))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')

'2 - importanto funções especificas '

from match import sqrt, floor
num=int(input('Digite um numero'))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}')