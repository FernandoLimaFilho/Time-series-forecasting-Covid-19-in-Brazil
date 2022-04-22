# Prevendo novos casos e mortes diárias por covid-19 no Brasil com ML
# 1. Introdução
A pandemia de covid-19 foi muito avassaladora em termos humanitários. Especificamente, no Brasil, perdemos em torno de <b>660 mil pessoas</b>. O vírus foi uma surpresa absurdamente inesperada, fazendo com que houvesse uma certa demora na arquitetação de planos de combate ao Coronavírus e, assim, perdas inimagináveis até então se concretizaram.

<p align="center">

<img src = "https://img.freepik.com/vetores-gratis/fundo-branco-da-celula-do-virus-covid-19-surto-de-coronavirus-em-2019xdxa_186616-273.jpg" style="width:500px;margin-bottom:15px">
    
<p>    

No entanto, o mundo correu atrás das vacinas e hoje, graças à ciência, <b>os casos de covid-19 estão diminuindo cada vez mais</b>, o que gera esperança em um futuro melhor para a raça humana.

<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161409341-30b90a01-3a52-4c24-8a64-586cb923f275.png" width = 900 height = 460 >    

<p>    
    
Nesse sentido, como uma técnica de prevenção contra o Coranavírus, a <b>previsão de novos casos de covid-19 utilizando Machine Learning</b> se torna muito relevante, uma vez que permite os sistemas de saúde se adaptarem ao que virá.

# 2. Objetivos
O presente trabalho tem como um dos principais objetivos, realizar previsões de séries temporais para novos casos e mortes diárias no Brasil. Tal previsão será de 60 dias a partir da seguinte data: 2022/03/17.

# 3. Procedimentos
## 3.1 Conjunto de dados original
O conjunto de dados que foi utilizado aqui está disponível no site do <b>Kaggle</b>: https://www.kaggle.com/datasets/josephassaker/covid19-global-dataset

As colunas do conjunto são descritas abaixo:

* `date`: Data de observação
* `country` : País
* `cumulative_total_cases` : Total de casos (cumulativo)
*  `daily_new_cases` : Novos casos (diário)
*  `active_cases` : Casos ativos (casos confirmados que ainda não se recuperaram nem morreram) 
*  `cumulative_total_deaths` : Total de mortes (cumulativo)
*  `daily_new_deaths` : Novas mortes (diário)

## 3.2 Importação das bibliotecas

```bash
"""
1°) Importação do pandas como pd para trabalhar com dados.
"""
import pandas as pd
"""
2°) Importação do numpy como np para trabalhar com matrizes e tudo mais.
"""
import numpy as np
"""
3°) Importação do matplotlib.pyplot como plt para fazer gráficos.
"""
import matplotlib.pyplot as plt
"""
4°) De matplotlib.ticker vamos importar o AutoMinorLocator e o MaxNLocator para trabalhar com os "ticks"
    dos gráficos.
"""
import matplotlib.ticker as mticker
from matplotlib.ticker import AutoMinorLocator, MaxNLocator
"""
5°) De matplotlib.font_manager vamos importar FontProperties para criar fontes de texto.
"""
from matplotlib.font_manager import FontProperties
"""
6°) Importação do seaborn para fazer gráficos
"""
import seaborn as sbn
"""
7°) Importação de pycaret.time_series para trabalhar com séries temporais
"""
from pycaret.time_series import *
```

## 3.3 Importação dos dados
Como os nosso objetivos estavam ligados ao Brasil e o conjunto de dados original era global, primeiro foi feito um filtro com o comando <b>.loc</b> para pegar apenas os dados brasileiros.

```bash
Dados = pd.read_csv("worldometer_coronavirus_daily_data.csv")
"""
Filtrando para pegar apenas os dados do Brazil
"""
Brazil = Dados.loc[Dados["country"] == "Brazil"]
```

## 3.4 Pré processamento de dados

Como já sabemos que se trata de dados apenas no Brasil, não faz sentido manter a coluna "country".

```bash
Brazil.drop(["country"], axis = 1, inplace = True)
```

Agora, vamos transformar a data de object para datetime64[ns].

```bash
Brazil["date"] = pd.to_datetime(Brazil["date"])
```

Além disso, vamos filtrar mais ainda para que nossa contagem de tempo comece na data: 01/03/2020

```bash
Brazil = Brazil.loc[Brazil["date"] > pd.Timestamp("2020-2-29")]
```

### 3.4.1 Dados faltantes

Utilizando o comando a seguir, podemos verificar que não há dados faltantes no conjunto de dados.

```bash
Brazil.isnull().sum()/len(Brazil["date"])
```

### 3.4.2 Análise dos dados

Com base do dataset resultante, foram feitos vários gráficos a fim de analisar o comportamento dos dados.

#### Mapa de calor para a matriz de correlação entre as variáveis
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161410648-a55cbaf3-a51e-463a-a7fd-6866a1ebc548.png" width = 700 height = 500 >    

<p>      

* Correlação muito forte entre total de casos (cumulativo) e total de mortes (cumulativo)
* Correlação forte entre novos casos (diário) e casos ativos
* Correlação moderada entre novos casos (diário) e novas mortes (diário)

#### Relação total de casos (cumulativo) e total de mortes (cumulativo)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161410703-fa2c3115-c9a8-4c37-a40a-54f545cfc6eb.png" width = 650 height = 500 >    

<p>       

