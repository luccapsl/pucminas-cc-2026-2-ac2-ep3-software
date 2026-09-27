import gestao_arquivo
import montador
import validador
from variaveis import nomeArquivo_hex, nomeArquivo_ula, conteudo, conteudoHexadecimal

# Arquivo principal do programa, que realiza a leitura do arquivo .ula, valida o conteudo e monta o arquivo .hex

print("-----------------------------------")
print("Exercicio Pratico 3 - Arquitetura de Computadores 2")
print("Ciencia da Computacao 2026/2 - PUC Minas")
print("Ana Flavia, Clarisse de Assis, Jamille Micaele, Julia Batista, Lucca de Paula")
print("\n")
print("Montador de arquivo .ula para .hex")
print("-----------------------------------")
print("\n[INFO] - Inicio do programa de montagem de arquivo .ula para .hex\n")

conteudo = gestao_arquivo.ler_arquivo_ula(nomeArquivo_ula)

if (validador.validar_conteudo_vazio(conteudo)):

    if (montador.montagem_texto_hexa(conteudo)):
        gestao_arquivo.escrever_arquivo_hex(nomeArquivo_hex)
    else:
        print("[ERRO] - Montagem do arquivo .hex nao realizada devido a erros de sintaxe.\n")