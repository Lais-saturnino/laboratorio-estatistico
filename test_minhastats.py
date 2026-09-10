import statistics
import minhastats

DADOS = [2.0, 3.0, 5.0, 5.5, 6.0, 6.8, 5.0, 5.5, 5.2, 6.0]
TOLERANCIA = 1e-9

def test_media():
    assert abs(minhastats.media(DADOS)- statistics.mean(DADOS)) < TOLERANCIA

