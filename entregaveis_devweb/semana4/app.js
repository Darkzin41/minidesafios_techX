// BLOCO 1 - Arrays e métodos

// forEach percorre os nomes; map cria outro array em maiúsculas.
const nomes = ["Ana", "Bruno", "Carla"];
nomes.forEach((nome) => console.log(`Olá, ${nome}!`));

const nomesMaiusculos = nomes.map((nome) => nome.toUpperCase());
console.log("Nomes em maiúsculas:", nomesMaiusculos);

// filter seleciona valores; reduce soma tudo em um único valor.
const precos = [10, 25, 40, 5, 60];
const precosCaros = precos.filter((preco) => preco > 20);
const totalPrecos = precos.reduce((soma, preco) => soma + preco, 0);
console.log("Preços acima de 20:", precosCaros);
console.log("Soma dos preços:", totalPrecos);

// Aqui os itens do array são objetos com nome e preço.
const produtos = [
  { nome: "Caderno", preco: 15 },
  { nome: "Mochila", preco: 120 },
  { nome: "Caneta", preco: 4 },
  { nome: "Lápis", preco: 2 }
];

const nomesProdutos = produtos.map((produto) => produto.nome);
const produtosBaratos = produtos.filter((produto) => produto.preco < 50);
const totalProdutos = produtos.reduce((soma, produto) => soma + produto.preco, 0);

console.log("Nomes dos produtos:", nomesProdutos);
console.log("Produtos abaixo de R$ 50:", produtosBaratos);
console.log("Quantidade de produtos baratos:", produtosBaratos.length);
console.log("Total dos produtos: R$", totalProdutos);

produtos.forEach((produto) => {
  console.log(`${produto.nome}: R$ ${produto.preco}`);
});

// BLOCO 2 - Manipulação do DOM

// querySelector encontra um elemento; querySelectorAll encontra todos.
const titulo = document.querySelector("#titulo");
titulo.textContent = "Blog do Ariel";

const textos = document.querySelectorAll(".texto");
textos.forEach((paragrafo) => console.log(paragrafo.textContent));

const lista = document.querySelector("#lista");
// O += mantém os 3 itens que já estavam escritos no HTML.
lista.innerHTML += "<li>Item 1</li><li>Item 2</li>";

// createElement cria um item; append coloca esse item na lista.
const terceiroItem = document.createElement("li");
terceiroItem.textContent = "Terceiro item";
terceiroItem.classList.add("destaque");
lista.append(terceiroItem);
console.log("Tem destaque:", terceiroItem.classList.contains("destaque"));

// forEach cria um li para cada tarefa do array.
const tarefas = ["Estudar JS", "Fazer exercícios", "Revisar DOM"];
tarefas.forEach((tarefa) => {
  const li = document.createElement("li");
  li.textContent = tarefa;
  lista.append(li);
});

// Marca o primeiro li como feito e conta todos os itens.
document.querySelector("li").classList.add("feito");
console.log("Quantidade de itens:", document.querySelectorAll("li").length);

// BLOCO 3 - Eventos e Event Delegation

const botao = document.querySelector("#botao");

// click acontece ao clicar; mouseover acontece ao passar o mouse.
botao.addEventListener("click", () => {
  console.log("Clicou!");
});

botao.addEventListener("mouseover", () => {
  botao.textContent = "Pode clicar!";
});

// keyup mostra o valor do campo depois que a tecla é solta.
const campoNome = document.querySelector("#nome");
campoNome.addEventListener("keyup", () => {
  console.log(campoNome.value);
});

// Um único evento na lista funciona para os li atuais e os futuros.
lista.addEventListener("click", (e) => {
  if (e.target.tagName === "LI") {
    e.target.classList.toggle("feito");
    console.log("Item clicado:", e.target.textContent);
  }
});

// Este novo item também funciona com o mesmo evento da lista.
const novoItem = document.createElement("li");
novoItem.textContent = "Item criado com JavaScript";
lista.append(novoItem);

// O submit não recarrega a página; espaços vazios são ignorados.
const formulario = document.querySelector("#formulario");
const campoTarefa = document.querySelector("#tarefa");

formulario.addEventListener("submit", (e) => {
  e.preventDefault();
  const tarefa = campoTarefa.value.trim();

  if (tarefa === "") {
    return; // Não adiciona tarefa vazia.
  }

  const li = document.createElement("li");
  li.textContent = tarefa;
  lista.append(li);
  campoTarefa.value = ""; // Limpa o campo depois de adicionar.
});
