# Calculadora de Orçamento de Viagem

## Descrição

A **Calculadora de Orçamento de Viagem** é uma ferramenta desenvolvida em Python para ser executada diretamente pelo terminal. O programa permite que o usuário informe os principais gastos relacionados a uma viagem e calcule automaticamente o valor total necessário.

Além do cálculo do orçamento total, o programa também permite informar se a viagem será realizada por mais de uma pessoa. Nesse caso, o valor total é dividido igualmente entre os participantes.

## Objetivo

O objetivo do projeto é fornecer uma ferramenta simples para auxiliar no planejamento financeiro de uma viagem. Por meio da inserção dos principais gastos previstos, o usuário pode obter uma estimativa do custo total da viagem e, quando necessário, saber quanto cada participante deverá contribuir.

## Funcionalidades

O programa possui as seguintes funcionalidades:

* Cálculo do valor total da viagem;
* Registro dos valores de transporte;
* Registro dos valores de hospedagem;
* Registro dos valores de alimentação;
* Registro dos gastos com passeios e entretenimento;
* Registro dos gastos com deslocamento;
* Registro de gastos adicionais;
* Inclusão de uma reserva de emergência;
* Validação para impedir valores negativos;
* Validação de entradas numéricas inválidas;
* Divisão do valor total entre os participantes;
* Exibição de um resumo completo do orçamento.

## Categorias de Gastos

O programa considera as seguintes categorias para o cálculo do orçamento:

* **Transporte:** gastos relacionados à ida e volta da viagem;
* **Hospedagem:** valores gastos com hotéis, pousadas ou outras formas de acomodação;
* **Alimentação:** gastos previstos com café da manhã, almoço e jantar;
* **Passeios e Entretenimento:** custos relacionados a atividades, atrações e lazer;
* **Deslocamento:** gastos com transporte durante a viagem, como táxi, Uber ou outros meios;
* **Gastos Adicionais:** despesas extras, como compras;
* **Reserva de Emergência:** valor separado para possíveis despesas inesperadas.

## Como o Programa Funciona

O funcionamento do programa segue as seguintes etapas:

1. O usuário informa os valores previstos para cada categoria de gasto.
2. O programa valida os valores informados, impedindo números negativos e entradas inválidas.
3. Todos os gastos são somados para calcular o custo total da viagem.
4. O usuário informa se os gastos serão divididos entre várias pessoas.
5. Caso a viagem tenha mais de um participante, o programa calcula o valor que cada pessoa deverá pagar.
6. Por fim, um resumo completo do orçamento é exibido no terminal.

## Estrutura do Código

O projeto é dividido em funções para organizar melhor o código.

### `obter_valor_positivo()`

Solicita um valor ao usuário e verifica se a entrada é um número válido e não negativo.

### `obter_numero_participantes()`

Pergunta se os gastos serão divididos entre participantes. Caso a resposta seja positiva, solicita e valida a quantidade de pessoas.

### `exibir_resumo()`

Exibe no terminal todos os gastos informados, o valor total da viagem e, quando aplicável, o valor correspondente a cada participante.

### `calcular_orcamento_viagem()`

É a função principal do programa. Ela solicita os gastos, calcula o valor total, verifica o número de participantes e exibe o resumo final.

## Exemplo de Uso

```text
Bem-vindo ao programa de cálculo de orçamento de viagem!

Digite o valor total do transporte: 500
Digite o valor total da hospedagem: 800
Digite o valor total da alimentação: 400
Digite o valor total dos passeios e entretenimentos: 300
Digite o valor total do deslocamento: 150
Digite o valor total dos gastos adicionais: 200
Digite o valor total da reserva de emergência: 300

Essa é uma viagem em grupo onde os participantes irão dividir os gastos? (sim/não): sim
Digite o número de participantes da viagem: 2
```

Após o preenchimento dos valores, o programa exibe um resumo contendo os gastos individuais, o custo total da viagem e o valor correspondente a cada participante.

## Possíveis Melhorias Futuras

Algumas melhorias que podem ser implementadas futuramente são:

* Cálculo do custo médio por dia de viagem;
* Inclusão de novas categorias de gastos
* Geração de recomendações com base nos valores informados.