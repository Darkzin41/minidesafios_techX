// BLOCO 2 - Funções

// Função declarada funciona antes da sua declaração (hoisting).
console.log("Maior de idade (declarada):", ehMaiorDeIdade(20));

function ehMaiorDeIdade(idade) {
  return idade >= 18;
}

// Função de expressão não pode ser chamada antes de inicializar a const.
// O try/catch permite observar o ReferenceError sem interromper o arquivo.
try {
  console.log(ehMaiorDeIdadeExpressao(20));
} catch (erro) {
  console.log("Erro antes da expressão:", erro.name, erro.message);
}

const ehMaiorDeIdadeExpressao = function (idade) {
  return idade >= 18;
};
console.log("Maior de idade (expressão):", ehMaiorDeIdadeExpressao(16));

// 1) Função declarada: usa a palavra function.
function dobro(n) {
  return n * 2;
}

// 2) Expressão: a função fica guardada em uma const.
const dobroExpressao = function (n) {
  return n * 2;
};

// 3) Arrow function curta: retorno direto, sem return escrito.
const dobroArrow = (n) => n * 2;

// As três formas devem dar o mesmo resultado.
console.log("Dobro (declarada):", dobro(5));
console.log("Dobro (expressão):", dobroExpressao(5));
console.log("Dobro (arrow):", dobroArrow(5));

// Se não passar n, o valor padrão será 1.
const dobroPadrao = (n = 1) => n * 2;
console.log("Dobro sem argumento:", dobroPadrao());
