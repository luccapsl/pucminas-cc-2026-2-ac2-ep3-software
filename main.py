import os

import gestao_arquivo
import montador
import validador

from variaveis import nomeArquivo_hex, nomeArquivo_ula


print("-----------------------------------")
print("Exercicio Pratico 3 - Arquitetura de Computadores 2")
print("Ciencia da Computacao 2026/2 - PUC Minas")
print("Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula")
print()
print("Montador de arquivo .ula para .hex")
print("-----------------------------------")
print()
print("[INFO] - Inicio do programa de montagem de arquivo .ula para .hex")
print()

conteudo = gestao_arquivo.ler_arquivo_ula(nomeArquivo_ula)

if validador.validar_conteudo_vazio(conteudo):
    if montador.montagem_texto_hexa(conteudo):
        gestao_arquivo.escrever_arquivo_hex(nomeArquivo_hex)
    else:
        if os.path.exists(nomeArquivo_hex):
            os.remove(nomeArquivo_hex)

        print(
            "[ERRO] - Montagem do arquivo .hex nao realizada "
            "devido a erros estruturais."
        )
