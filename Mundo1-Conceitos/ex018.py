#Seno, Cosseno e Tangente
from math import radians, sin, cos, tan
an = float(input('Digite o angulo que vocÊ deseja: '))
seno = sin(radians(an))
print(f'O angulo de {an} tem o SENO de {seno:.2f}')
cosseno = cos(radians(an))
print(f'O angulo de {an} tem o COSSENO de {cosseno:.2f}')
tan = tan(radians(an))
print(f'O angulo de {an} tem a TANGENTE de {tan:.2f}')