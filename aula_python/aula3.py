# def somar(a,b):
#     return a + b

# def mostrar(x):
#     print(x)

# r = somar(10,5)
# print(mostrar(7))

# #retorno antecipado 
# def dividir(a,b):
#     if b == 0 :
#         return None   #sai antes
#     return a/b

# #devolver varios valores
# def dividir2(a,b):
#     return a // b, a % b

# q, r = dividir2(7,2) #3 e 1
# print(q, r)

#executando apenas ação
def saudar(nome):
    return f"Ola, {nome}!"

saudar("ana")
r = saudar("ana")
print(r)