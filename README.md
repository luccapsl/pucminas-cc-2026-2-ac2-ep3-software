# pucminas-cc-2026-2-ac2-ep3-software
Desenvolvimento do software em Python que traduzirá um .ula para um arquivo .hex utilizando todos os 16 mnemônicos de uma ULA de 4 bits.

Montador e interface serial do Exercício Prático 03 da disciplina de Arquitetura de Computadores 2 do curso de Ciência da Computação da PUC Minas (2026/2).

Este repositório contém **apenas o lado PC**. O firmware do Arduino é mantido pelos outros três integrantes do grupo.

# Integrantes 

- Arduino
  - Ana Flávia Menezes de Almeida 
  - Jamille Micaele Soares Ferreira 
  - Julia Batista Moreira
  
- Python
  - Clarisse de Assis Pereira
  - Lucca de Paula Silva Lopes

## O que este programa faz

1. Lê o arquivo fonte `testeula.ula`, escrito com os mnemônicos da ULA.
2. Traduz cada operação em uma palavra hexadecimal de 3 dígitos (`XYS`) e grava o resultado em `testeula.hex`.
3. Detecta erros no fonte (sintaxe inválida e linhas em branco), reporta e **continua** a tradução.
4. Envia o `.hex` gerado ao Arduino pela porta serial, em bloco único.

O Arduino executa o `.hex`, nunca o `.ula`.

## Requisitos

- Python 3.10 ou superior
- `pyserial` (somente para o envio serial)

```bash
pip install pyserial
```

## Uso

Traduzir o fonte e gerar o executável:

```bash
python montador.py testeula.ula
```

Traduzir e enviar direto ao Arduino:

```bash
python montador.py testeula.ula --porta COM3
python montador.py testeula.ula --porta /dev/ttyUSB0
```

Se a porta serial não estiver disponível, o conteúdo do `.hex` é impresso na tela para ser copiado e colado no campo "Enviar" do Monitor Serial da IDE do Arduino. Os dois caminhos são equivalentes do ponto de vista do Arduino.

## Estrutura do repositório

```
.
├── montador.py        # ponto de entrada: lê o .ula, gera o .hex, envia
├── tradutor.py        # tabela de mnemônicos e conversão linha a linha
├── validador.py       # detecção e relato dos erros do fonte
├── serial_envio.py    # comunicação com o Arduino
├── testeula.ula       # fonte de teste do grupo (cobre as 16 instruções e os 2 erros)
├── testeula.hex       # saída gerada
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

## Comunicação serial

| Parâmetro | Valor |
|---|---|
| Baud rate | 9600 |
| Terminador de linha | `\n` (NL) |
| Pausa após abrir a porta | 2 segundos |

A pausa é obrigatória: abrir a porta serial reinicia o Arduino, e enviar antes disso faz o bloco se perder. O `.hex` é transmitido inteiro, de uma vez — o Arduino carrega tudo na memória antes de executar qualquer instrução.

Enquanto o programa do PC estiver usando a porta, o Monitor Serial da IDE do Arduino precisa estar fechado.

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

Cada etapa do software é dividida ao meio entre os dois integrantes, de modo que nenhum dos dois seja o único a conhecer qualquer parte do fluxo. O corte segue a fronteira natural de cada módulo: um lado cuida da **entrada**, o outro da **saída**.

### Etapa 1 — Tradutor (`tradutor.py`)

| Lucca — entrada | Clarisse — saída |
|---|---|
| Abertura e leitura do `.ula` | Tabela dos 16 mnemônicos |
| Normalização de espaços, tabs e `CRLF` | Conversão decimal → hexadecimal de X e Y |
| Reconhecimento de `inicio:` e `fim.` | Montagem da palavra `XYS` |
| Parsing de `X=` e `Y=` e estado interno | Gravação do `testeula.hex` |

### Etapa 2 — Validação (`validador.py`)

| Lucca | Clarisse |
|---|---|
| Linha em branco | Mnemônico inexistente |
| Falta de ponto e vírgula | Valor fora da faixa de 4 bits |
| Variável desconhecida à esquerda do `=` | Padronização das mensagens `[ERRO]` / `[AVISO]` |
| Garantia de que o erro não interrompe a tradução | Resumo final com contagem de erros e instruções |

### Etapa 3 — Serial (`serial_envio.py`)

| Lucca | Clarisse |
|---|---|
| Abertura da porta e pausa de 2 s | Argumentos de linha de comando (`--porta`) |
| Transmissão do `.hex` em bloco único | Modo alternativo: impressão em tela para copiar e colar |
| Baud rate e terminador de linha | Tratamento de porta inexistente ou ocupada |

### Etapa 4 — Arquivo de teste (`testeula.ula`)

| Lucca | Clarisse |
|---|---|
| Cobertura das 16 instruções da tabela | Os dois casos de erro (sintaxe e linha em branco) |
| Reaproveitamento de X e Y sem reatribuição | `zeroL` e `umL`, que ignoram as entradas |
| Conferência do `.hex` gerado contra o esperado | Conferência do resultado no Arduino, LED a LED |

### Regras comuns

- Cada um comenta o próprio código; comentários são critério explícito de nota.
- Toda etapa é revisada pelo outro antes de ser considerada pronta.
- O formato exato de linha do `.hex` é acertado **pelos dois juntos** com o responsável pela memória do Arduino, já que a etapa 1 é compartilhada.
- Ambos treinam o rastreamento completo de `C6B`, do fonte `.ula` até os LEDs acesos. A entrevista é aleatória e nenhuma parte do fluxo pode ser desconhecida por qualquer um dos dois.
