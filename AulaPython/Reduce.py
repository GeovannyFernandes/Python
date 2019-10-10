#Função Reduce
from functools import reduce

def soma (x,y):
    return x+y

lista = [1,2,3,4,5,6,7,8,9,10]

soma = reduce(soma, lista)
print(soma)
