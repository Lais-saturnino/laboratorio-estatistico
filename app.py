
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


import minhastats


st.title("Laboratório Estatístico Interativo")
st.caption("Sistematização - Matemática e Estatística para computação - Lais dos Santos Silva Saturnino")
st.caption("Todas as medidas são calculadas pela biblioteca minhastats.py, escrita à mão, sem funções estatísticas prontas.")


dados = pd.read_csv("insurance.csv")


st.write("Total de registros:", len(dados))
st.dataframe(dados.head(10))

coluna = st.selectbox("Escolha uma variável:", ["age", "bmi", "children", "charges"])

valores = dados[coluna].tolist()

st.subheader(f"Medidas de {coluna}")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Média", f"{minhastats.media(valores):.2f}")
col2.metric("Mediana", f"{minhastats.mediana(valores):.2f}")
col3.metric("Desvio padrão", f"{minhastats.desvio_padrao(valores):.2f}")
col4.metric("Coef. variação", f"{minhastats.coeficiente_variacao(valores):.1f}%")


st.subheader("Histograma")

figura, eixo = plt.subplots()
eixo.hist(valores, bins=20, color="steelblue", edgecolor="white")
eixo.set_xlabel(coluna)
eixo.set_ylabel("Frequência")
st.pyplot(figura)


st.subheader("Boxplot e outliers")

fig2, eixo2 = plt.subplots()
eixo2.boxplot(valores, vert=False)
eixo2.set_xlabel(coluna)
st.pyplot(fig2)

outliers = minhastats.detectar_outliers(valores)
st.write(f"Quantidade de outliers encontrados: {len(outliers)}")

st.subheader("Distribuição por categoria")

categoria = st.selectbox("Escolha uma categoria:", ["sex", "smoker", "region"])

contagem = dados[categoria].value_counts()

fig3, eixo3 = plt.subplots()
eixo3.bar(contagem.index, contagem.values, color="steelblue")
eixo3.set_xlabel(categoria)
eixo3.set_ylabel("Quantidade")
st.pyplot(fig3)

st.subheader("Interpretação automática")

media_valor = minhastats.media(valores)
mediana_valor = minhastats.mediana(valores)

if media_valor > mediana_valor:
    st.info(f"A média ({media_valor:.2f}) é maior que a mediana ({mediana_valor:.2f}): a distribuição de {coluna} é assimétrica à direita, puxada por valores altos.")
elif media_valor <mediana_valor:
    st.info(f"A média ({media_valor:.2f}) é menor que a mediana ({mediana_valor:.2f}): a distribuição de {coluna} é assimétrica à esquerda.")
else:
    st.info(f"Média e mediana de {coluna} são iguais: distribuição simétrica.")



st.subheader("Regressão linear")

var_x = st.selectbox("Variável X:", ["age", "bmi", "children"], key="x")
var_y = st.selectbox("Variável Y:", ["charges"], key="y")

x = dados[var_x].tolist()
y = dados[var_y].tolist()

inclinacao, intercepto = minhastats.regressao_linear(x, y)
r2 = minhastats.r_quadrado(x, y)

fig4, eixo4 = plt.subplots()
eixo4.scatter(x, y, alpha=0.4, color="orange")

reta_x = [min(x), max(x)]
reta_y = [inclinacao * v + intercepto for v in reta_x]
eixo4.plot(reta_x, reta_y, color="steelblue")

eixo4.set_xlabel(var_x)
eixo4.set_ylabel(var_y)
st.pyplot(fig4)

st.write(f"R² = {r2:.3f}")
st.warning("Correlação não implica causalidade: a reta mostra uma relação estatística, não uma relação de causa e efeito.")


