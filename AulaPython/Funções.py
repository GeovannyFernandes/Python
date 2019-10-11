#Criação de funções, sempre será criada pela palavra def

def soma (x,y):
    return x+y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
def sub(x,y):
    return x-y

#Chamando a função e fornecendo parâmetros

s = soma(24,30)
print(s)
m = mult(2,8)
print(m)
d = div(10,2)
print(d)
su = sub(50,20)
print(su)

#E depois com valores recebidos da função

total = soma(s,m)
print(total)