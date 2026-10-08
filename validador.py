#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

# Arquivo que armazena todas as funcoes de validacao do conteudo da variavel auxiliar conteudo, que contem o conteudo do arquivo .ula, e que sera convertido para hexadecimal e gravado no arquivo .hex

import mnemonicos

def validar_inicio(texto):
    """Funcao que valida o texto de inicio do arquivo .ula.

    Args:
        texto: string contendo o texto a ser validado

    Returns:
        validacao: booleano indicando se o texto de inicio foi validado com sucesso
    """
    validacao = False

    if (texto == "inicio:"):
        validacao = True
    return validacao

def validar_fim(texto):
    """Funcao que valida o texto de fim do arquivo .ula.

    Args:
        texto: string contendo o texto a ser validado

    Returns:
        validacao: booleano indicando se o texto de fim foi validado com sucesso
    """
    validacao = False

    if (texto == "fim."):
        validacao = True

    return validacao

def validar_conteudo_vazio(conteudo):
    """Funcao que valida se o conteudo do arquivo .ula esta vazio.

    Args:
        conteudo: lista contendo o conteudo do arquivo .ula

    Returns:
        validacao: booleano indicando se o conteudo do arquivo .ula esta vazio
    """

    validacao = True

    # valida se o conteudo do arquivo .ula esta vazio, caso esteja, um erro e informado
    if not (conteudo):
        validacao = False
        print(f"[ERRO] - Conteudo do arquivo esta vazio!\n")

    return validacao 

def validar_igual(texto):
    """Funcao que valida se o texto contem o operador '='.

    Args:
        texto: string contendo o texto a ser validado

    Returns:
        validacao: booleano indicando se o texto contem o operador '='
    """

    validacao = False

    if (texto == '='):
        validacao = True
    else:
        print(f"[ERRO] - Necessario operador '=' apos variavel.\n")

    return validacao

def validar_x(var):
    """Funcao que valida se o texto contem a variavel 'X'.

    Args:
        var: string contendo o texto a ser validado

    Returns:
        validacao: booleano indicando se o texto contem a variavel 'X'
    """
    validacao = False

    if (var == 'X'):
        validacao = True

    return validacao

def validar_y(var):
    """Funcao que valida se o texto contem a variavel 'Y'.
    
    Args:
        var: string contendo o texto a ser validado

    Returns:
        validacao: booleano indicando se o texto contem a variavel 'Y'
    """
    validacao = False

    if (var == 'Y'):
        validacao = True

    return validacao

def validar_operador(var):
    """Funcao que valida se o texto contem a variavel 'W'.
    
    Args:
        var: string contendo o texto a ser validado

    Returns:
        validacao: booleano indicando se o texto contem a variavel 'W'
    """
    validacao = False

    if (var == 'W'):
        validacao = True

    return validacao

def validar_pontovirgula(texto):
    """Funcao que valida se o texto contem o operador ';'.
    
    Args:
        texto: string contendo o texto a ser validado

    Returns:
        validacao: booleano indicando se o texto contem o operador ';'
    """
    validacao = False

    if (texto.endswith(';')):
        validacao = True

    return validacao

def validar_hexa(valor):
    """Funcao que valida se o valor esta entre 0 e 15.

    Args:
        valor: inteiro contendo o valor a ser validado

    Returns:
        validacao: booleano indicando se o valor esta entre 0 e 15
    """
    validacao = False

    if (valor >= 0 and valor <= 15):
        validacao = True

    return validacao

def validar_mnemonico(texto):
    """Funcao que valida se o texto contem um mnemonico valido.

    Args:
        texto: string contendo o texto a ser validado

    Returns:
        mnemonico: inteiro contendo o valor do mnemonico valido, ou -1 se o mnemonico for invalido
    """
    return mnemonicos.hash_mnemonicos.get(texto, -1)
    

