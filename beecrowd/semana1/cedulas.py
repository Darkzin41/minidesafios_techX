cedulas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())
if valor > 0 and valor < 1000000:
    print(valor)
    for cedula in cedulas:
        quantidade = valor // cedula
        print(f"{quantidade} nota(s) de R$ {cedula},00")
        valor -= quantidade * cedula

#explicando o for 
# para cada cédula:
#     calcular quantas vezes ela cabe no valor restante
#     mostrar a quantidade
#     retirar do valor as notas já utilizadas