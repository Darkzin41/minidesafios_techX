#codigo da atividade media de notas melhorado, com estudo ativo pensando em sistemas de notas (ampliando o estudo - trabalhando com listas, funções e condicionais)
notas = list(map(float, input("Digite as 3 notas do aluno: ").split()))

def validar_notas(notas):
    if not notas:
        raise ValueError("É necessário inserir numeros validos, ou pelo menos uma nota")
    
    for nota in notas:
        if nota < 0 or nota > 10:
            raise ValueError("A nota é invalida")
    return True

def calcular_media(notas):
    validar_notas(notas) 
    
    return sum(notas) / len(notas)

def determinar_situacao():
    if media >= 9.0:
        return "Aprovado com louvor"
    elif media >= 7.0:
        return "Aprovado"
    
    return "Reprovado"

media = calcular_media(notas)
situacao = determinar_situacao()

print(f"Média do aluno: {media:.2f}")
print(f"Situação do aluno: {situacao}")

    