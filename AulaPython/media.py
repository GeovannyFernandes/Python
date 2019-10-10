#Média, Mediana e a Moda
#Biblioteca para resolver problemas com média
from statistics import *

def media(lista):
    media = sum(lista)/float(len(lista))

    return media

def mediana(lista):
    return median(lista)

def moda(lista):
    return mode(lista)