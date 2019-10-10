# -*- coding: utf-8 -*-
#método sort para ordenação de lista sem necessitar retornar um valor
lista = [1,2,1,2,4,5,7,8]
lista.sort
print(lista)


#Método sorted requere um valor a ser retornado
lista2 = [4,1,2,5,4,8,9,7,4]
lista2 = sorted(lista2)
print(lista2)


#Método para ordernar a lista reversa
lista2.sort(reverse=True)
print(lista2)


#Método reverse para reverter as posiçoes da lista

lista2.reverse()
print(lista2)