# Atividade JavaScript - Semana 04

Exercícios da aula **Arrays, DOM e Eventos**, divididos em três blocos.

## Arquivos

- `index.html`: página com título, parágrafos, botão, campos, formulário e lista.
- `app.js`: resolução das atividades com comentários curtos.

## Bloco 1 - Arrays

- `forEach()`: percorre os itens para executar uma ação, sem criar outro array.
- `map()`: cria um novo array transformando cada item.
- `filter()`: cria um novo array com os itens que passam em uma condição.
- `reduce()`: percorre os itens e acumula um resultado, como uma soma.

## Bloco 2 - DOM

`querySelector()` busca o primeiro elemento, e `querySelectorAll()` busca todos os que combinam com o seletor. `textContent` muda o texto; `innerHTML` permite inserir tags HTML. `createElement()` cria um elemento, `append()` o coloca na página e `classList` adiciona ou altera classes CSS.

## Bloco 3 - Eventos

`addEventListener()` acompanha os eventos de clique, mouse e teclado. No formulário, `preventDefault()` evita o recarregamento e `trim()` impede adicionar tarefas só com espaços.

**Event Delegation:** usamos apenas um listener de `click` na lista (`#lista`). Com `e.target.tagName === "LI"`, verificamos se o clique foi em um item. Isso evita colocar um listener em cada `li` e também funciona com itens criados depois pelo JavaScript.

## Como executar

1. Deixe `index.html` e `app.js` na mesma pasta.
2. Abra o `index.html` no navegador, ou use Live Server no VS Code.
3. Abra o console com **F12** para ver os resultados dos arrays e as mensagens dos eventos.
4. Teste passar o mouse e clicar no botão, digitar no campo de nome, clicar nos itens e adicionar tarefas pelo formulário.

Não precisa instalar bibliotecas ou usar Node.js: as atividades de DOM e eventos são executadas no navegador.
