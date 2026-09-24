# ULA 4 bits — Software do PC

Montador do Exercício Prático 03 da disciplina de Arquitetura de Computadores 2.

Este repositório contém **apenas o lado PC**. O firmware do Arduino está em repositório separado, mantido pelos três integrantes responsáveis pelo hardware.

## O que este programa faz

1. Lê o arquivo fonte `testeula.ula`, escrito com os mnemônicos da ULA.
2. Detecta erros no fonte (sintaxe inválida e linhas em branco), reporta e **continua** a tradução.
3. Traduz cada operação em uma palavra hexadecimal de 3 dígitos (`XYS`).
4. Grava o resultado em `testeula.hex` e exibe o conteúdo na tela.

O programa **não se comunica com o Arduino**. Sua única saída é o arquivo `testeula.hex`, que é levado ao Arduino manualmente pelo Monitor Serial. O Arduino executa o `.hex`, nunca o `.ula`.

## Requisitos

- Python 3.10 ou superior
- Nenhuma biblioteca externa

## Uso

```bash
python montador.py testeula.ula
```

Sem argumento, o programa procura `testeula.ula` na pasta atual. A saída é sempre gravada como `testeula.hex`, na mesma pasta.

## Como levar o .hex ao Arduino

1. Abra o Monitor Serial da IDE do Arduino, com o firmware do grupo já gravado na placa.
2. Ajuste o baud rate e o terminador de linha conforme definido no repositório do Arduino.
3. Abra o `testeula.hex` (ou copie o conteúdo exibido na tela pelo montador).
4. Selecione **todo** o conteúdo, cole no campo "Enviar" e envie de uma vez.

A especificação exige que a carga seja feita em bloco único. Não se digita uma instrução de cada vez.

## Estrutura do repositório

```
.
├── montador.py     # ponto de entrada: orquestra leitura, tradução e gravação
├── tradutor.py     # leitura do fonte, estado de X e Y, tabela de mnemônicos
├── validador.py    # detecção e relato dos erros do fonte
├── saida.py        # gravação do testeula.hex e exibição na tela
├── testeula.ula    # fonte de teste do grupo (cobre as 16 instruções e os 2 erros)
├── testeula.hex    # saída gerada
└── README.md
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

- `X=` e `Y=` recebem valores **decimais** de 0 a 15 e **não geram linha no .hex**. Apenas atualizam o estado interno do montador.
- `W=<mnemônico>;` gera uma linha no `.hex`, usando os valores de X e Y vigentes naquele momento.
- X e Y permanecem válidos até uma nova atribuição. É por isso que dez linhas de fonte produzem quatro linhas de saída.
- X e Y iniciam em 0 caso uma operação apareça antes de qualquer atribuição.
- `inicio:` e `fim.` delimitam o programa.

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

As operações são sempre realizadas sobre X e Y, e o resultado vai para W.

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

| Linha do fonte | X | Y | S | Saída |
|---|---|---|---|---|
| `X=12; Y=6; W=AeB;` | 12 → C | 6 → 6 | `AeB` → B | `C6B` |
| `X=10; Y=3; W=AoB;` | 10 → A | 3 → 3 | `AoB` → E | `A3E` |
| `W=AeBn;` | A (mantido) | 3 (mantido) | `AeBn` → 4 | `A34` |
| `X=13; W=nB;` | 13 → D | 3 (mantido) | `nB` → 5 | `D35` |

Executando `C6B` no Arduino: X = 1100, Y = 0110, S = 1011 (`AeB`, o "e" das entradas). O resultado é 0100, ou seja W = 4, com o LED do pino 12 aceso.

## Tratamento de erros

O montador detecta os dois erros previstos na especificação. Em ambos os casos o erro é **relatado e a tradução prossegue** — nunca há interrupção.

**Linha em branco**

```
[AVISO] linha 7: linha em branco ignorada
```

**Sintaxe ou mnemônico inválido**

```
[ERRO] linha 9: mnemonico desconhecido 'AeZ' — linha ignorada
[ERRO] linha 12: sintaxe invalida 'X=5' — falta ponto e virgula
```

Linhas com erro não geram código e não ocupam posição no vetor memória do Arduino. Ao final, o montador imprime um resumo com a contagem de erros e o número de instruções geradas.

Também são tratados como erro os valores fora da faixa de 4 bits, como `X=20`.

O parser normaliza espaços, tabulações e finais de linha `CRLF` antes de analisar cada linha, e compara os mnemônicos por igualdade completa — `nA` e `nAoB` não se confundem.

O número de linha informado nas mensagens é sempre o do arquivo `.ula` original, e não tem relação com a posição da instrução na memória do Arduino.

## Arquivo de teste

O `testeula.ula` deste repositório cobre:

- as 16 instruções da tabela;
- reaproveitamento de X e Y sem reatribuição;
- `zeroL` e `umL`, que ignoram as entradas;
- uma linha em branco no meio do programa;
- um mnemônico inexistente;
- uma linha com sintaxe quebrada.

O arquivo usado na avaliação é outro e só será conhecido no momento da apresentação.

## Divisão de trabalho (lado PC)

### Lucca — Etapas 1 e 2

**Etapa 1 — Tradutor (`tradutor.py`)**

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
- Padronização das mensagens `[ERRO]` / `[AVISO]`
- Garantia de que nenhum erro interrompe a tradução

### Clarisse — Etapas 3 e 4

**Etapa 3 — Saída (`saida.py` e `montador.py`)**

- Orquestração do fluxo em `montador.py`: leitura, tradução, validação, gravação
- Argumento de linha de comando com o caminho do `.ula`
- Gravação do `testeula.hex` no formato exato combinado com o Arduino
- Exibição do conteúdo gerado na tela, pronto para copiar e colar
- Resumo final com contagem de erros e de instruções geradas

**Etapa 4 — Arquivo de teste (`testeula.ula`)**

- Cobertura das 16 instruções da tabela
- Reaproveitamento de X e Y sem reatribuição
- `zeroL` e `umL`, que ignoram as entradas
- Os dois casos de erro (sintaxe e linha em branco)
- Conferência do `.hex` gerado contra o resultado esperado, calculado à mão
- Conferência do resultado no Arduino, LED a LED, junto com a equipe de hardware

### Regras comuns

- **Contrato entre as etapas:** Lucca entrega a lista de palavras `XYS` e a lista de erros; Clarisse grava e exibe. O formato dessas duas listas é combinado entre os dois antes de começar e não muda depois.
- **Formato de linha do `.hex`:** acertado por Clarisse com o responsável pela memória do Arduino, já que ela é quem grava o arquivo.
- Cada um comenta o próprio código; comentários são critério explícito de nota.
- Cada um revisa o código do outro antes de a etapa ser considerada pronta.
- Ambos treinam o rastreamento completo de `C6B`, do fonte `.ula` até os LEDs acesos. A entrevista é aleatória e nenhuma parte do fluxo pode ser desconhecida por qualquer um dos dois.