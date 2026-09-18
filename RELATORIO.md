# Relatório da Sistematização — Laboratório Estatístico Interativo


**Aluna:** Lais dos Santos Silva Saturnino


**Disciplina:** Matemática e Estatística para Computação (Turma B) — Prof. Romes Heriberto


**Dataset:** Medical Cost Personal (Kaggle), 1.338 registros


## 1. Módulo 1 — Biblioteca estatística


Escrevi 11 funções no arquivo `minhastats.py`: média, mediana, amplitude, moda, variância (amostral e populacional), desvio padrão, coeficiente de variação, percentil, quartis, covariância e correlação de Pearson. Nenhuma delas usa função pronta de estatística (nada de `numpy.mean()` ou `statistics.stdev()`) — todas foram calculadas com laço de repetição e as fórmulas na mão.

Para conferir se as contas estavam certas, escrevi 24 testes automatizados (`test_minhastats.py`), comparando cada resultado meu com o do `numpy` e do `statistics`. Usei uma margem de erro de `1e-9`, porque o computador arredonda número decimal e as duas contas podem diferir numa casa decimal bem distante sem isso ser erro de verdade.

**Duas decisões que tomei:**

- Para o quartil, existe mais de um jeito de calcular. Eu usei interpolação (que "anda" entre dois valores vizinhos), porque é o mesmo método que o `numpy.percentile` usa — assim meu teste compara com a mesma referência.
- Para a correlação de Pearson, existem duas fórmulas equivalentes. Escolhi a que usa covariância dividida pelos dois desvios padrão, porque ela reaproveita funções que eu já tinha escrito, e porque deixa mais claro de onde o número vem.

**Um bug que encontrei:** a função `moda` tinha um erro de indentação — o `return` estava dentro do `else`, então ela devolvia a resposta assim que via o primeiro valor repetido, sem terminar de contar. O teste que eu tinha passava mesmo assim, porque a lista usada começava justamente pelo valor certo — foi coincidência. Só descobri o erro testando `moda([1, 2, 2, 2])`, que devolvia `1` em vez de `2`. Corrigi e criei um teste novo (`test_moda_quando_nao_e_o_primeiro`) para esse caso não voltar a passar despercebido.


## 2. Módulo 2 — Análise exploratória


Criei as funções `iqr`, `limites_outliers`, `detectar_outliers` e `tabela_frequencia`, todas usando as funções do Módulo 1 por baixo. Os outliers são definidos pela regra clássica: qualquer valor abaixo de `Q1 − 1,5×IQR` ou acima de `Q3 + 1,5×IQR`.

Na tela do programa, olhando a coluna `charges` (custo do plano), a média deu 13.270,42 e a mediana deu 9.382,03 — a média bem mais alta mostra que a distribuição é puxada por valores altos. O programa encontrou 139 outliers nessa coluna, o que faz sentido: provavelmente é o grupo de pessoas fumantes, que pagam bem mais caro que a maioria.

## 3. Módulo 5 — Regressão linear

Criei as funções `regressao_linear` (calcula a inclinação e o ponto onde a reta corta o eixo) e `r_quadrado` (mede o quanto a reta explica os dados).

Relacionando `bmi` (índice de massa corporal) com `charges`, o R² deu 0,039 — ou seja, o BMI sozinho explica menos de 4% da  da variação no custo do plano. A tela mostra um aviso: correlação não é a mesma coisa que causa e efeito. A reta mostra que as duas variáveis andam um pouco juntas, mas não prova que uma seja a causa da outra.


## 4. Testes


No total, 24 testes, todos passando. Não são só os casos "fáceis" — tem também casos de borda, como uma lista sem nenhum outlier e uma lista onde a moda não é o primeiro valor. Esses testes existem porque um teste com dado fácil pode passar mesmo com o código errado, como aconteceu com a `moda`.



## 5. Conclusão

O maior desafio deste trabalho foi dar início ao desenvolvimento do código e colocar em prática a matemática em Python. Fui escrevendo cada função com calma, testando uma de cada vez, e usei livros de referência, aulas  para entender a lógica por trás de cada linha antes de digitar.

A parte que mais me ensinou foi o erro da moda. Entendi que teste passando não significa que o código está certo, só significa que aquele caso em específico está certo.
