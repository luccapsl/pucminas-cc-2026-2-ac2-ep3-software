# ULA 4 bits — Software do PC

Montador do Exercício Prático 03 da disciplina de Arquitetura de Computadores 2 (Ciência da Computação, PUC Minas, 2026/2).

**Grupo:** Ana Flávia, Clarisse de Assis, Jamille Micaele, Júlia Batista, Lucca de Paula.

Este repositório contém **apenas o lado PC**. O firmware do Arduino (ULA, vetor memória, PC, DUMP e LEDs) está em repositório separado, mantido pelos integrantes responsáveis pelo hardware.

## Contexto do exercício

O sistema completo tem duas partes:

1. **PC (este repositório):** lê o programa fonte `testeula.ula`, escrito com os mnemônicos da ULA, e gera o programa executável `testeula.hex`.
2. **Arduino:** recebe o conteúdo do `testeula.hex` pela serial, carrega todas as instruções no vetor memória e só então as executa, uma a cada 4 segundos, mostrando o resultado nos LEDs dos pinos 13 (F3), 12 (F2), 11 (F1) e 10 (F0) e um DUMP da memória após cada instrução.

O Arduino executa o `.hex`, nunca o `.ula`.

## O que este programa faz

1. Lê o arquivo `testeula.ula` da pasta atual e normaliza cada linha.
2. Confere se o programa começa com `inicio:` e termina com `fim.`.
3. Interpreta as atribuições `X=` e `Y=` e mantém o valor vigente de cada uma.
4. Traduz cada `W=<mnemônico>;` em uma palavra hexadecimal de 3 dígitos (`XYS`).
5. Grava o resultado em `testeula.hex`, uma instrução por linha.

O programa **não se comunica com o Arduino**. Sua única saída é o arquivo `testeula.hex`, levado ao Arduino manualmente pelo Monitor Serial.

## Requisitos

- Python 3
- Nenhuma biblioteca externa

## Uso

```bash
python3 main.py
```

O programa não recebe argumentos. Os nomes dos arquivos de entrada e saída estão fixos em [variaveis.py](variaveis.py) (`testeula.ula` e `testeula.hex`), como exige a especificação, e são procurados na pasta onde o comando é executado.

Exemplo de saída no console:

```
[INFO] - Inicio do programa de montagem de arquivo .ula para .hex

[INFO] - Leitura do arquivo testeula.ula realizada com sucesso.

[INFO] - Montagem do conteudo hexadecimal realizada com sucesso.

[INFO] - Escrita do arquivo testeula.hex realizada com sucesso.
```

## Como levar o .hex ao Arduino

1. Abra o Monitor Serial da IDE do Arduino, com o firmware do grupo já gravado na placa.
2. Ajuste o baud rate e o terminador de linha conforme definido no repositório do Arduino.
3. Abra o `testeula.hex` e copie **todo** o conteúdo.
4. Cole no campo "Enviar" e envie de uma vez.

A especificação exige que a carga seja feita em bloco único. Não se digita uma instrução de cada vez.

## Estrutura do repositório

```
.
├── main.py            # ponto de entrada: orquestra leitura, montagem e gravação
├── gestao_arquivo.py  # leitura do .ula e escrita do .hex
├── tratador.py        # limpeza das linhas, extração de números e mnemônicos, conversão para hexa
├── validador.py       # validações: inicio/fim, variáveis, '=', ';', faixa de 4 bits, mnemônico
├── montador.py        # percorre o fonte, mantém X e Y e monta as palavras XYS
├── mnemonicos.py      # tabela dos 16 mnemônicos e seus códigos
├── variaveis.py       # nomes dos arquivos e listas globais de conteúdo
├── testeula.ula       # fonte de teste do grupo
├── testeula.hex       # saída gerada
└── README.md
```

### Fluxo de execução

```
main.py
 ├─ gestao_arquivo.ler_arquivo_ula()   → lista de linhas já limpas (tratador.limpeza_texto_linha)
 ├─ validador.validar_conteudo_vazio() → aborta se o arquivo não existe ou está vazio
 ├─ montador.montagem_texto_hexa()     → valida linha a linha e preenche conteudoHexadecimal
 └─ gestao_arquivo.escrever_arquivo_hex() → grava testeula.hex
```

## Formato do fonte (.ula)

```
inicio:
X=12;
Y=6;
W=AeB;
X=10;
Y=3;
W=AoB;
W=AeBn;
X=13;
W=nB;
fim.
```

Regras:

