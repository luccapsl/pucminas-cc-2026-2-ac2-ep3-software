#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

import os

def limpeza_texto_linha(texto):
    """ Recebe um texto e faz a limpeza dos '\n', '\r', e espacos vazios

    Args:
        texto: string contendo o texto

    Returns:
        texto limpo
    """

    texto = texto.replace('\n','')
    texto = texto.replace('\r','')
    texto = texto.replace(' ','')

    return texto

def tratar_numero(texto, caractere):
    """ Recebe um texto e um caractere e trata o numero que vem depois do caractere

    Args:
        texto: string contendo o texto
        caractere: inteiro contendo o indice do caractere

    Returns:
        numero tratado
    """

    numero = ''
    while (caractere < len(texto) and texto[caractere].isdigit()):
        numero += texto[caractere]
        caractere += 1

    return int(numero)