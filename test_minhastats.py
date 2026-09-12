import statistics
import numpy
import minhastats

DADOS = [2.0, 3.0, 5.0, 5.5, 6.0, 6.8, 5.0, 5.5, 5.2, 6.0]
TOLERANCIA = 1e-9

def test_media():
    assert abs(minhastats.media(DADOS)- statistics.mean(DADOS)) < TOLERANCIA

def test_mediana():
     assert abs(minhastats.mediana(DADOS)-statistics.median(DADOS)) < TOLERANCIA


def test_amplitude():
    assert abs(minhastats.amplitude(DADOS) - numpy.ptp(DADOS)) < TOLERANCIA

DADOS_MODA =[7,8,7,9,10,7,8]


def test_moda():
    assert minhastats.moda(DADOS_MODA) == statistics.mode(DADOS_MODA)

    
def test_variancia_amostral():
    assert abs(minhastats.variancia(DADOS) - statistics.variance(DADOS)) < TOLERANCIA


def test_variancia_populacional():
    assert abs(minhastats.variancia(DADOS, amostral=False) - statistics.pvariance(DADOS)) < TOLERANCIA


def test_desvio_padrao_amostral():
    assert abs(minhastats.desvio_padrao(DADOS) - statistics.stdev(DADOS)) < TOLERANCIA
    

def test_desvio_padrao_populacional():
    assert abs(minhastats.desvio_padrao(DADOS, amostral=False) - statistics.pstdev(DADOS)) < TOLERANCIA


# O STATISTICS E O NUMPY NAO TEM FUNCAO PRONTA DE COEFICIENTE DE VARIACAO.
# POR ISSO A REFERENCIA E MONTADA COM STDEV E MEAN DAS PROPRIAS BIBLIOTECAS.

    

def test_coeficiente_variacao():
    esperado = statistics.stdev(DADOS) / statistics.mean(DADOS) * 100
    assert abs(minhastats.coeficiente_variacao(DADOS) - esperado) < TOLERANCIA
