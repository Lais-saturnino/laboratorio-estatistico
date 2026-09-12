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
