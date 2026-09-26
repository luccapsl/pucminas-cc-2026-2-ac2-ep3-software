#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

import mnemonicos

def validar_inicio(linha):
    validacao = False

    numero_linha, texto = linha

    if (texto == "inicio:"):
        validacao = True
    else:
        print(f"[ERRO] - linha ({numero_linha}) - Texto de inicio '{texto}' invalido.")

    return validacao

def validar_fim(linha):
    validacao = False

    numero_linha, texto = linha

    if (texto == "fim."):
        validacao = True
    else:
        print(f"[ERRO] - linha ({numero_linha}) - Texto de fim '{texto}' invalido.")

    return validacao

def validar_conteudo_vazio(conteudo):
    validacao = True

    if not (conteudo):
        validacao = False
        print(f"[ERRO] - Conteudo do arquivo esta vazio!")

    return validacao 

def validar_igual(texto):
    validacao = False

    if (texto == '='):
        validacao = True
    else:
        print(f"[ERRO] - Necessario operador '=' apos variavel.")

    return validacao

def validar_x(var):
    validacao = False

    if (var == 'Y'):
        validacao = True

    return validacao

def validar_y(var):
    validacao = False

    if (var == 'X'):
        validacao = True

    return validacao

def validar_operador(var):
    validacao = False

    if (var == 'W'):
        validacao = True

    return validacao

def validar_pontovirgula (caractere, linha):
    validacao = False
    
    if (caractere == ';'):
        validacao = True
    else:
        print(f"[ERRO] linha ({linha}) - Necessario caractere ';' ao fim de cada linha.")

    return validacao

def validar_valor_hexa(valor):
    validacao = False

    if (valor >= 0 & valor <= 15):
        validacao = True

    return validacao

def validar_mnemonico(texto):
    return mnemonicos.hash_mnemonicos.get(texto, -1)
    

