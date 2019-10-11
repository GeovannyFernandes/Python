#Visualização de dados em python

import matplotlib.pyplot as plt

#Definição dos eixos criando a list
x = [1,2,3,4,5]
y = [2,3,7,1,0]
titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"
#Titulo
plt.title(titulo)
#Legendas
plt.xlabel(eixox)
plt.ylabel(eixoy)
#Criando gráfico
plt.plot (x,y)
#Gráfico com barras
plt.bar(x,y)
#Comando para exibir gráfico
plt.show()

