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
