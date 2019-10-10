"""
IMC
"""
print("__CALCULO DO IMC__\n")
peso   = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc    = peso / altura**2
print(imc)

if imc <= 18.5:
    print("Excesso de magreza")
elif imc <= 25.0:
    print("Peso normal")
elif imc <=30:
    print("Excesso de peso")
elif imc <=35:
    print("Obesidade grau 1")
elif imc <=40:
    print("Obesidade grau 2")
elif imc >=45:
     print("Obesidade grau 3")
else:print("Valor incorreto")
