// BLOCO 1 - Fundamentos e variáveis

// let permite mudar o valor depois.
let pontos = 50;
pontos = pontos + 10;
console.log("Pontos:", pontos);

// const não permite reatribuir. O try/catch mostra o erro sem parar o arquivo.
const MAX_PONTOS = 100;
try {
  MAX_PONTOS = 120;
} catch (erro) {
  console.log("Erro ao mudar const:", erro.name, erro.message);
  // TypeError: não podemos atribuir outro valor a uma constante.
}

// typeof mostra o tipo do valor.
const texto = "Olá";
const numero = 10;
const booleano = true;
let semValor;
const vazio = null;

console.log("string:", typeof texto);
console.log("number:", typeof numero);
console.log("boolean:", typeof booleano);
console.log("undefined:", typeof semValor);
console.log("null:", typeof vazio); // Retorna "object": comportamento antigo do JS.

// Template literal usa crase e ${} para colocar variáveis no texto.
const produto = "Caderno";
const preco = 15;
console.log(`O produto ${produto} custa R$ ${preco}.`);

// A mesma frase, agora juntando partes com +.
console.log("O produto " + produto + " custa R$ " + preco + ".");
