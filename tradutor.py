#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

import os
from variaveis import nomeArquivo, conteudo

def ler_arquivo_ula(nomeArquivo):
    """ Faz a leitura do arquivo .ula, enumera cada linha e salva em uma variavel vetorizada

    Args:
        nomeArquivo: nome do arquivo .ula

    Returns:
        conteudo do arquivo
        formato: [(num_linha, 'texto_linha'), ..., (num_linha, 'texto_linha')]
    """

    if (os.path.exists(nomeArquivo)):
        with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
            for num_linha, texto_linha in enumerate(arquivo, start=1):
                conteudo.append((num_linha, texto_linha))
    else:
        print("[ERRO] - Arquivo com nome %s nao foi encontrado. Leitura impossivel de ser realizada." % nomeArquivo)

    return conteudo

ler_arquivo_ula(nomeArquivo)
