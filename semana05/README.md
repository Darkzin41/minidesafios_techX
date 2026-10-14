# Sprint 5: Sistema de Análise de Dados em Python

Projeto da Aula 5: **manipulação de arquivos, expressões regulares e tratamento de exceções**.

## Como executar

1. Abra a pasta do projeto no terminal ou no VS Code.
2. Execute `python main.py`.
3. Veja o resultado no terminal e no arquivo `relatorio.txt`.

Não precisa instalar bibliotecas: `csv` e `re` já vêm com o Python.

## Arquivos

- `01_manipulacao_arquivos.py`: abre `dados.csv` com `with open()` e imprime `read()`.
- `02_validacao_regex.py`: testa as quatro funções de validação.
- `03_tratamento_excecoes.py`: mostra `try`, `except`, `else` e `finally`.
- `04_excecao_personalizada.py`: cria e usa `FormatoInvalidoError`.
- `05_relatorio_formatado.py`: cria `relatorio_exemplo.txt` com f-strings.
- `main.py`: reúne todos os requisitos da Sprint.
- `dados.csv`: registros fictícios para testar o programa.
- `relatorio.txt`: relatório que o `main.py` gera ao executar.

## Validações e justificativas

As validações usam o módulo `re`, seguindo os padrões trabalhados nos slides:

| Campo | Formato esperado | Motivo |
|---|---|---|
| E-mail | `nome@dominio.com` | Impedir texto sem estrutura básica de e-mail |
| CPF | `000.000.000-00` | Exigir pontuação e quantidade de dígitos |
| Telefone | `(00) 00000-0000` | Exigir DDD, espaço e número formatado |
| Data | `AAAA-MM-DD` | Padronizar o formato das datas |

**Importante:** regex verifica o formato, mas não garante que o CPF seja matematicamente válido, que a data exista no calendário ou que o e-mail funcione. A coluna `idade` foi incluída apenas para praticar a conversão `int()` e o erro `ValueError`.

## Exceções tratadas

- `FileNotFoundError`: arquivo CSV não encontrado.
- `KeyError`: coluna necessária não existe.
- `ValueError`: não foi possível converter a idade em número.
- `FormatoInvalidoError`: exceção personalizada usada quando o formato de um dos campos está incorreto.
- `else`: gera relatório se a leitura principal não falhar.
- `finally`: mostra que a análise terminou, com ou sem erro.

## Exemplo de entrada

Trecho de `dados.csv`:

```csv
nome,email,cpf,telefone,data,idade
Ana,ana@email.com,123.456.789-00,(98) 91234-5678,2026-10-10,25
Bruno,brunoemail.com,987.654.321-00,(98) 99876-5432,2026-10-11,20
```

## Exemplo de saída

```text
RELATÓRIO DE ANÁLISE DE DADOS
Total de registros: 7
Válidos: 2
Inválidos: 5

REGISTROS VÁLIDOS:
- Ana (25 anos)
- Gabriela (30 anos)

REGISTROS INVÁLIDOS:
- Bruno: e-mail inválido
- Carla: CPF fora do formato
- Diego: telefone fora do formato
- Eva: data fora do formato
- Felipe: invalid literal for int() with base 10: 'abc'
```

## Entrega

Publique os arquivos deste projeto em um repositório público do GitHub e envie o link no AVA.