- A primeira linha deve ser `inicio:` e a última, `fim.`.
- `X=` e `Y=` recebem valores **decimais** de 0 a 15 e **não geram linha no `.hex`**. Apenas atualizam o estado interno do montador.
- `W=<mnemônico>;` gera uma linha no `.hex`, usando os valores de X e Y vigentes naquele momento.
- X e Y permanecem válidos até uma nova atribuição. É por isso que as dez linhas de instrução do exemplo produzem quatro linhas de saída.
- X e Y iniciam em 0 caso uma operação apareça antes de qualquer atribuição.
- Toda linha entre `inicio:` e `fim.` deve terminar em `;`.
- Espaços e finais de linha (`\n`, `\r`) são removidos antes da análise, então `X = 12 ;` é aceito.
- Os mnemônicos são comparados por igualdade exata com a tabela, diferenciando maiúsculas de minúsculas.

## Conjunto de instruções

| Função | Mnemônico | Código |
|---|---|---|
| A' | `nA` | 0 |
| (A+B)' | `AoBn` | 1 |
| A'·B | `nAeB` | 2 |
| 0 | `zeroL` | 3 |
| (A·B)' | `AeBn` | 4 |
| B' | `nB` | 5 |
| A'·B + A·B' | `AxB` | 6 |
| A·B' | `AenB` | 7 |
| A' + B | `nAoB` | 8 |
| A·B + A'·B' | `AxBn` | 9 |
| B | `copiaB` | A |
| A·B | `AeB` | B |
| 1 | `umL` | C |
| A + B' | `AonB` | D |
| A + B | `AoB` | E |
| A | `copiaA` | F |

As operações são sempre realizadas sobre X e Y, e o resultado vai para W. A tabela está em [mnemonicos.py](mnemonicos.py).

## Formato da saída (.hex)

Uma instrução por linha, três dígitos hexadecimais maiúsculos, sem separadores:

```
C6B
A3E
A34
D35
```

Leitura de cada palavra: primeiro dígito = X, segundo = Y, terceiro = S (instrução).

### Rastreamento do exemplo acima

| Linhas do fonte | X | Y | S | Saída |
|---|---|---|---|---|
| `X=12; Y=6; W=AeB;` | 12 → C | 6 → 6 | `AeB` → B | `C6B` |
| `X=10; Y=3; W=AoB;` | 10 → A | 3 → 3 | `AoB` → E | `A3E` |
| `W=AeBn;` | A (mantido) | 3 (mantido) | `AeBn` → 4 | `A34` |
| `X=13; W=nB;` | 13 → D | 3 (mantido) | `nB` → 5 | `D35` |

### Execução no Arduino

Com `C6B`: X = 1100, Y = 0110, S = 1011 (`AeB`, o "e" das entradas). O resultado é 0100, ou seja W = 4, com o LED do pino 12 aceso.

Com `A3E` em seguida: X = 1010, Y = 0011, S = 1110 (`AoB`). O resultado é 1011, ou seja W = B, com os LEDs dos pinos 13, 11 e 10 acesos.

DUMP esperado do vetor memória (`PC | W | X | Y | instruções...`) para esse programa de duas instruções:

```
- >| 4 | 0 | 0 | 0 | C6B | A3E |    carga do vetor
- >| 5 | 4 | C | 6 | C6B | A3E |    após a 1ª instrução
- >| 6 | B | A | 3 | C6B | A3E |    após a 2ª instrução
```

## Tratamento de erros

Mensagens emitidas pela versão atual:

| Situação | Mensagem |
|---|---|
| Arquivo `.ula` não encontrado | `[ERRO] - Arquivo com nome testeula.ula nao foi encontrado. Leitura impossivel de ser realizada.` |
| Arquivo vazio | `[ERRO] - Conteudo do arquivo esta vazio!` |
| Primeira linha diferente de `inicio:` | `[ERRO] - linha (0) - Texto de inicio '...' invalido.` |
| Linha sem `;` (inclui linha em branco) | `[ERRO] (linha N) - Conteudo '...' invalido. Erro de sintaxe.` |
| Variável diferente de `X`, `Y` ou `W` | `[ERRO] (linha N) - Caractere ... Invalido.` |
| Falta `=` após a variável | `[ERRO] - Necessario operador '=' apos variavel.` |
| Mnemônico inexistente | `[ERRO] (linha N) - Mnemonico ... Invalido.` seguido da lista de mnemônicos válidos |

Também é validada a faixa de 4 bits (0 a 15) dos valores de X e Y.

