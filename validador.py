#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

def validar_inicio(texto):
    validacao = False

    if (texto == "inicio:"):
        validacao = True
    else:
        print("[ERRO] - Texto de inicio %s invalido.", texto)

    return validacao

def validar_fim(texto):
    validacao = False

    if (texto == "fim"):
        validacao = True
    else:
        print("[ERRO] - Texto de finalizacao %s invalido.", texto)

    return validacao 

def validar_conteudo_vazio(conteudo):
    validacao = True

    if not (conteudo):
        validacao = False
        print("[ERRO] - Conteudo do arquivo esta vazio!")
        
    return validacao 

def validar_igual(texto):
    validacao = False

    if (texto == '='):
        validacao = True
    else:
        print("[ERRO] - Necessario operador '=' apos variavel.")

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



def validar_valor_hexa(valor):
    validacao = False

    if (valor >= 0 & valor <= 15):
        validacao = True

    return validacao

def validar_mnemonico(texto):
    case 
