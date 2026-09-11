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
