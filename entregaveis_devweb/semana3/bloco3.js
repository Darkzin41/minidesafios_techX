// BLOCO 3 - Controle de fluxo

// if/else escolhe o resultado de acordo com a nota.
function classificarNota(nota) {
  if (nota >= 6) {
    return "Aprovado";
  } else {
    return "Reprovado";
  }
}

console.log("Nota 8:", classificarNota(8));
console.log("Nota 4:", classificarNota(4));

// switch compara a cor com os casos disponíveis.
const corSemaforo = "amarelo";
switch (corSemaforo) {
  case "vermelho":
    console.log("Pare");
    break;
  case "amarelo":
    console.log("Atenção");
    break;
  case "verde":
    console.log("Siga");
    break;
}

// for: começa em 1, repete até 10 e soma 1 a cada volta.
console.log("Tabuada do 5:");
for (let i = 1; i <= 10; i++) {
  console.log(`5 x ${i} = ${5 * i}`);
}

// while: diminui a contagem até chegar a 1.
console.log("Contagem regressiva:");
let contagem = 5;
while (contagem >= 1) {
  console.log(contagem);
  contagem--;
}

// % 2 dá resto zero para números pares.
console.log("Pares e ímpares com for:");
for (let i = 1; i <= 20; i++) {
  if (i % 2 === 0) {
    console.log(i, "par");
  } else {
    console.log(i, "ímpar");
  }
}

// A mesma contagem, agora com while e incremento manual.
console.log("Pares e ímpares com while:");
let numero = 1;
while (numero <= 20) {
  if (numero % 2 === 0) {
    console.log(numero, "par");
  } else {
    console.log(numero, "ímpar");
  }
  numero++; // Faz a condição parar quando chegar a 21.
}

// switch também pode retornar um valor com return.
function diaDaSemana(numero) {
  switch (numero) {
    case 1: return "Domingo";
    case 2: return "Segunda-feira";
    case 3: return "Terça-feira";
    case 4: return "Quarta-feira";
    case 5: return "Quinta-feira";
    case 6: return "Sexta-feira";
    case 7: return "Sábado";
    default: return "Número inválido";
  }
}

console.log("Dia 1:", diaDaSemana(1));
console.log("Dia 4:", diaDaSemana(4));
console.log("Dia 7:", diaDaSemana(7));
console.log("Dia 9:", diaDaSemana(9)); // Teste do default.
