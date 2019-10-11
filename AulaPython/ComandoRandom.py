#Método que retorna numeros ou valores aleatórios
import random
#A variável recebe o valor dado pela função, onde nos parametros são colocados o campo de numeros a serem escolhidos aleatoriamente
numero = random.randint(0,10)
print(numero)

#Retorna um valor aleatório dado uma lista
lista = [0,5,4,6,3,2,]
numero2 = random.choice(lista)
print(numero2)

