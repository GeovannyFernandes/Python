#Dicionário
#Criação de váriavel com multiplos valores
meu_dicionario = {"A":"Ameixa","B":"Bola","C":"Cachorro"}

print(meu_dicionario)

#Imprimir meu dicionario na posição chave usada no contador
for chave in meu_dicionario:
    print(meu_dicionario[chave])

#Retornando todos os itens com função
for i in meu_dicionario.items():
    print(i)