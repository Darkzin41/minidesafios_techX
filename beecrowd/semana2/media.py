N1, N2, N3, N4 = map(float, input().split())

notas = [N1, N2, N3, N4]
pesos = [2, 3, 4, 1]

# funcao pra calcular a media das notas junto aos pesos, retornando a media ponderada
def calcular_media(notas, pesos):
    soma = 0

    for nota, peso in zip(notas, pesos):
         #pecorre nota e peso em notas e pesos ao mesmo tempo
        soma += nota * peso 
        #adiciona ao valor da soma a nota multiplicada pelo peso correspondente

    return soma / sum(pesos)
#esse return retorna a soma das notas multiplicadas pelos pesos dividido pela soma dos pesos, que é a media ponderada


media = calcular_media(notas, pesos)

print(f"Media: {media:.1f}")

#condicionais de nota
if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")

    nota_exame = float(input())

    print(f"Nota do exame: {nota_exame:.1f}")

    media_final = (media + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")

    else:
        print("Aluno reprovado.")

    print(f"Media final: {media_final:.1f}")