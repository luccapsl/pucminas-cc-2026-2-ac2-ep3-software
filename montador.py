# ---------------------------------- #
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele,
# Julia Batista, Lucca de Paula
# ---------------------------------- #

# Arquivo responsavel pela montagem do arquivo .ula para .hex.

import mnemonicos
import tratador
import validador

from variaveis import conteudoHexadecimal


def limpar_indice_auxiliar():
    """Limpa as instrucoes geradas em uma montagem anterior."""
    conteudoHexadecimal.clear()


def inserir_indice_auxiliar(indice, valor):
    """Acrescenta um caractere hexadecimal na instrucao indicada."""
    while len(conteudoHexadecimal) <= indice:
        conteudoHexadecimal.append("")

    conteudoHexadecimal[indice] += str(valor)


def montagem_texto_hexa(conteudo):
    """
    Traduz o programa .ula para palavras XYS em hexadecimal.

    Erros de linhas individuais sao informados e nao interrompem
    a traducao das linhas seguintes. A ausencia de inicio: ou de
    fim. tambem e informada, mas nao impede a gravacao do
    arquivo .hex.
    """

    limpar_indice_auxiliar()

    if not conteudo:
        print("[ERRO] - O conteudo do arquivo esta vazio.")
        return False

    x = 0
    y = 0
    indiceConteudo = 0
    quantidadeErros = 0
    quantidadeAvisos = 0
    quantidadeInstrucoes = 0
    encontrouFim = False

    linha = 1

    # Sem inicio:, o erro e informado e a primeira linha
    # passa a ser traduzida como um comando comum.
    if not validador.validar_inicio(conteudo[0]):
        print(
            f"[ERRO] - (linha 1) - Texto de inicio "
            f"'{conteudo[0]}' invalido."
        )
        quantidadeErros += 1
        linha = 0

    while linha < len(conteudo):
        texto = conteudo[linha]
        numeroLinha = linha + 1

        # Linha em branco: avisa e continua.
        if texto == "":
            print(
                f"[AVISO] - (linha {numeroLinha}) - "
                f"Linha em branco sera ignorada."
            )
            quantidadeAvisos += 1
            linha += 1
            continue

        # Qualquer conteudo depois de fim. e informado e ignorado.
        if encontrouFim:
            print(
                f"[ERRO] - (linha {numeroLinha}) - "
                f"Conteudo '{texto}' depois de 'fim.' sera ignorado."
            )
            quantidadeErros += 1
            linha += 1
            continue

        # fim. encerra o programa.
        if validador.validar_fim(texto):
            encontrouFim = True
            linha += 1
            continue

        # Depois de inicio:, todas as linhas de comando precisam
        # terminar em ponto e virgula.
        if not validador.validar_pontovirgula(texto):
            print(
                f"[ERRO] - (linha {numeroLinha}) - "
                f"Conteudo '{texto}' invalido. Erro de sintaxe."
            )
            quantidadeErros += 1
            linha += 1
            continue

        # --------------------------------------------------
        # ATRIBUICAO DE X
        # --------------------------------------------------
        if texto.startswith("X"):
            if len(texto) < 4 or not texto.startswith("X="):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Necessario operador '=' apos X."
                )
                quantidadeErros += 1
                linha += 1
                continue

            valorTexto = texto[2:-1]

            if valorTexto == "":
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de X ausente."
                )
                quantidadeErros += 1
                linha += 1
                continue

            if not valorTexto.isdigit():
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de X '{valorTexto}' invalido."
                )
                quantidadeErros += 1
                linha += 1
                continue

            valorX = int(valorTexto)

            if not validador.validar_hexa(valorX):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de X '{valorX}' fora da faixa permitida "
                    f"de 0 a 15."
                )
                quantidadeErros += 1
                linha += 1
                continue

            x = valorX
            linha += 1
            continue

        # --------------------------------------------------
        # ATRIBUICAO DE Y
        # --------------------------------------------------
        if texto.startswith("Y"):
            if len(texto) < 4 or not texto.startswith("Y="):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Necessario operador '=' apos Y."
                )
                quantidadeErros += 1
                linha += 1
                continue

            valorTexto = texto[2:-1]

            if valorTexto == "":
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de Y ausente."
                )
                quantidadeErros += 1
                linha += 1
                continue

            if not valorTexto.isdigit():
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de Y '{valorTexto}' invalido."
                )
                quantidadeErros += 1
                linha += 1
                continue

            valorY = int(valorTexto)

            if not validador.validar_hexa(valorY):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de Y '{valorY}' fora da faixa permitida "
                    f"de 0 a 15."
                )
                quantidadeErros += 1
                linha += 1
                continue

            y = valorY
            linha += 1
            continue

        # --------------------------------------------------
        # ATRIBUICAO DE W
        # --------------------------------------------------
        if texto.startswith("W"):
            if len(texto) < 4 or not texto.startswith("W="):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Necessario operador '=' apos W."
                )
                quantidadeErros += 1
                linha += 1
                continue

            mnemonicoTexto = texto[2:-1]

            if mnemonicoTexto == "":
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Mnemonico ausente."
                )
                quantidadeErros += 1
                linha += 1
                continue

            mnemonico = validador.validar_mnemonico(mnemonicoTexto)

            if mnemonico == -1:
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Mnemonico {mnemonicoTexto} invalido."
                )
                print(
                    f"A lista de mnemonicos validos e: "
                    f"{mnemonicos.print_lista_mnemonicos}"
                )
                quantidadeErros += 1
                linha += 1
                continue

            # Cada instrucao e formada por X, Y e S.
            xHexadecimal = tratador.converter_hexadecimal(x)
            yHexadecimal = tratador.converter_hexadecimal(y)
            mnemonicoHexadecimal = tratador.converter_hexadecimal(mnemonico)

            conteudoHexadecimal.append(
                xHexadecimal + yHexadecimal + mnemonicoHexadecimal
            )

            quantidadeInstrucoes += 1
            linha += 1
            continue

        # Qualquer outra variavel e invalida.
        print(
            f"[ERRO] - (linha {numeroLinha}) - "
            f"Variavel ou instrucao invalida: '{texto}'."
        )
        quantidadeErros += 1
        linha += 1

    # Sem fim., o erro e informado, mas o .hex e gravado.
    if not encontrouFim:
        print(
            "[ERRO] - O programa nao possui um 'fim.' valido."
        )
        quantidadeErros += 1

    print()
    print("----------------------------------")
    print("RESUMO DA MONTAGEM")
    print("----------------------------------")
    print(f"Quantidade de instrucoes geradas: {quantidadeInstrucoes}")
    print(f"Quantidade de erros: {quantidadeErros}")
    print(f"Quantidade de avisos: {quantidadeAvisos}")

    print()
    print("----------------------------------")
    print("CONTEUDO HEXADECIMAL GERADO")
    print("----------------------------------")

    if conteudoHexadecimal:
        for instrucao in conteudoHexadecimal:
            print(instrucao)
    else:
        print("(nenhuma instrucao valida foi gerada)")

    print("----------------------------------")
    print()

    print(
        "[INFO] - Montagem do conteudo hexadecimal "
        "finalizada."
    )

    return True
