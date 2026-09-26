#----------------------------------#
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula
# ----------------------------------#

def mnem_nA(a, b):
    return int(not a)

def mnem_AoBn(a, b):
    return int(not (a or b))

def mnem_nAeB(a, b):
    return int((not a) and b)

def mnem_zeroL(a, b):
    return 0

def mnem_AeBn(a, b):
    return int(not (a and b))

def mnem_nB(a, b):
    return int(not b)

def mnem_AxB(a, b):
    return int(((not a) and b) or (a and (not b)))

def mnem_AenB(a, b):
    return int(a and (not b))

def mnem_nAoB(a, b):
    return int((not a) or b)

def mnem_AxBn(a, b):
    return int((a and b) or ((not a) and (not b)))

def mnem_copiaB(a, b):
    return b

def mnem_AeB(a, b):
    return int(a and b)

def mnem_umL(a, b):
    return 1

def mnem_AonB(a, b):
    return int(a or (not b))

def mnem_AoB(a, b):
    return int(a or b)

def mnem_copiaA(a, b):
    return a
