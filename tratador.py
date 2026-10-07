# ---------------------------------- #
# Exercicio Pratico 3
# Arquitetura de Computadores 2
# Ciencia da Computacao 2026/2 - PUC Minas
# Ana Flavia, Clarisse de Assis, Jamille Micaele,
# Julia Batista, Lucca de Paula
# ---------------------------------- #

# Arquivo responsavel por realizar tratamentos simples
# no conteudo lido do arquivo .ula.
#
# Este modulo NAO decide se uma linha esta correta ou errada.
# Essa responsabilidade pertence ao validador.py.
#
# Aqui ficam apenas funcoes auxiliares, como:
# - limpeza das linhas;
# - extracao de numeros;
# - conversao decimal para hexadecimal;
# - extracao de mnemonicos.


def limpeza_texto_linha(texto):
    """
    Recebe uma linha do arquivo .ula e remove caracteres
    que podem atrapalhar a analise sintatica.

    Sao removidos:
    - '\n' -> quebra de linha;
    - '\r' -> retorno de carro, comum em arquivos Windows;
    - ' '  -> espacos;
    - '\t' -> tabulacoes.

    Exemplo:

        " X = 12;\\n"

    torna-se:

        "X=12;"

    Args:
        texto: string contendo a linha original.

    Returns:
        String limpa.
    """

    # Remove a quebra de linha.
    texto = texto.replace('\n', '')

    # Remove o retorno de carro.
    # Isso evita problemas quando o arquivo utiliza CRLF.
    texto = texto.replace('\r', '')

    # Remove espacos comuns.
    texto = texto.replace(' ', '')

    # Remove tabulacoes.
    # Isso tambem foi incluido para tornar a leitura
    # mais robusta.
    texto = texto.replace('\t', '')

    return texto


def tratar_numero(texto, caractere):
    """
    Recebe um texto e a posicao inicial onde deve procurar
    um numero.

    A funcao percorre o texto enquanto encontrar digitos
    numericos e monta uma string contendo esse numero.

    Exemplo:

        texto = "X=123;"
        caractere = 2

    Resultado:

        123

    Se nao houver nenhum numero na posicao indicada,
    retorna None.

    Isso e importante para casos como:

        X=;
        Y=;

    pois nessas situacoes nao devemos tentar fazer
    int(''), o que causaria uma excecao.

    Args:
        texto: string contendo o texto.
        caractere: indice inicial da procura.

    Returns:
        Inteiro contendo o numero encontrado ou None.
    """

    numero = ''

    # Continua enquanto:
    # 1. o indice estiver dentro do texto;
    # 2. o caractere atual for um digito.
    while (caractere < len(texto) and texto[caractere].isdigit()):

        # Adiciona o digito encontrado ao numero.
        numero += texto[caractere]

        # Avanca para o proximo caractere.
        caractere += 1

    # Se nenhum digito foi encontrado,
    # nao existe numero para retornar.
    if numero == '':
        return None

    # Converte a string numerica para inteiro.
    return int(numero)


def converter_hexadecimal(numero):
    """
    Recebe um numero inteiro decimal e converte para
    hexadecimal.

    A funcao hex() do Python retorna, por exemplo:

        hex(10) -> '0xa'

    Como o projeto precisa apenas do numero hexadecimal,
    removemos o prefixo '0x' e transformamos as letras
    em maiusculas.

    Exemplos:

        10 -> A
        11 -> B
        12 -> C
        13 -> D
        14 -> E
        15 -> F

    Args:
        numero: inteiro contendo o numero decimal.

    Returns:
        String contendo o numero hexadecimal em maiusculo.
    """

    return hex(numero).replace("0x", "").upper()


def tratar_mnemonico(texto, caractere):
    """
    Recebe um texto e a posicao inicial do mnemonico.

    A funcao percorre os caracteres enquanto forem letras.

    Exemplo:

        texto = "W=AeB;"
        caractere = 2

    Resultado:

        "AeB"

    O ponto e virgula nao entra no mnemonico porque nao e
    uma letra.

    Args:
        texto: string contendo o texto.
        caractere: indice inicial do mnemonico.

    Returns:
        String contendo o mnemonico encontrado.
    """

    mnemonico = ''

    # Continua enquanto estiver dentro do texto e encontrar
    # caracteres alfabeticos.
    while (caractere < len(texto) and texto[caractere].isalpha()):

        # Adiciona a letra ao mnemonico.
        mnemonico += texto[caractere]

        # Avanca para o proximo caractere.
        caractere += 1

    return mnemonico