# atribuo variavel vezes para em seguida definir quantas vezes o loop vai acontecer
vezes = int(input())

# funcao para descobrir se o numero é primo ou nao (individualmente)
def eh_primo(numero):

    # Números menores que 2 não são primos
    if numero < 2:
        return f"{numero} nao eh primo"

    # Testamos possíveis divisores começando em 2
    # O próprio número não precisa ser testado
    for divisor in range(2, numero):

        # Se a divisão for exata, encontramos um divisor
        if numero % divisor == 0:
            return f"{numero} nao eh primo"
        
    # Se nenhum divisor foi encontrado, o número é primo
    return f"{numero} eh primo"

# loop para pecorrer os casos de teste, atraves do numero de vezes com o valor da variavel vezes, dai eu peço o numero pela quantidade definida, verifico se é primo com chamando a funcao e printando
for _ in range(vezes):
  n = int(input())
  resultado = eh_primo(n)
  print(resultado)
