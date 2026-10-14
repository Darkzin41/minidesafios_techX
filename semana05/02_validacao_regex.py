import re  # Módulo usado para trabalhar com expressões regulares.


def validar_email(email):
    # Verifica o formato básico nome@dominio.com.
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(padrao, email))


def validar_cpf(cpf):
    # \d{3} significa exatamente três dígitos.
    padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    return bool(re.match(padrao, cpf))


def validar_telefone(telefone):
    # \s representa o espaço entre o DDD e o número.
    padrao = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    return bool(re.match(padrao, telefone))


def validar_data(data):
    # Formato AAAA-MM-DD.
    padrao = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(padrao, data))


# Testes simples: True = formato correto; False = formato incorreto.
print("E-mail:", validar_email("ana@email.com"))
print("CPF:", validar_cpf("123.456.789-00"))
print("Telefone:", validar_telefone("(98) 91234-5678"))
print("Data:", validar_data("2026-10-10"))
print("E-mail incorreto:", validar_email("anaemail.com"))
