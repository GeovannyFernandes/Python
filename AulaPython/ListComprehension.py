#Compreensão de Lista
#Simples
x = [1,2,3,4,5]
y =[]

for i in x:
    y.append(i**2)
print(x)
print(y)

#Com o comprehension

y = [i**2 for i in x]

#Condição para adicionar a Z apenas se for impar. com o mod 2 = 1
z = [i for i in x if i%2==1]
print(x)
print(y)
print(z)
