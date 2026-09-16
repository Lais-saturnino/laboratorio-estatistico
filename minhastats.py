"""
minhastats.py
Biblioteca estatistica propria - Laboratorio Estatistico Interativo.

REGRA DO TRABALHO: nada de numpy.mean(), statistics.mean() etc.
Aqui tudo e calculado na mao, com laco de repeticao e as formulas.
"""


def media(dados):
    """
    Media aritmetica.

    Formula:  media = (soma de todos os valores) / (quantidade de valores)
    """
    soma = 0            # comeca o acumulador no zero
    for valor in dados:  # passa por cada numero da lista
        soma = soma + valor   # vai somando
    return soma / len(dados)  # divide pela quantidade


def mediana(dados):
    """
    Mediana: o valor que fica bem no meio, com os dados ordenados.

    - Se a quantidade for IMPAR: e o valor central.
    - Se for PAR: e a media dos dois valores centrais.
    """
    ordenados = sorted(dados)   # sorted() so ordena, nao calcula estatistica
    n = len(ordenados)
    meio = n // 2               # divisao inteira

    if n % 2 == 1:              # quantidade impar
        return ordenados[meio]
    else:                       # quantidade par
        return (ordenados[meio - 1] + ordenados[meio]) / 2


def variancia(dados, amostral=True):
    """
    Variancia: media dos desvios ao quadrado.

    Formula:  variancia = soma((cada valor - media)^2) / divisor

    divisor = n - 1  -> variancia AMOSTRAL   (padrao)
    divisor = n      -> variancia POPULACIONAL
    """
    m = media(dados)            # reaproveita a funcao que ja escrevemos
    soma_quadrados = 0
    for valor in dados:
        desvio = valor - m               # distancia ate a media
        soma_quadrados += desvio ** 2    # eleva ao quadrado e acumula

    n = len(dados)
    divisor = n - 1 if amostral else n
    return soma_quadrados / divisor


def desvio_padrao(dados, amostral=True):
    """
    Desvio padrao: a raiz quadrada da variancia.

    Serve para voltar a unidade original (a variancia fica em unidade ao quadrado).
    """
    return variancia(dados, amostral) ** 0.5
