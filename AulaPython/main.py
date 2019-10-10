import media as m
import aleatorio as a

lista = a.geraListaInteiro(10)
print(lista)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print("Minha lista:")
print(lista)
print("A média da minha lista é " + str(media))
print("A mediana da minha lista é " + str(mediana))
print("A moda da minha lista é " + str(moda))

