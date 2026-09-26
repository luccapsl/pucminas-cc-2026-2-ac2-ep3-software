#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#


import os
import tratador
import validador
from variaveis import nomeArquivo, conteudo


def montagem_texto_hexa(conteudo)

    validadorSintaxe = False
    conteudoHexadecimal = []
    
    if (validar_conteudo_vazio(conteudo)):
        if (validar_inicio(conteudo[0])):

            controlador = True
            linha = 1
            caractere = 0
            x = 0
            y = 0
            tamConteudo = len(conteudo)-1;
            mnemonico = -1

            indiceConteudo = 0

            while ( linha < tamConteudo & controlador & validadorLinha & (not (validar_fim(conteudo[linha]) ) ) ):

                texto = conteudo[linha]

                if (validar_x(texto[caractere])):
                    caractere=+1
                    if (validar_igual(texto[caractere])):
                        caractere=+1
                        if (validar_hexa(numero)):
                            x = hex(numero)
                            conteudoHexadecimal[indiceConteudo] = conteudoHexadecimal[indiceConteudo] + x

                    #123
                elif (validar_y(texto[caractere])):
                    caractere=+1
                    if (validar_igual(texto[caractere])):
                        caractere=+1
                        if (validar_hexa(numero)):
                            y = hex(numero)
                            conteudoHexadecimal[indiceConteudo] = conteudoHexadecimal[indiceConteudo] + y

                    #123
                elif (validar_operador(texto[caractere])):

                    caractere=+1
                    if (validar_igual(texto[caractere])):
                        caractere=+1
                        mnemonico = validar_mnemonico(mnemonico)
                        if (mnemonico != -1):
                            conteudoHexadecimal[indiceConteudo] = conteudoHexadecimal[indiceConteudo] + mnemonico
                else:
                    controlador = False
                    print("[ERRO] (linha %d) - Caractere %c Invalido.", linha, texto[caractere])

                caractere = 0
                linha+1
                indiceConteudo+1
                


                
    if (validadorSintaxe == False):
        conteudoHexadecimal = []

    return conteudoHexadecimal