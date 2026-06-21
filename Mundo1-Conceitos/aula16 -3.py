#Variavéis compostas

lanche = ( suco, pizza, queijo, pudim)
#           0   ,  1   ,   2 ,  3
print (lanche [2]) # imprime queijo
print (lanche[0:2]) # imprime suco e piza
print (lanche[1:]) # começa no 1 e vai até o final ( pizza,queijo e pudim)
print (lanche[-1]) # o ultimo elemento : pudim
len (lanche) # quantos elementos tem na variavel

for c in lanche:
    print(c) # ele vai para um loop dos lanches e depois sai

    # AS TUPLAS SÃO IMUTÁVEIS, não da para remover um item