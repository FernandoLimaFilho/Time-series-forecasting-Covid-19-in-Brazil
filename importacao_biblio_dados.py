#!/usr/bin/env python
# coding: utf-8

# # $\color{cyan}{\textbf{Time series forecasting; Covid 19 in Brazil}}$ 

# # $\color{cyan}{\textbf{1. Importação das bibliotecas}}$ 

# In[320]:


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


# # $\color{cyan}{\textbf{2. Trazendo os dados para o python}}$ 

# In[321]:


Dados = pd.read_csv("worldometer_coronavirus_daily_data.csv")
"""
Filtrando para pegar apenas os dados do Brazil
"""
Brazil = Dados.loc[Dados["country"] == "Brazil"]
Brazil.head()