Na versão atual, **o primeiro erro interrompe a montagem**: o conteúdo já traduzido é descartado e o `testeula.hex` não é gravado (`[ERRO] - Montagem do arquivo .hex nao realizada devido a erros de sintaxe.`). Isso ainda não atende à especificação — ver [Pendências](#pendências-em-relação-à-especificação).

## Arquivo de teste

O `testeula.ula` atual contém o exemplo da especificação (Figura 3) acrescido de repetições de `W=nB;`, cobrindo o reaproveitamento de X e Y sem reatribuição.

A especificação pede que o arquivo de teste do grupo cubra:

- as 16 instruções da tabela;
- reaproveitamento de X e Y sem reatribuição;
- `zeroL` e `umL`, que ignoram as entradas;
- uma ou mais linhas em branco no meio do programa;
- instruções com sintaxe errada.

O arquivo usado na avaliação é outro e só será conhecido no momento da apresentação.

## Pendências em relação à especificação

- [ ] **Erros não podem interromper a tradução.** A especificação exige que linhas em branco e instruções com sintaxe errada sejam informadas e que a carga continue normalmente (item 7 dos critérios de perda de pontos). Hoje o montador para no primeiro erro e não grava o `.hex`.
- [ ] **Linha em branco** deve gerar um aviso próprio e ser ignorada; hoje ela cai no erro genérico de sintaxe.
- [ ] **`X=` ou `Y=` sem número** (ex.: `X=;`) provoca exceção (`int('')`) em `tratador.tratar_numero`, encerrando o programa.
- [ ] **Valor fora da faixa** (ex.: `X=20;`) interrompe a montagem sem exibir mensagem.
- [ ] **`inicio:` ausente** exibe o erro, mas o fluxo segue como sucesso e grava um `.hex` vazio.
- [ ] **Linha em branco após `fim.`** é tratada como erro, porque `fim.` precisa ser a última linha da lista.
- [ ] **Tabulações** não são removidas por `tratador.limpeza_texto_linha` (apenas espaços, `\n` e `\r`).
- [ ] **Exibir o conteúdo do `.hex` na tela** ao final, pronto para copiar, e um resumo com a contagem de erros e de instruções geradas.
- [ ] **Arquivo de teste** cobrindo as 16 instruções e os dois tipos de erro.

## Divisão de trabalho (lado PC)

### Lucca — Etapas 1 e 2

**Etapa 1 — Leitura e tradução (`gestao_arquivo.py`, `tratador.py`, `montador.py`, `mnemonicos.py`)**

- Abertura e leitura do `.ula`, com numeração das linhas a partir de 1
- Normalização de espaços, tabulações e `CRLF`
- Reconhecimento de `inicio:` e `fim.`
- Parsing de `X=` e `Y=` e manutenção do estado interno
- Tabela dos 16 mnemônicos
- Conversão decimal → hexadecimal de X e Y
- Montagem da palavra `XYS`

**Etapa 2 — Validação (`validador.py`)**

- Linha em branco
- Falta de ponto e vírgula
- Variável desconhecida à esquerda do `=`
- Mnemônico inexistente
- Valor fora da faixa de 4 bits
- Padronização das mensagens `[ERRO]` / `[AVISO]` / `[INFO]`
- Garantia de que nenhum erro interrompe a tradução

### Clarisse — Etapas 3 e 4

**Etapa 3 — Pendências e correções (todos os módulos)**

- Resolução de todas as [pendências em relação à especificação](#pendências-em-relação-à-especificação), de acordo com o `EP03_2026_2.pdf`
- Correção do que ainda resta no código do lado PC, em especial:
  - erros relatados sem interromper a tradução nem a gravação do `.hex`;
  - aviso próprio para linha em branco;
  - tratamento de `X=`/`Y=` sem número e de valores fora da faixa, com mensagem;
  - fluxo correto quando falta `inicio:` ou há linhas após `fim.`;
  - remoção de tabulações na normalização;
  - ajuste dos nomes invertidos de `validar_x` / `validar_y`
- Exibição do conteúdo do `.hex` na tela, pronto para copiar e colar
- Resumo final com contagem de erros e de instruções geradas

**Etapa 4 — Cobertura de testes e conferência (`testeula.ula`)**

- Cobertura das 16 instruções da tabela
- Reaproveitamento de X e Y sem reatribuição
- `zeroL` e `umL`, que ignoram as entradas
- Os dois casos de erro (sintaxe e linha em branco)
- Conferência do `.hex` gerado contra o resultado esperado, calculado à mão
- Conferência do resultado no Arduino, LED a LED, junto com a equipe de hardware

### Regras comuns

- **Contrato entre as etapas:** a montagem entrega a lista de palavras `XYS` (`conteudoHexadecimal`, em [variaveis.py](variaveis.py)) e a lista de erros; a saída grava e exibe. O formato dessas listas é combinado antes de começar e não muda depois.
- **Formato de linha do `.hex`:** acertado com o responsável pela memória do Arduino.
- Cada um comenta o próprio código; comentários são critério explícito de nota.
- Cada um revisa o código do outro antes de a etapa ser considerada pronta.
- Ambos treinam o rastreamento completo de `C6B`, do fonte `.ula` até os LEDs acesos. A avaliação é individual, durante a apresentação, e nenhuma parte do fluxo pode ser desconhecida por qualquer um dos dois.
