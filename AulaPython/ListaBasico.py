# -*- coding: utf-8 -*-
#Comando append adiciona ao final da lista
from Lista import lista1

lista = [1,2,3,5]

lista.append(3)
print(lista)

#Pesquisa para saber se o elemento é existente na lista
n = int(input("Digite um valor:"))
if n in lista:
     print("Está contido na lista")
else:
     print("Não esta contido")

#Comando para deletar um elemento da lista

del lista[1]
print(lista)

#Adicionando valores a lista

lista01.append(30)
print(lista01)