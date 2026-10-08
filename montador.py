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
    
    quantidadeErros = 0
    quantidadeAvisos = 0
    quantidadeInstrucoes = 0

    #variavel para verificar se o programa possui o indicativo de 'fim.' 
    encontrouFim = False

    # A primeira linha do arquivo .ula e sempre a linha 1 devido a presenca de 'inicio:'
    linha = 1

    # avalia se a primeira linha do arquivo .ula e valida, caso nao seja, o erro e informado e a montagem continua.
    if not validador.validar_inicio(conteudo[0]):
        print(
            f"[ERRO] - (linha 1) - Texto de inicio "
            f"'{conteudo[0]}' invalido."
        )
        quantidadeErros += 1
        linha = 0

    # avalia cada linha do arquivo .ula (armazenado na variavel conteudo)
    # informando erros e avisos, mas nao interrompendo a montagem.
    while linha < len(conteudo):
        texto = conteudo[linha]
        numeroLinha = linha + 1

        # se a linha estiver em branco, um aviso e informado e a linha e ignorada.
        if texto == "":
            print(
                f"[AVISO] - (linha {numeroLinha}) - "
                f"Linha em branco sera ignorada."
            )
            quantidadeAvisos += 1
            linha += 1
            continue

        # se o programa ja encontrou o indicativo de 'fim.', qualquer linha seguinte e ignorada e um erro e informado
        if encontrouFim:
            print(
                f"[ERRO] - (linha {numeroLinha}) - "
                f"Conteudo '{texto}' depois de 'fim.' sera ignorado."
            )
            quantidadeErros += 1
            linha += 1
            continue

        # se a linha for o indicativo de 'fim.', a variavel encontrouFim e atualizada para True e a linha seguinte sera ignorada
        if validador.validar_fim(texto):
            encontrouFim = True
            linha += 1
            continue

        # se a linha nao terminar com ';', um erro e informado e a linha e ignorada
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

            # se a linha nao tiver o operador '=' apos o 'X', um erro e informado e a linha e ignorada
            if len(texto) < 4 or not texto.startswith("X="):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Necessario operador '=' apos X."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # pega o valor de X, removendo o "X=" do inicio e o ";" do final
            valorTexto = texto[2:-1]

            # se o valor de X estiver ausente, um erro e informado e a linha e ignorada
            if valorTexto == "":
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de X ausente."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # se o valor de X nao for um numero inteiro, um erro e informado e a linha e ignorada
            if not valorTexto.isdigit():
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de X '{valorTexto}' invalido."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # variavel auxiliar para armazenar o valor de X convertido para inteiro
            valorX = int(valorTexto)

            # se o valor de X nao estiver na faixa de 0 a 15, um erro e informado e a linha e ignorada
            if not validador.validar_hexa(valorX):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de X '{valorX}' fora da faixa permitida "
                    f"de 0 a 15."
                )
                quantidadeErros += 1
                linha += 1
                continue

            # dando tudo certo. O valor de X e atualizado e a linha seguinte e avaliada
            x = valorX
            linha += 1
            continue

        # --------------------------------------------------
        # ATRIBUICAO DE Y
        # --------------------------------------------------
        if texto.startswith("Y"):

            # valida se a linha possui o operador '=' apos o 'Y', caso nao possua, um erro e informado e a linha e ignorada
            if len(texto) < 4 or not texto.startswith("Y="):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Necessario operador '=' apos Y."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # pega o valor de Y, removendo o "Y=" do inicio e o ";" do final
            valorTexto = texto[2:-1]

            # valida se o valor de Y esta ausente, caso esteja, um erro e informado e a linha e ignorada
            if valorTexto == "":
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de Y ausente."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue


            # valida se o valor de Y e um numero inteiro, caso nao seja, um erro e informado e a linha e ignorada
            if not valorTexto.isdigit():
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de Y '{valorTexto}' invalido."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # variavel auxiliar para armazenar o valor de Y convertido para inteiro
            valorY = int(valorTexto)

            # valida se o valor de Y esta na faixa de 0 a 15, caso nao esteja, um erro e informado e a linha e ignorada
            if not validador.validar_hexa(valorY):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Valor de Y '{valorY}' fora da faixa permitida "
                    f"de 0 a 15."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # dando tudo certo. O valor de Y e atualizado e a linha seguinte e avaliada
            y = valorY
            linha += 1
            continue

        # --------------------------------------------------
        # ATRIBUICAO DE W
        # --------------------------------------------------
        if texto.startswith("W"):

            # valida se a linha possui o operador '=' apos o 'W', caso nao possua, um erro e informado e a linha e ignorada
            if len(texto) < 4 or not texto.startswith("W="):
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Necessario operador '=' apos W."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # pega o valor de W, removendo o "W=" do inicio e o ";" do final
            mnemonicoTexto = texto[2:-1]

            # valida se o mnemonico esta ausente, caso esteja, um erro e informado e a linha e ignorada
            if mnemonicoTexto == "":
                print(
                    f"[ERRO] - (linha {numeroLinha}) - "
                    f"Mnemonico ausente."
                )
                quantidadeErros += 1
                linha += 1

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # valida se o mnemonico e valido, caso nao seja, um erro e informado e a linha e ignorada
            mnemonico = validador.validar_mnemonico(mnemonicoTexto)

            # se o mnemonico = -1, significa que o mnemonico e invalido, entao um erro e informado e a linha e ignorada
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

                # pula para a proxima iteracao do loop, ignorando a linha atual
                continue

            # converte os valores de X, Y e mnemonico para hexadecimal e adiciona a variavel auxiliar conteudoHexadecimal
            xHexadecimal = tratador.converter_hexadecimal(x)
            yHexadecimal = tratador.converter_hexadecimal(y)
            mnemonicoHexadecimal = tratador.converter_hexadecimal(mnemonico)

            # adiciona a instrucao completa em hexadecimal na lista de conteudoHexadecimal
            conteudoHexadecimal.append(
                xHexadecimal + yHexadecimal + mnemonicoHexadecimal
            )

            quantidadeInstrucoes += 1
            linha += 1

            # pula para a proxima iteracao do loop, ignorando a linha atual
            continue

        # caso a linha nao seja uma atribuicao de X, Y ou W, um erro e informado e a linha e ignorada
        print(
            f"[ERRO] - (linha {numeroLinha}) - "
            f"Variavel ou instrucao invalida: '{texto}'."
        )
        quantidadeErros += 1
        linha += 1

    # se o programa nao possuir o indicativo de 'fim.', um erro e informado
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
