#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

import os
from variaveis import nomeArquivo

def ler_arquivo_ula(nomeArquivo):
    """ Faz a leitura do arquivo .ula

    Args:
        nomeArquivo: nome do arquivo .ula

    Returns:
        conteudo do arquivo (se nao existir, retorna None)

    """

    conteudo = None

    if (os.path.exists(nomeArquivo)):
        with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
            
    else:
        print("[ERRO] - Arquivo com nome %s nao foi encontrado. Leitura impossivel de ser realizada." % nomeArquivo)

    return conteudo