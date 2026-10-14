// PARTE 1 - Manipulação e validação de pedidos

// Array de objetos usado no exercício guiado da aula.
const pedidos = [
  { cliente: "Bia", valor: 120, status: "pago" },
  { cliente: "", valor: 45, status: "pago" },
  { cliente: "Caio", valor: "abc", status: "pendente" },
  { cliente: "Duda", valor: 310.5, status: "pago" }
];

// filter mantém só clientes preenchidos e valores numéricos acima de zero.
const pedidosValidos = pedidos.filter((pedido) =>
  pedido.cliente.trim() !== "" &&
  Number.isFinite(Number(pedido.valor)) &&
  Number(pedido.valor) > 0
);

// Dos pedidos válidos, ficam apenas os pagos.
const pedidosPagos = pedidosValidos.filter((pedido) => pedido.status === "pago");

// reduce soma os valores; map cria os textos com duas casas decimais.
const totalFaturado = pedidosPagos.reduce((total, pedido) => total + Number(pedido.valor), 0);
const resumoPedidos = pedidosPagos.map((pedido) =>
  `${pedido.cliente} — R$ ${Number(pedido.valor).toFixed(2)}`
);

console.log("Pedidos válidos:", pedidosValidos);
console.log("Pedidos pagos:", pedidosPagos);
console.log("Total faturado: R$", totalFaturado.toFixed(2));
console.log("Resumo:", resumoPedidos);

// PARTE 2 - Buscador de CEP

const formCep = document.querySelector("#formCep");
const inputCep = document.querySelector("#cep");
const botaoCep = document.querySelector("#botaoCep");
const statusCep = document.querySelector("#statusCep");
const resultadoCep = document.querySelector("#resultadoCep");
const listaHistorico = document.querySelector("#historicoCep");
const historico = []; // Guarda cada busca realizada com sucesso.

// Cria os elementos dt e dd para mostrar os dados do endereço.
function mostrarEndereco(dados) {
  resultadoCep.replaceChildren(); // Limpa o resultado anterior.

  const campos = [
    ["Rua", dados.logradouro],
    ["Bairro", dados.bairro],
    ["Cidade", dados.localidade],
    ["UF", dados.uf]
  ];

  for (const [rotulo, valor] of campos) {
    const dt = document.createElement("dt");
    const dd = document.createElement("dd");
    dt.textContent = rotulo;
    dd.textContent = valor || "Não informado";
    resultadoCep.append(dt, dd);
  }
}

// Mostra o histórico usando os dados guardados no array.
function mostrarHistorico() {
  listaHistorico.replaceChildren();

  historico.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = `${item.cep} - ${item.cidade}/${item.uf}`;
    listaHistorico.append(li);
  });
}

formCep.addEventListener("submit", async (e) => {
  e.preventDefault(); // Evita recarregar a página.
  resultadoCep.replaceChildren();

  // trim tira espaços das pontas; a regex retira o hífen do CEP.
  const cep = inputCep.value.trim().replace(/-/g, "");

  if (!/^\d{8}$/.test(cep)) {
    statusCep.textContent = "CEP deve ter 8 dígitos";
    return;
  }

  statusCep.textContent = "Buscando...";
  botaoCep.disabled = true;

  try {
    // fetch faz a busca; await espera a resposta e a conversão do JSON.
    const resposta = await fetch(`https://viacep.com.br/ws/${cep}/json/`, {
      signal: AbortSignal.timeout(5000)
    });

    if (!resposta.ok) throw new Error(`HTTP ${resposta.status}`);

    const dados = await resposta.json();

    if (dados.erro) {
      statusCep.textContent = "CEP não encontrado";
      return;
    }

    mostrarEndereco(dados);
    statusCep.textContent = ""; // Sucesso: tira o aviso.

    // Bônus: salva e mostra o CEP pesquisado no histórico.
    historico.push({ cep, cidade: dados.localidade, uf: dados.uf });
    mostrarHistorico();
  } catch (erro) {
    // Erros de internet, HTTP, tempo limite ou JSON aparecem aqui.
    statusCep.textContent = "Falha na conexão. Tente de novo.";
  } finally {
    botaoCep.disabled = false; // Libera o botão em qualquer situação.
  }
});

// PARTE 3 - Mini Pokédex

const formPokemon = document.querySelector("#formPokemon");
const inputPokemon = document.querySelector("#nomePokemon");
const botaoPokemon = document.querySelector("#botaoPokemon");
const statusPokemon = document.querySelector("#statusPokemon");
const resultadoPokemon = document.querySelector("#resultadoPokemon");

// Monta o resultado com textContent e createElement, sem innerHTML.
function mostrarPokemon(dados) {
  resultadoPokemon.replaceChildren();

  const nome = document.createElement("h3");
  nome.textContent = dados.name;
  resultadoPokemon.append(nome);

  const imagem = document.createElement("img");
  if (dados.sprites.front_default) {
    imagem.src = dados.sprites.front_default;
    imagem.alt = `Imagem de ${dados.name}`;
    resultadoPokemon.append(imagem);
  }

  const tipos = document.createElement("p");
  tipos.textContent = `Tipos: ${dados.types.map((item) => item.type.name).join(", ")}`;
  resultadoPokemon.append(tipos);
}

formPokemon.addEventListener("submit", async (e) => {
  e.preventDefault();
  resultadoPokemon.replaceChildren();

  // Deixa a busca sem espaços nas pontas e em letras minúsculas.
  const nome = inputPokemon.value.trim().toLowerCase();

  if (nome === "") {
    statusPokemon.textContent = "Digite o nome de um Pokémon";
    return;
  }

  statusPokemon.textContent = "Buscando...";
  botaoPokemon.disabled = true;

  try {
    const resposta = await fetch(`https://pokeapi.co/api/v2/pokemon/${encodeURIComponent(nome)}`);

    // A API usa HTTP 404 quando o Pokémon não existe.
    if (resposta.status === 404) {
      statusPokemon.textContent = "Pokémon não encontrado";
      return;
    }

    if (!resposta.ok) throw new Error(`HTTP ${resposta.status}`);

    const dados = await resposta.json();
    mostrarPokemon(dados);
    statusPokemon.textContent = ""; // Sucesso: limpa o aviso.
  } catch (erro) {
    statusPokemon.textContent = "Falha na conexão. Tente de novo.";
  } finally {
    botaoPokemon.disabled = false;
  }
});
