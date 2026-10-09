def sacar(saldo, valor):
    if valor > saldo:
        raise ValueError("Saldo Insuficiente para realizar o saque!!")
    return saldo - valor
try: 
    sacar(100,200)
except ValueError as e:
    print(e)
