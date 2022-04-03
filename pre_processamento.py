#!/usr/bin/env python
# coding: utf-8

# # $\color{cyan}{\textbf{3. Pré-processsamento de dados}}$ 

# In[322]:


"""
Como já sabemos que se trata de dados apenas no Brasil, não faz sentido manter a coluna "country"
"""
Brazil.drop(["country"], axis = 1, inplace = True)
"""
Tranformação da data de object para datetime64[ns]
"""
Brazil["date"] = pd.to_datetime(Brazil["date"])
"""
Vamos filtrar mais ainda para que nossa contagem de tempo comece na data: 01/03/2020
"""
Brazil = Brazil.loc[Brazil["date"] > pd.Timestamp("2020-2-29")]


# # $\color{cyan}{\textbf{3.1. Dados missing}}$

# In[323]:


"""
Calcula as porcentagens de dados missing em cada coluna do DF
"""
Brazil.isnull().sum()/len(Brazil["date"])


# # $\color{cyan}{\textbf{3.2. Dtypes}}$

# In[324]:


Brazil.dtypes


# # $\color{cyan}{\textbf{3.3. Análise dos dados}}$

# In[325]:


Brazil.columns = ["Data", 
                  "Total de casos (cumulativo)", 
                  "Novos casos (diário)", 
                  "Casos ativos", 
                  "Total de mortes (cumulativo)",
                  "Novas mortes (diário)"]


# # $\rho = \frac{\textbf{Cov (x, y)}}{\sqrt{\textbf{Var(x)} \cdot \textbf{Var(y)}}}$

# In[326]:


"""
Vamos começar plotando um mapa de calor para avaliar o coeficiente de correlação de Pearson p entre as
variáveis.
"""
sbn.heatmap(Brazil.corr(), # Matriz de correlação
            vmin = -1, # p min
            vmax = 1, # p max
            annot = True, # Anotar p = True
            cmap = "YlGnBu", # Colormap
            linewidths =0.5, # width da linha de controno entre as células do mapa de calor
            linecolor="white", # cor de tais linhas
            annot_kws={"size": 13}) # size dos números no heatmap
"""
Mudando o size da fontedos labels
"""
sbn.set(font_scale=1.2)
"""
Tudo em negrito
"""
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
"""
Mostrar gráfico
"""
plt.show()


# $\color{cyan}{\textbf{$\bullet$ Correlação muito forte entre total de casos (cumulativo) e total de mortes (cumulativo)}}$
# $\color{cyan}{\textbf{$\bullet$ Correlação forte entre novos casos (diário) e casos ativos}}$
# $\color{cyan}{\textbf{$\bullet$ Correlação moderada entre novos casos (diário) e novas mortes (diário)}}$

# #  $\color{cyan}{\textbf{Casos (cumulativo) e mortes (cumulativo)}}$

# In[327]:


"""
Criação da primeira fonte de texto para colocar como fonte dos labels
"""
font1 = {"family": "serif", "weight": "bold", "color": "gray", "size": 14}
"""
Criação da segunda fonte de texto para colocar como fonte da legenda
"""
font2 = FontProperties(family = "serif",
                       weight = "bold",
                       size = 14)
"""
Cria um "lugar" com size (9, 7) para alocar a figura
"""
fig, axs = plt.subplots(figsize = (9, 7))
"""
Plota um scatter entre o total de casos (cumulativo) e total de mortes (cumulativo)
"""
axs.scatter(Brazil["Total de casos (cumulativo)"], 
            Brazil["Total de mortes (cumulativo)"], 
            color = "cyan",
            s = 10)
axs.grid(False)
"""
Definindo a "grossura" e a cor do eixos
"""
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
"""
Trabalha com os ticks do gráfico
"""    
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
"""
Números com notação científica
"""
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
"""
Descrição para cada eixo
"""
axs.set_xlabel("Total de casos (cumulativo)", fontdict = font1)
axs.set_ylabel("Total de mortes (cumulativo)", fontdict = font1)
"""
plt.rcParams["axes.labelweight"] = "bold" mostra em negrito os números nos eixos.
"""
plt.rcParams["axes.labelweight"] = "bold"
"""
Definindo um fundo branco para a imagem
"""
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
"""
Mostrar o gráfico
"""
plt.show()


# #  $\color{cyan}{\textbf{Novos casos (diário) e casos ativos}}$

# In[328]:


fig, axs = plt.subplots(figsize = (9, 7))
axs.scatter(Brazil["Novos casos (diário)"], 
            Brazil["Casos ativos"], 
            color = "cyan",
            s = 10)
axs.grid(False)
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xlabel("Novos casos (diário)", fontdict = font1)
axs.set_ylabel("Casos ativos", fontdict = font1)
plt.rcParams["axes.labelweight"] = "bold"
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# #  $\color{cyan}{\textbf{Novos casos (diário) e Novas mortes (diário)}}$

# In[329]:


fig, axs = plt.subplots(figsize = (9, 7))
axs.scatter(Brazil["Novos casos (diário)"], 
            Brazil["Novas mortes (diário)"], 
            color = "cyan",
            s = 10)
axs.grid(False)
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xlabel("Novos casos (diário)", fontdict = font1)
axs.set_ylabel("Novas mortes (diário)", fontdict = font1)
plt.rcParams["axes.labelweight"] = "bold"
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# #  $\color{cyan}{\textbf{Total de casos (cumulativo)}}$

# In[330]:


