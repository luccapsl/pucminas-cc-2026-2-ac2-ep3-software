#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

import os
import tratador
import validador
import montador
from variaveis import nomeArquivo_hex, nomeArquivo_ula, conteudo

def ler_arquivo_ula(nomeArquivo_ula):
    """ Faz a leitura do arquivo .ula, enumera cada linha e salva em uma variavel vetorizada

    Args:
        nomeArquivo_ula: nome do arquivo .ula

    Returns:
        conteudo do arquivo
        formato: [(num_linha, 'texto_linha'), ..., (num_linha, 'texto_linha')]
    """

    if (os.path.exists(nomeArquivo_ula)):
        with open(nomeArquivo_ula, "r", encoding="utf-8") as arquivo:
            for num_linha, texto_linha in enumerate(arquivo, start=1):
                conteudo.append((num_linha, tratador.limpeza_texto_linha(texto_linha)))

        print("[INFO] - Leitura do arquivo %s realizada com sucesso." % nomeArquivo_ula)
    else:
        print("[ERRO] - Arquivo com nome %s nao foi encontrado. Leitura impossivel de ser realizada." % nomeArquivo_ula)

    return conteudo


def escrever_arquivo_hex(nomeArquivo_hex, conteudoHexadecimal):
    """ Faz a escrita do arquivo .hex, com o conteudo hexadecimal

    Args:
        nomeArquivo_hex: nome do arquivo .hex
        conteudoHexadecimal: conteudo hexadecimal a ser escrito no arquivo

    Returns:
        None
    """

    with open(nomeArquivo_hex, "w", encoding="utf-8") as arquivo:
        for linha in conteudoHexadecimal:
            arquivo.write(linha + "\n")

    print("[INFO] - Escrita do arquivo %s realizada com sucesso." % nomeArquivo_hex)