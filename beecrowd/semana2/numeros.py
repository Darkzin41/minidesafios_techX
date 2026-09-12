n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
numeros = [n1, n2, n3, n4, n5]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]
positivos = [num for num in numeros if num > 0]
negativos = [num for num in numeros if num < 0]

#num for num por que é uma expressão de compreensão de lista que itera sobre cada elemento da lista 'numeros' e seleciona apenas aqueles que atendem à condição especificada.

print(f"{len(pares)} valor(es) par(es)")
print(f"{len(impares)} valor(es) impar(es)")
print(f"{len(positivos)} valor(es) positivo(s)")
print(f"{len(negativos)} valor(es) negativo(s)")
