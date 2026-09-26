#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#


import os
import tratador
import validador


def montagem_texto_hexa(conteudo):
    linha = 0
    validadorSintaxe = True
    conteudoHexadecimal = []
    
    if (validador.validar_inicio(conteudo[linha])):

        linha += 1
        caractere = 0
        x = 0
        y = 0
        numero = -1
        tamConteudo = len(conteudo)-1;
        mnemonico = -1
        
        indiceConteudo = 0
        
        while ( linha <= tamConteudo and validadorSintaxe == True):

            texto = conteudo[linha]
            if (validador.validar_pontovirgula(texto[len(texto)-1], linha)):

                if (validador.validar_x(texto[caractere])):
                    caractere+=1

                    if (validador.validar_igual(texto[caractere])):
                        caractere+=1
                        numero = tratador.tratar_numero(texto, caractere)
                        
                        if (validador.validar_hexa(numero)):
                            x = hex(numero)
                            conteudoHexadecimal[indiceConteudo] = conteudoHexadecimal[indiceConteudo] + x
                        else:
                            validadorSintaxe = False
                    else:
                        validadorSintaxe = False
                elif (validador.validar_y(texto[caractere])):
                    caractere+=1

                    if (validador.validar_igual(texto[caractere])):
                        caractere+=1
                        numero = tratador.tratar_numero(texto, caractere)
                        
                        if (validador.validar_hexa(numero)):
                            y = hex(numero)
                            conteudoHexadecimal[indiceConteudo] = conteudoHexadecimal[indiceConteudo] + y
                        else:
                            validadorSintaxe = False
                    else:
                        validadorSintaxe = False
                elif (validador.validar_operador(texto[caractere])):

                    caractere+=1
                    
                    if (validador.validar_igual(texto[caractere])):
                        caractere+=1
                        mnemonico = validador.validar_mnemonico(mnemonico)
                        
                        if (mnemonico != -1):
                            conteudoHexadecimal[indiceConteudo] = conteudoHexadecimal[indiceConteudo] + mnemonico
                        else:
                            validadorSintaxe = False
                    else:
                        validadorSintaxe = False
                elif (validador.validar_fim((linha, texto))):
                    validadorSintaxe = True
                else:
                    validadorSintaxe = False
                    print(f"[ERRO] (linha {linha}) - Caractere {texto[caractere]} Invalido.")
            else:
                validadorSintaxe = False

            caractere = 0
            linha+1
            indiceConteudo+1
 
    if (validadorSintaxe == False):
        conteudoHexadecimal = []

    return conteudoHexadecimal