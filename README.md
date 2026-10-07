# ULA 4 bits — Software do PC

Montador do Exercício Prático 03 de Arquitetura de Computadores 2 (Ciência da Computação, PUC Minas, 2026/2).

**Grupo:** Ana Flávia, Clarisse de Assis, Jamille Micaele, Júlia Batista, Lucca de Paula.

## Visão geral

O trabalho tem duas partes:

| Parte | O que faz |
|---|---|
| **PC** (este repositório) | Traduz o programa fonte `testeula.ula` para o programa executável `testeula.hex`. |
| **Arduino** (outro repositório) | Recebe o `.hex` pela serial, carrega tudo no vetor memória e executa uma instrução a cada 4 s, acendendo os LEDs dos pinos 13 a 10 e mostrando o DUMP da memória. |

```
testeula.ula  ──[ python3 main.py ]──▶  testeula.hex  ──[ Monitor Serial ]──▶  Arduino
 (mnemônicos)                            (hexadecimal)                         (LEDs)
```

O programa do PC **não se comunica com o Arduino**: o `.hex` é copiado e colado no Monitor Serial.

## Como usar

Requisito: Python 3, sem bibliotecas externas.

```bash
python3 main.py
```

1. O programa lê `testeula.ula` da pasta atual. Os nomes dos arquivos são fixos, conforme a especificação, e estão em [variaveis.py](variaveis.py).
2. Mostra os erros e avisos, um resumo e o conteúdo gerado.
3. Grava `testeula.hex` na mesma pasta.

Para enviar ao Arduino, abra o `testeula.hex`, copie **todo** o conteúdo, cole no campo "Enviar" do Monitor Serial e envie **de uma vez**. Nunca envie uma instrução por vez.

## Do `.ula` ao `.hex`, passo a passo

### 1. O programa fonte

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

- `inicio:` e `fim.` delimitam o programa.
- `X=` e `Y=` recebem um **decimal de 0 a 15**. Eles só guardam o valor e **não geram linha no `.hex`**.
- `W=<mnemônico>;` gera **uma linha** no `.hex`, usando os valores de X e Y daquele momento.
- X e Y valem 0 até a primeira atribuição e mantêm o valor até serem reatribuídos.
- Toda linha de comando termina em `;`. Espaços, tabulações e finais de linha do Windows são ignorados.

### 2. Cada `W=` vira uma palavra de 3 dígitos: `X Y S`

| Linhas do fonte | X | Y | S (instrução) | Saída |
|---|---|---|---|---|
| `X=12; Y=6; W=AeB;` | 12 → **C** | 6 → **6** | `AeB` → **B** | `C6B` |
| `X=10; Y=3; W=AoB;` | 10 → **A** | 3 → **3** | `AoB` → **E** | `A3E` |
| `W=AeBn;` | A (mantido) | 3 (mantido) | `AeBn` → **4** | `A34` |
| `X=13; W=nB;` | 13 → **D** | 3 (mantido) | `nB` → **5** | `D35` |

Por isso as 10 linhas do fonte geram só 4 linhas no `testeula.hex`:

```
C6B
A3E
A34
D35
```

### 3. O que o Arduino faz com `C6B`

X = `1100`, Y = `0110`, S = `B` = `AeB` (X **e** Y, bit a bit) → W = `0100` = 4 → **LED do pino 12 aceso**.

Com `A3E` em seguida: `1010` **ou** `0011` = `1011` = B → **LEDs dos pinos 13, 11 e 10 acesos**.

## Conjunto de instruções

| Código | Mnemônico | Função | | Código | Mnemônico | Função |
|---|---|---|---|---|---|---|
| 0 | `nA` | A' | | 8 | `nAoB` | A' + B |
| 1 | `AoBn` | (A+B)' | | 9 | `AxBn` | A·B + A'·B' |
| 2 | `nAeB` | A'·B | | A | `copiaB` | B |
| 3 | `zeroL` | 0 | | B | `AeB` | A·B |
| 4 | `AeBn` | (A·B)' | | C | `umL` | 1 |
| 5 | `nB` | B' | | D | `AonB` | A + B' |
| 6 | `AxB` | A'·B + A·B' | | E | `AoB` | A + B |
| 7 | `AenB` | A·B' | | F | `copiaA` | A |

A = X e B = Y. O resultado vai sempre para W. A tabela está em [mnemonicos.py](mnemonicos.py).

## Erros

Como pede a especificação, **nenhum erro interrompe a montagem**: a linha com problema é informada e ignorada, as demais são traduzidas e o `.hex` é gravado normalmente.

