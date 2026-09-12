n = int(input())

coelhos = 0
ratos = 0
sapos = 0

#o que aconte nesse for é que ele itera n vezes, onde n é o número de casos de teste fornecido pelo usuário. Em cada iteração, ele lê uma linha de entrada contendo a quantidade de cobaias e o tipo de cobaia (C para coelhos, R para ratos e S para sapos).
for _ in range(n):
    quantidade, tipo = input().split()

    quantidade = int(quantidade)

    if tipo == "C":
        coelhos += quantidade

    elif tipo == "R":
        ratos += quantidade

    elif tipo == "S":
        sapos += quantidade


total = coelhos + ratos + sapos

percentual_coelhos = (coelhos / total) * 100
percentual_ratos = (ratos / total) * 100
percentual_sapos = (sapos / total) * 100


print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")