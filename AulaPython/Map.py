#Função Map

def dobro(x):
    return x*2

valor = [1,2,3,4,5]

valor_dobrado = map(dobro,valor)

valor_dobrado = list(valor_dobrado)

print(valor_dobrado)

#Função Lambda
#Cria uma pequena função dentro da condição, para uso exclusivo, sem precisar criar uma função def

valor = [1,2,3,4,5]

valor_dobrado = map(lambda i: i*2,valor)

valor_dobrado = list(valor_dobrado)

print(valor_dobrado)

