nome = input("Digite o nome que deseja para o arquivo")
arquivo  = open(nome)
linhas = arquivo.readline()
for linha in linhas:
    print (linha)
