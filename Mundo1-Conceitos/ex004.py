#Dissecando uma variavel
a  = input('Digite algo:')

print('O tipo primitivo desse valor é ',type(a))
print('Possui espaços? ',a.isspace())
print('É um número?',a.isnumeric())
print('É alfabetico?',a.isalpha())
print('É alfanumerico?',a.isalnum())
print('Esta em maiuscula?',a.isupper())
print('Esta em minusculas?',a.islower())
print('Esta em capitalizada?',a.istitle())

'''type(a) → Sempre vai mostrar <class 'str'>, porque tudo que vem do input() é texto (string)'''