#### Novos casos (diário) e casos ativos
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161410802-15169b91-2328-4e56-982e-0ff44623a529.png" width = 650 height = 500 >    

<p>     

#### Novos casos (diário) e Novas mortes (diário)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161410821-4ff724a4-e211-4a38-b199-9d5746711c4b.png" width = 650 height = 500 >    

<p>      

Depois disso, começamos a analisar as variáveis individualmente.

#### Total de casos (cumulativo)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161410896-5700ec6b-a36b-42f1-bff1-b27d0ea47f16.png" width = 479 height = 360 >    
<img src = "https://user-images.githubusercontent.com/93550626/161410898-46fb72b6-024c-40c3-bf54-67c475364974.png" width = 650 height = 500 >     

<p>      
    
* Como a variável é cumulativa, esse gráfico é estritamente crescente.

#### Novos casos (diário)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161411011-537ca593-0c61-4e07-8dd5-36e2db0083c2.png" width = 479 height = 360 >    
<img src = "https://user-images.githubusercontent.com/93550626/161411015-28e7b811-b0e4-4bfd-a25e-726c1be441ed.png" width = 900 height = 460 >     

<p>    

* Graças ao avanço da vacinação no Brasil, o número de novos casos de covid-19 vem caindo...

#### Casos ativos
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161411034-c824c9dc-3d3b-4fcf-8c6f-db958b0227bc.png" width = 479 height = 360 >    
<img src = "https://user-images.githubusercontent.com/93550626/161411040-16b2cb15-1297-4abc-aef1-833374597649.png" width = 900 height = 460 >     

<p>      

#### Total de mortes (cumulativo)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161411045-d98c462b-1dcc-484d-9ccb-7cd8e082788d.png" width = 479 height = 360 >    
<img src = "https://user-images.githubusercontent.com/93550626/161411052-3688d71d-e2fc-4a36-8971-435d8d9e04c7.png" width = 650 height = 500 >     

<p>    

#### Novas mortes (diário)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161411056-764710ed-2f4c-411b-9b52-e3df2d3fd52e.png" width = 479 height = 360 >    
<img src = "https://user-images.githubusercontent.com/93550626/161411061-2c507b4f-c6a9-4e8c-b94c-b6575c54d18e.png" width = 900 height = 460 >     

<p>       

* Perdemos muitas pessoas e com certeza não queremos perder mais! Nesse caso, os dados estão caminhando ao nosso favor!

## 3.5 Preparação dos DataFrames para a aplicação do pycaret

Vamos criar 3 DFs, cada um uma coluna de data e uma variável (dentre três: Novos casos (diário), Casos ativos e Novas mortes (diário))

```bash
novos_casos_diarios = Brazil[["Data", "Novos casos (diário)"]]
casos_ativos = Brazil[["Data", "Casos ativos"]]
novas_mortes_diarias = Brazil[["Data", "Novas mortes (diário)"]]
```

Depois disso, precisamos fazer com que as datas em cada DF funcione como índices deles.

```bash
novos_casos_diarios.set_index("Data", drop = True, inplace = True)
casos_ativos.set_index("Data", drop = True, inplace = True)
novas_mortes_diarias.set_index("Data", drop = True, inplace = True)
```

Pronto, estamos prontos para a aplicação do pycaret a fim de realizar previsão de séries temporais. 

## 3.6 Como o pycaret é aplicado?
#### Exemplo para os novos casos diários

```bash
"""
Criando um setup
"""
setup(novos_casos_diarios, fh = 65, fold = 10, seasonal_period="D", n_jobs = -1, use_gpu = True)
"""
Comparação de modelos
"""
best_model = compare_models(exclude = "auto_arima")
"""
Finalização do modelo
"""
final = finalize_model(ets)
"""
Previsões do modelo
"""
pred = predict_model(final, fh = 60) # 60 dias de previsão
pred = pd.DataFrame(pred, columns = ["Data", "Novos casos (diário)"])
pred["Data"] = pred.index.to_timestamp()
pred = pred.loc[pred["Novos casos (diário)"] > 0]
```

Agora é só plotar as previsões!!!

# 4. Resultados

## 4.1 Novos casos (diário)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161411681-e7029bcd-24ec-49f7-b9a8-97ebb108122c.png" width = 900 height = 460 >     

<p>     

## 4.2 Casos ativos
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161411719-71153f78-778b-4176-9ee5-a9fb8e636b63.png" width = 900 height = 460 >     

<p>     

## 4.3 Novas mortes (diário)
    
<p align="center">    

<img src = "https://user-images.githubusercontent.com/93550626/161411729-1b651bd0-2e63-4478-9612-91c27b0bb5a4.png" width = 900 height = 460 >     

<p>     

# 5. Conclusão

Dessa forma, no gráfico da seção 4.1, observou-se que, os novos casos diários de covid-19 tendem a diminuir. Tal fato já era esperado por nós por conta do avanço da vacinação no Brasil. Além disso, o algorítmo propôs que haverá um certo aumento do número de casos ativos. Aumento esse que já pode deixar em alerta o SUS e os sistemas privados de saúde. Já em relação aos casos de morte diárias por covid-19, conseguiu-se perceber, pela figura da seção 4.3, uma oscilação em torno de um ponto de equilíbrio. Em um primeiro momento, isso parece estranho, pois esperamos que, com a vacinação, o número de mortes diminua. No entanto, <b>possivelmente</b>, essas oscilações estáveis vem sendo causadas por pessoas não vacinadas contra o Coronavírus. 

