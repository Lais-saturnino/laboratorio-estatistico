def media(dados):
    soma = 0
    for valor in dados:
        soma = soma + valor
        
    return soma / len(dados)


def mediana(dados):
    ordenados = sorted(dados)

    n = len(ordenados)
    meio = n // 2

    if n % 2 == 1:
        return ordenados[meio]
    else:
         return (ordenados [meio -1] + ordenados[meio]) / 2

def amplitude(dados):
    return max(dados) - min(dados)


def moda(dados):
    contagem = {}
    for valor in dados:
        if valor in contagem:
            contagem[valor] = contagem[valor] + 1
        else:
            contagem[valor] = 1

    return max(contagem, key=contagem.get)
            


def variancia(dados , amostral=True):
    m = media(dados)
    soma_quadrados = 0
    for valor in dados:
        soma_quadrados = soma_quadrados + (valor - m) **2

    
    if amostral:
        return soma_quadrados / (len(dados) -1)
    else:
        return soma_quadrados / len(dados)


def desvio_padrao(dados, amostral=True):
    return variancia(dados, amostral) ** 0.5


def coeficiente_variacao(dados):
    return desvio_padrao(dados) / media(dados) * 100

def percentil(dados, p):
    ordenados = sorted(dados)
    n = len(ordenados)
    posicao = (n - 1) * p / 100
    inferior = int(posicao)
    resto = posicao - inferior

    if inferior + 1 < n:
        return ordenados[inferior] + resto * (ordenados[inferior + 1] - ordenados[inferior])
    else:
        return ordenados[inferior]


def quartis(dados):
    return percentil(dados, 25), percentil(dados, 50), percentil(dados, 75)


def covariancia(x, y, amostral=True):
    mx = media(x)
    my = media(y)
    soma_produtos = 0
    for a, b in zip(x, y):
        soma_produtos = soma_produtos + (a - mx) * (b - my)

    if amostral:
        return soma_produtos / (len(x) -1)
    else:
        return soma_produtos / len(x)


def correlacao_pearson(x, y):
    return covariancia(x, y) / (desvio_padrao(x) * desvio_padrao(y))

