# Faça um programa que recebe uma lista de nomes e imprime todos os nomes que começam
# com a letra "A".
listaDeNomes = []
quantidadeDeNomes = int(input("Entre com a quantidade de nomes a serem inseridos: "))
for i in range(quantidadeDeNomes):
    nome = str(input("Entre com o nome " + str(i) + ": "))
    listaDeNomes.append(nome)
print("A lista de nomes é: ", listaDeNomes)

nomesQueComecamComA = [nome for nome in listaDeNomes if nome[0] == 'A']
print ("O(s) nome(s) que começa(m) com a letra A: ", nomesQueComecamComA)