| Situação | Exemplo | Mensagem |
|---|---|---|
| Linha em branco | | `[AVISO] - (linha N) - Linha em branco sera ignorada.` |
| Falta `;` | `X=13` | `[ERRO] - (linha N) - Conteudo 'X=13' invalido. Erro de sintaxe.` |
| Falta `=` | `X3;` | `[ERRO] - (linha N) - Necessario operador '=' apos X.` |
| Valor não numérico | `X=1a;` | `[ERRO] - (linha N) - Valor de X '1a' invalido.` |
| Valor fora de 0 a 15 | `X=20;` | `[ERRO] - (linha N) - Valor de X '20' fora da faixa permitida de 0 a 15.` |
| Variável desconhecida | `Z=3;` | `[ERRO] - (linha N) - Variavel ou instrucao invalida: 'Z=3;'.` |
| Mnemônico inexistente | `W=AeZ;` | `[ERRO] - (linha N) - Mnemonico AeZ invalido.` (seguida da lista de mnemônicos válidos) |
| Falta `inicio:` | | `[ERRO] - (linha 1) - Texto de inicio '...' invalido.` (a linha 1 é traduzida como comando) |
| Texto depois de `fim.` | | `[ERRO] - (linha N) - Conteudo '...' depois de 'fim.' sera ignorado.` |
| Falta `fim.` | | `[ERRO] - O programa nao possui um 'fim.' valido.` |

`N` é a linha no arquivo `.ula`, contando a partir de 1. O `.hex` só deixa de ser gerado quando o `.ula` não existe ou está vazio.

## Arquivo de teste

O [testeula.ula](testeula.ula) do grupo cobre:

- as 16 instruções (com X = 0 e Y = 0, gerando `000` a `00F`);
- o exemplo da especificação, incluindo o reaproveitamento de X e Y;
- os dois erros previstos: uma linha em branco e um mnemônico inválido.

Na apresentação, o professor usa outro `testeula.ula`.

### Bateria de testes

A pasta [testes-ula/](testes-ula/) tem 12 programas `.ula`. Cada um vem com um `.txt` de mesmo nome que descreve o objetivo do teste, as mensagens esperadas, o resumo e o `testeula.hex` esperado.

| Teste | Cobre |
|---|---|
| `01_exemplo_pdf` | Exemplo da especificação (Figura 3) |
| `02_todas_instrucoes` | As 16 instruções, com tabela de LEDs para conferir no Arduino |
| `03_reaproveitamento_xy` | X e Y iniciais, extremos 0 e 15, reaproveitamento |
| `04_linhas_em_branco` | Linhas em branco isoladas, seguidas, só com espaços/TAB e depois de `fim.` |
| `05_erros_sintaxe` | Todas as variações de sintaxe errada |
| `06_espacos_tabs_crlf` | Espaços, TABs e finais de linha do Windows |
| `07_sem_inicio` / `08_inicio_invalido` | `inicio:` ausente ou escrito errado |
| `09_sem_fim` / `10_conteudo_apos_fim` | `fim.` ausente ou seguido de conteúdo |
| `11_sem_instrucoes` | Programa sem nenhum `W=` (gera `.hex` vazio) |
| `12_arquivo_vazio` | Arquivo vazio (não gera `.hex`) |

Como o programa só lê `testeula.ula`, copie o teste para a raiz antes de rodar. Para não perder o arquivo do grupo, rode a partir de uma cópia ou restaure depois com `git checkout testeula.ula testeula.hex`.

```bash
cp testes-ula/05_erros_sintaxe.ula testeula.ula
python3 main.py
```

## Organização do código

| Arquivo | Responsabilidade |
|---|---|
| [main.py](main.py) | Ponto de entrada: lê, monta e grava. |
| [gestao_arquivo.py](gestao_arquivo.py) | Lê o `.ula` e grava o `.hex`. |
| [tratador.py](tratador.py) | Limpa cada linha (espaços, tabulações, `\r`, `\n`) e converte números para hexadecimal. |
| [validador.py](validador.py) | Verificações simples: `inicio:`, `fim.`, `;`, faixa de 0 a 15, mnemônico. |
| [montador.py](montador.py) | Percorre o fonte, guarda X e Y, monta as palavras `XYS`, reporta erros e mostra o resumo. |
| [mnemonicos.py](mnemonicos.py) | Tabela dos 16 mnemônicos. |
| [variaveis.py](variaveis.py) | Nomes dos arquivos e listas compartilhadas. |

## Divisão do trabalho (lado PC)

- **Lucca:** leitura, tradução e validação (estrutura inicial dos módulos).
- **Clarisse:** tratamento de erros sem interrupção, resumo na tela e arquivo de teste.

Todo o grupo deve saber explicar o caminho completo de `C6B`, do `.ula` até o LED aceso: a avaliação é individual, durante a apresentação.
