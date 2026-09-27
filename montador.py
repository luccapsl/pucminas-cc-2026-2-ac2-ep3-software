#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

# Arquivo para realizar a montagem do arquivo .ula para .hex

import os
import mnemonicos
import tratador
import validador
from variaveis import conteudoHexadecimal

def limpar_indice_auxiliar():
    """Funcao que limpa o conteudo da lista de conteudo hexadecimal.
    
    Args global:
        conteudoHexadecimal: lista contendo o conteudo do arquivo .hex
    
    """
    while ( len(conteudoHexadecimal) > 0 ):
        conteudoHexadecimal.pop()

def inserir_indice_auxiliar(indice, valor):
    """Funcao que insere um valor na lista de conteudo hexadecimal.
    
    Args global:
        conteudoHexadecimal: lista contendo o conteudo do arquivo .hex
    
    """
    while ( len(conteudoHexadecimal) <= indice ):
        conteudoHexadecimal.append("") 
    
    conteudoHexadecimal[indice] = str(conteudoHexadecimal[indice]) + str(valor)

def montagem_texto_hexa(conteudo):
    """Funcao que realiza a montagem do conteudo textual para hexadecimal.
    
    Args:
        conteudo: lista contendo o conteudo do arquivo .ula

    Args global:
        conteudoHexadecimal: lista contendo o conteudo do arquivo .hex

    Returns:
        validadorSintaxe: booleano indicando se a sintaxe do conteudo foi validada com sucesso
    
    """
    linha = 0
    validadorSintaxe = True
    
    if (validador.validar_inicio(conteudo[linha])):

        linha += 1
        caractere = 0
        x = 0
        y = 0
        numero = -1
        indiceConteudo = 0
        tamConteudo = len(conteudo)-1;
        mnemonico = -1
        
        while ( linha <= tamConteudo and validadorSintaxe == True):

            texto = conteudo[linha]

            if (validador.validar_pontovirgula(texto, linha)):

                if (validador.validar_x(texto[caractere])):
                    caractere+=1

                    if (validador.validar_igual(texto[caractere])):
                        caractere+=1
                        numero = tratador.tratar_numero(texto, caractere)
                        
                        if (validador.validar_hexa(numero)):
                            x = numero
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
                            y = numero
                        else:
                            validadorSintaxe = False
                    else:
                        validadorSintaxe = False
                elif (validador.validar_operador(texto[caractere])):

                    caractere+=1
                    
                    if (validador.validar_igual(texto[caractere])):
                        caractere+=1
                        mnemonico = validador.validar_mnemonico(tratador.tratar_mnemonico(texto, caractere))
                        
                        if (mnemonico != -1):
                            inserir_indice_auxiliar(indiceConteudo, tratador.converter_hexadecimal(y)) 
                            inserir_indice_auxiliar(indiceConteudo, tratador.converter_hexadecimal(x))
                            inserir_indice_auxiliar(indiceConteudo, tratador.converter_hexadecimal(mnemonico))
                            indiceConteudo+=1
                        else:
                            validadorSintaxe = False
                            print(f"[ERRO] (linha {linha+1}) - Mnemonico {texto[caractere:]} Invalido.")
                            print(f"A lista de mnemonicos validos é: {mnemonicos.print_lista_mnemonicos}\n")
                    else:
                        validadorSintaxe = False
                else:
                    validadorSintaxe = False
                    print(f"[ERRO] (linha {linha+1}) - Caractere {texto[caractere]} Invalido.\n")
            elif (validador.validar_fim(texto) and linha == tamConteudo):
                validadorSintaxe = True
            else:
                validadorSintaxe = False
                print(f"[ERRO] (linha {linha+1}) - Conteudo '{texto}' invalido. Erro de sintaxe. \n")

            caractere = 0
            linha+=1
            
 
    if (validadorSintaxe == False):
        limpar_indice_auxiliar()
    else:
        print("[INFO] - Montagem do conteudo hexadecimal realizada com sucesso.\n")

    return validadorSintaxe