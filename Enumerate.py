#Função enumerate

lista = ["Abacate","Bola","Cachorro"]

#Forma Simples
#Comando Range: Cria um vetor
#Comando Len: Ele resgata o tomanho da lista de acordo com os indices
for i in range(len(lista)):
    print(i, lista[i])

#Utilizando o Enumerate
for i, nome in enumerate(lista):
    print(i, nome)