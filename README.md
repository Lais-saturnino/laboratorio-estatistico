# Laboratório Estatístico Interativo 🔬

Sistematização da disciplina Matemática e Estatística para Computação (Turma B, Prof. Romes Heriberto) - CEUB.

**Autora:** Lais dos Santos Silva Saturnino 

<img width="256" height="256" alt="image" src="https://github.com/user-attachments/assets/cca2eb4d-95f0-48d3-b6f2-27d5720cc8f2" />

## O que é:

Uma biblioteca de estatística escrita do zero em Python, sem usar funções prontas como 'numpy.mean()' ou 'statistics.stdev()', validada por testes automatizados contra Numpy e a biblioteca 'statistics'. Os resultados são apresentados numa tela interativa feita com Streamlit, usando o dataset [Medical Cost Personal](https://www.kaggle.com/datasets/mirichoi0218/insurance) (1.338 registros).

## Estrutura 

- `minhastats.py` — a biblioteca estatística, com 17 funções escritas à mão
- `test_minhastats.py` — 24 testes automatizados, validando cada função contra NumPy/statistics
- `app.py` — a tela interativa (Streamlit)
- `insurance.csv` — o dataset usado
- `RELATORIO.md` — o relatório da sistematização

## Como rodar

Pré-requisitos: Python 3.12, com as bibliotecas instaladas.

```
pip install -r requirements.txt
pytest
streamlit run app.py
```

## Funções da biblioteca

Média, mediana, amplitude, moda, variância (amostral e populacional), desvio padrão, coeficiente de variação, percentil, quartis, covariância, correlação de Pearson, IQR, limites de outliers, detecção de outliers, tabela de frequência, regressão linear e R².