"""
Plot de um gráfico violino
"""
sbn.violinplot(data = Brazil, y = "Total de casos (cumulativo)", palette = ["cyan"])
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = False, bottom = False, top = False, right = False)
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("gray")
Cor_fundo.patch.set_alpha(0.1)
plt.ylabel("Total de casos (cumulativo)", fontdict = font1)
plt.show()


# In[331]:


fig, axs = plt.subplots(figsize = (9, 7))
axs.plot(Brazil["Data"], 
            Brazil["Total de casos (cumulativo)"], 
            color = "cyan",
            linewidth = 2.4)
axs.grid(False)
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = False, top = False, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xlabel("Data", fontdict = font1)
axs.set_ylabel("Total de casos de Covid-19 (cumulativo)", fontdict = font1)
plt.rcParams["axes.labelweight"] = "bold"
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# $\color{cyan}{\textbf{$\bullet$ Como a variável é cumulativa, esse gráfico é estritamente crescente.}}$

# # $\color{cyan}{\textbf{Novos casos (diário)}}$

# In[332]:


sbn.violinplot(data = Brazil, y = "Novos casos (diário)", palette = ["cyan"])
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = False, bottom = False, top = False, right = False)
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("gray")
Cor_fundo.patch.set_alpha(0.1)
plt.ylabel("Novos casos (diário)", fontdict = font1)
plt.show()


# In[333]:


fig, axs = plt.subplots(figsize = (14, 7))
axs.plot(Brazil["Data"], 
            Brazil["Novos casos (diário)"], 
            color = "cyan",
            linewidth = 1.1)
axs.grid(False)
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = False, top = False, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xlabel("Data", fontdict = font1)
axs.set_ylabel("Novos casos (diário)", fontdict = font1)
plt.rcParams["axes.labelweight"] = "bold"
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# $\color{cyan}{\textbf{$\bullet$ Graças ao avanço da vacinação no Brasil, o número de novos casos de covid-19 vem caindo...}}$

# # $\color{cyan}{\textbf{Casos ativos}}$

# In[334]:


sbn.violinplot(data = Brazil, y = "Casos ativos", palette = ["cyan"])
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = False, bottom = False, top = False, right = False)
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("gray")
Cor_fundo.patch.set_alpha(0.1)
plt.ylabel("Casos ativos", fontdict = font1)
plt.show()


# In[335]:


fig, axs = plt.subplots(figsize = (14, 7))
axs.plot(Brazil["Data"], 
            Brazil["Casos ativos"], 
            color = "cyan",
            linewidth = 1.5)
axs.grid(False)
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = False, top = False, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xlabel("Data", fontdict = font1)
axs.set_ylabel("Casos ativos", fontdict = font1)
plt.rcParams["axes.labelweight"] = "bold"
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# $\color{cyan}{\textbf{$\bullet$ O número de casos ativos também vem diminuindo, o que é uma benção!}}$

# # $\color{cyan}{\textbf{Total de mortes (cumulativo)}}$

# In[336]:


sbn.violinplot(data = Brazil, y = "Total de mortes (cumulativo)", palette = ["cyan"])
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = False, bottom = False, top = False, right = False)
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("gray")
Cor_fundo.patch.set_alpha(0.1)
plt.ylabel("Total de mortes (cumulativo)", fontdict = font1)
plt.show()


# In[337]:


fig, axs = plt.subplots(figsize = (9, 7))
axs.plot(Brazil["Data"], 
            Brazil["Total de mortes (cumulativo)"], 
            color = "cyan",
            linewidth = 1.5)
axs.grid(False)
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = False, top = False, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xlabel("Data", fontdict = font1)
axs.set_ylabel("Total de mortes (cumulativo)", fontdict = font1)
plt.rcParams["axes.labelweight"] = "bold"
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# $\color{cyan}{\textbf{$\bullet$ Novamente, como a variável é cumulativa, esse gráfico é estritamente crescente.}}$

# # $\color{cyan}{\textbf{Novas mortes (diário)}}$

# In[338]:


sbn.violinplot(data = Brazil, y = "Novas mortes (diário)", palette = ["cyan"])
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = False, bottom = False, top = False, right = False)
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("gray")
Cor_fundo.patch.set_alpha(0.1)
plt.ylabel("Novas mortes (diário)", fontdict = font1)
plt.show()


# In[339]:


fig, axs = plt.subplots(figsize = (14, 7))
axs.plot(Brazil["Data"], 
            Brazil["Novas mortes (diário)"], 
            color = "cyan",
            linewidth = 1.1)
axs.grid(False)
for axis in ["left", "right", "top", "bottom"]:
    axs.spines[axis].set_linewidth(2)
    axs.spines[axis].set_color("gray")
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())
axs.tick_params(axis = "both", direction = "in", labelcolor = "gray", labelsize = 14, left = True, bottom = True, top = True, right = True)
axs.tick_params(which = "major", direction = "in", color = "gray", length = 5.4, width = 2.5, left = True, bottom = False, top = False, right = True)
axs.tick_params(which = "minor", direction = "in", color = "gray", length=4, width = 2, left = True, bottom = True, top = True, right = True)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
axs.set_xlabel("Data", fontdict = font1)
axs.set_ylabel("Novas mortes (diário)", fontdict = font1)
plt.rcParams["axes.labelweight"] = "bold"
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# $\color{cyan}{\textbf{$\bullet$ Perdemos muitas pessoas e com certeza não queremos perder mais! Nesse caso, os dados estão}}$
# $\color{cyan}{\textbf{caminhando ao nosso favor!}}$
