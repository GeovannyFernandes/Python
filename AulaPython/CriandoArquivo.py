#Arquivos
#Abrindo arquivo
arquivo = open("arquivo.txt")

#Criando uma vareável para receber as linhas do arquivo com o readline
linhas = arquivo.readline()
print(linhas)

for linha in linhas:
    print(linha)

#Imprimindo o arquivo completo

texto_completo = arquivo.read()
print(texto_completo)

