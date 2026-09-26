import gestao_arquivo
import montador
import validador
from variaveis import nomeArquivo_hex, nomeArquivo_ula, conteudo

conteudo = gestao_arquivo.ler_arquivo_ula(nomeArquivo_ula)

#print(conteudo)

if (validador.validar_conteudo_vazio(conteudo)):


    
    conteudoHexadecimal = montador.montagem_texto_hexa(conteudo)
    
    print(conteudoHexadecimal)
    
    gestao_arquivo.escrever_arquivo_hex(nomeArquivo_hex, conteudoHexadecimal)