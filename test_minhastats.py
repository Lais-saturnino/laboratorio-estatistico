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
DADOS_Y = [1.0, 2.5, 4.0, 5.0, 6.5, 7.0, 4.5, 5.0, 4.8, 6.2]


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



def test_moda_quando_nao_e_o_primeiro():
    assert minhastats.moda([1, 2, 2, 2]) == 2


def test_quartis():
    q1, q2, q3 = minhastats.quartis(DADOS)
    esperados = numpy.percentile(DADOS, [25, 50, 75])
    assert abs(q1 - esperados[0]) < TOLERANCIA
    assert abs(q2 - esperados[1]) < TOLERANCIA
    assert abs(q3 - esperados[2]) < TOLERANCIA


def test_percentil():
    assert abs(minhastats.percentil(DADOS, 90) - numpy.percentile(DADOS, 90)) <TOLERANCIA


def test_covariancia_amostral():
    esperado = numpy.cov(DADOS, DADOS_Y)[0][1] 
    assert abs(minhastats.covariancia(DADOS, DADOS_Y) - esperado) < TOLERANCIA


def test_covariancia_populacional():
    esperado = numpy.cov(DADOS, DADOS_Y, ddof=0)[0][1]
    assert abs(minhastats.covariancia(DADOS, DADOS_Y, amostral=False) - esperado) < TOLERANCIA


def test_correlacao_pearson():
    esperado = numpy.corrcoef(DADOS, DADOS_Y) [0][1]
    assert abs(minhastats.correlacao_pearson(DADOS, DADOS_Y) - esperado) < TOLERANCIA

# O numpy nao tem funcao pronta de IQR nem de limites de outlier.
# Por isso a referencia e montada com numpy.percentile, que e independente
# do meu percentil: continua sendo uma conferencia de fora.


def test_iqr():
    q1 = numpy.percentile(DADOS, 25)
    q3 = numpy.percentile(DADOS, 75)
    assert abs(minhastats.iqr(DADOS) - (q3 - q1)) < TOLERANCIA


def test_limites_outliers():
    q1 = numpy.percentile(DADOS, 25)
    q3 = numpy.percentile(DADOS, 75)
    intervalo = q3 - q1
    inferior, superior = minhastats.limites_outliers(DADOS)
    assert abs(inferior - (q1 - 1.5 * intervalo)) < TOLERANCIA
    assert abs(superior - (q3 + 1.5 * intervalo)) < TOLERANCIA
    

def test_detectar_outliers():
    assert minhastats.detectar_outliers(DADOS) == [2.0, 3.0]
    

def test_detectar_outliers_sem_nenhum():
    assert minhastats.detectar_outliers([10, 11, 12, 13, 14]) == []


def test_tabela_frequencia_bate_com_numpy():
    contagens, limites = numpy.histogram(DADOS, bins=5)
    minha = minhastats.tabela_frequencia(DADOS, 5)
    for i in range(5):
        assert minha[i]["frequencia"] == contagens[i]
        assert abs(minha[i]["inicio"] - limites[i]) < TOLERANCIA


def test_tabela_frequencia_soma_o_total():
    soma = 0
    for linha in minhastats.tabela_frequencia(DADOS):
        soma = soma + linha["frequencia"]
    assert soma == len(DADOS)


def test_tabela_frequencia_acumulada_final():
    tabela = minhastats.tabela_frequencia(DADOS)
    assert tabela[-1]["acumulada"] == len(DADOS)


def test_regressao_linear():
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]
    inclinacao, intercepto = minhastats.regressao_linear(x, y)
    assert abs(inclinacao - 2.0) < TOLERANCIA
    assert abs(intercepto - 0.0) < TOLERANCIA


def test_r_quadrado():
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]
    assert abs(minhastats.r_quadrado(x, y) - 1.0) < TOLERANCIA
