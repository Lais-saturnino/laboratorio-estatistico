"""
test_minhastats.py
Testes automatizados: comparam MINHAS funcoes com as bibliotecas prontas.

Se der tudo "passed", minhas formulas estao certas.
Rodar com:  pytest -v
"""

import statistics
import numpy as np

import minhastats

# Uma listinha de numeros para testar
DADOS = [2.0, 3.0, 5.0, 5.5, 6.0, 6.8, 5.0, 5.5, 5.2, 6.0]

TOLERANCIA = 1e-9   # margem de erro aceita (0,000000001)


def test_media():
    assert abs(minhastats.media(DADOS) - statistics.mean(DADOS)) < TOLERANCIA


def test_mediana():
    assert abs(minhastats.mediana(DADOS) - statistics.median(DADOS)) < TOLERANCIA


def test_mediana_quantidade_par():
    dados_par = [1, 2, 3, 4]
    assert abs(minhastats.mediana(dados_par) - statistics.median(dados_par)) < TOLERANCIA


def test_variancia_amostral():
    esperado = statistics.variance(DADOS)          # variancia amostral (n-1)
    assert abs(minhastats.variancia(DADOS, amostral=True) - esperado) < TOLERANCIA


def test_variancia_populacional():
    esperado = np.var(DADOS)                       # numpy usa n por padrao
    assert abs(minhastats.variancia(DADOS, amostral=False) - esperado) < TOLERANCIA


def test_desvio_padrao_amostral():
    esperado = statistics.stdev(DADOS)
    assert abs(minhastats.desvio_padrao(DADOS, amostral=True) - esperado) < TOLERANCIA
