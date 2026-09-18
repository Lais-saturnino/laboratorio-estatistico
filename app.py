
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
reta_y = []
for v in reta_x:
    reta_y.append(inclinacao * v + intercepto)


eixo4.plot(reta_x, reta_y, color="steelblue")

eixo4.set_xlabel(var_x)
eixo4.set_ylabel(var_y)
st.pyplot(fig4)

st.write(f"R² = {r2:.3f}")
st.warning("Correlação não implica causalidade: a reta mostra uma relação estatística, não uma relaçãode causa e efeito.")
st.subheader("Módulo 3 - Lei dos Grandes Números")

n_jogadas = st.slider("Número de jogadas:", 10, 5000, 100)

frequencias = minhastats.simular_moeda(n_jogadas)

fig5, eixo5 = plt.subplots()
eixo5.plot(frequencias, color="steelblue")
eixo5.axhline(0.5, color="red", linestyle="--")
eixo.set_xlabel("Número de jogadas")
eixo5.set_ylabel("Frequência de 'cara'")
st.pyplot(fig5)

st.write(f"Depois de {n_jogadas} jogadas, a frequência de cara foi {frequencias[-1]:.3f}")
st.subheader("Módulo 3 - Teorema Central do Limite")

variavel_tcl = st.selectbox("Escolha uma variável:", ["age", "bmi", "children", "charges"], key="tcl")

valores_tcl = dados[variavel_tcl].tolist()

tamanho_amostra = st.slider("Tamanho de cada amostra:", 5, 200, 30)
n_amostras = st.slider("Número de amostras:", 100, 2000, 500)

medias_amostrais = minhastats.simular_tcl(valores_tcl, tamanho_amostra, n_amostras)

fig6, eixo6 = plt.subplots()
eixo6.hist(medias_amostrais, bins=30, color="steelblue", edgecolor="white")
eixo6.set_xlabel(f"Média da amostra de {variavel_tcl}")
eixo6.set_ylabel("Frequência")
st.pyplot(fig6)

st.write(f"Média das {n_amostras} médias amostrais: {minhastats.media(medias_amostrais):.2f}")
st.subheader("Módulo 4 - Distribuições Teóricas")

st.write("Ajuste da curva Normal na variável bmi")

valores_bmi = dados["bmi"].tolist()
media_bmi = minhastats.media(valores_bmi)
desvio_bmi = minhastats.desvio_padrao(valores_bmi)

minimo_bmi = min(valores_bmi)
maximo_bmi = max(valores_bmi)
passo = (maximo_bmi - minimo_bmi) / 100

eixo_x = []
eixo_y = []
for i in range(100):
    x = minimo_bmi + i * passo
    eixo_x.append(x)
    eixo_y.append(minhastats.normal_pdf(x, media_bmi, desvio_bmi))


fig7, eixo7 = plt.subplots()
eixo7.hist(valores_bmi, bins=30, color="steelblue", edgecolor="white", density=True)
eixo7.plot(eixo_x, eixo_y, color="red")
eixo7.set_xlabel("bmi")
eixo7.set_ylabel("Densidade")
st.pyplot(fig7)

st.write("Ajuste da curva Exponencial na variável charges")

valores_charges = dados["charges"].tolist()
media_charges = minhastats.media(valores_charges)
taxa_charges = 1 / media_charges

minimo_charges = min(valores_charges)
maximo_charges = max(valores_charges)
passo_charges = (maximo_charges - minimo_charges) / 100

eixo_x2 = []
eixo_y2 = []
for i in range(100):
    x = minimo_charges + i * passo_charges
    eixo_x2.append(x)
    eixo_y2.append(minhastats.exponencial_pdf(x, taxa_charges))

fig8, eixo8 = plt.subplots()
eixo8.hist(valores_charges, bins=30, color="steelblue", edgecolor="white", density=True)
eixo8.plot(eixo_x2, eixo_y2, color="red")
eixo8.set_xlabel("charges")
eixo8.set_ylabel("Densidade")
st.pyplot(fig8)
