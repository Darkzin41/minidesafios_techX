# Atividade JavaScript - Semana 05

Exercícios da aula **Objetos, Dados e Assincronismo**, incluindo buscador de CEP e Mini Pokédex.

## Arquivos

- `index.html`: página com os dois formulários e as áreas de resultado.
- `app.js`: resolução das atividades, com comentários curtos no código.

## Parte 1 - Pedidos

O código cria um array de objetos e verifica se cada pedido tem cliente preenchido e valor numérico maior que zero.

- `filter()`: escolhe os pedidos válidos e depois somente os pagos.
- `reduce()`: soma os valores dos pedidos pagos.
- `map()`: cria os textos dos pedidos para mostrar no console.
- `toFixed(2)`: deixa os valores com duas casas decimais.

O resultado do exercício aparece no console (F12).

## Parte 2 - Buscador de CEP

O formulário aceita CEP com oito dígitos, com ou sem hífen. O `trim()` retira espaços e a expressão regular remove a máscara do CEP. Depois, `fetch()` consulta a API ViaCEP e `await` aguarda a resposta. O endereço é montado com `createElement()`, `textContent` e `append()`. O `replaceChildren()` limpa a pesquisa anterior.

A busca guarda os CEPs encontrados em um array de objetos e mostra o histórico na página.

API: https://viacep.com.br/ws/01001000/json/

## Parte 3 - Mini Pokédex

O nome é validado com `trim()` e convertido para minúsculo com `toLowerCase()`. O `fetch()` consulta a PokéAPI, e o JavaScript mostra nome, imagem e tipos do Pokémon. Respostas HTTP 404 mostram **Pokémon não encontrado**.

API: https://pokeapi.co/api/v2/pokemon/pikachu

## Os quatro estados da tela

1. **Carregando:** mostra "Buscando..." e desabilita o botão.
2. **Erro:** informa falha na conexão ou erro HTTP.
3. **Vazio / não encontrado:** mostra "CEP não encontrado" ou "Pokémon não encontrado".
4. **Sucesso:** exibe os dados e limpa a mensagem de status.

O `try/catch` trata falhas e o `finally` habilita novamente o botão. No CEP, `AbortSignal.timeout(5000)` limita a espera a cinco segundos. O `preventDefault()` impede o formulário de recarregar a página.

## Reflexão - Por que Promise.all pode ser mais rápido?

Com vários `await` seguidos, uma requisição espera a anterior terminar antes de começar. Quando criamos várias Promises sem esperar uma pela outra e usamos `Promise.all()`, as requisições podem ocorrer ao mesmo tempo. Assim, aproveitamos melhor o tempo de rede e esperamos todas terminarem juntas.

## Como executar

1. Deixe `index.html` e `app.js` na mesma pasta.
2. Abra `index.html` no navegador (ou use o Live Server do VS Code).
3. Abra o console com **F12** para ver o exercício de pedidos.
4. Pesquise um CEP, como `01001000`, e um Pokémon, como `pikachu`.
5. Teste CEP inválido, CEP inexistente e Pokémon inexistente para observar os avisos.

É necessário ter internet para as consultas às APIs. Não precisa instalar bibliotecas nem frameworks.

**Entrega:** publique os arquivos em um repositório do GitHub com acesso público ou liberado para quem vai corrigir.
