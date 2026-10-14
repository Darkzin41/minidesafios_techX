import re


# Criamos nossa própria exceção herdando de Exception.
class FormatoInvalidoError(Exception):
    pass


def verificar_email(email):
    # Se o e-mail não seguir o padrão, lançamos o erro com raise.
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(padrao, email):
        raise FormatoInvalidoError("E-mail fora do formato esperado.")
    return True


try:
    verificar_email("email_sem_arroba")
except FormatoInvalidoError as erro:
    # A variável erro recebe a mensagem da exceção.
    print(f"Erro: {erro}")
else:
    print("E-mail válido.")
