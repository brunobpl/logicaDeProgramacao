# Faça um programa que recebe uma lista de números do usuário e encontra o menor número.

listaNumeros = []
quantidadeDeNumeros = int(input("Informe a quantidade de elementos da lista: "))

for i in range(quantidadeDeNumeros):
    numero = str(input("Entre com o " + str(i+1) + "º número" + ": "))
    listaNumeros.append(numero)

maiorNumero = 0
menorNumero = 0
for contador in range(quantidadeDeNumeros):
    if contador == 0:
        maiorNumero = menorNumero = listaNumeros[contador]
    else:
        if listaNumeros[contador] > maiorNumero:
            maiorNumero = listaNumeros[contador]
        if listaNumeros[contador] < menorNumero:
            menorNumero = listaNumeros[contador]

print ("A lista de números informada pelo usuário: " +  str(listaNumeros))
print ("O menor número é: ", menorNumero)