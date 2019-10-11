#Visualização de dados em python
#Grafico de pontos

import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2,3,7,1,0]
titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"
#Titulo
plt.title(titulo)
#Legendas
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Gráfico de pontos
plt.scatter(x,y, label = "Meus Pontos", color = "b")
#Ligando o gráfico de pontos ao de linhas
plt.plot(x,y)

plt.show()

