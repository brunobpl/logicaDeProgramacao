# Faça um programa que cria uma lista de números aleatórios e encontra o maior número.

import random

listaNumeros = [random.randrange(1, 99, 1) for i in range(10)]
maiorNumero = 0
menorNumero = 0
for contador in range(0, 10):
    if contador == 0:
        maiorNumero = menorNumero = listaNumeros[contador]
    else:
        if listaNumeros[contador] > maiorNumero:
            maiorNumero = listaNumeros[contador]
        if listaNumeros[contador] < menorNumero:
            menorNumero = listaNumeros[contador]

print ("A lista de números aleatórios é: " +  str(listaNumeros))
print ("O maior número é: ", maiorNumero)
