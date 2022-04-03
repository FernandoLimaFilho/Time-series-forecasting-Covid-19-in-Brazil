#!/usr/bin/env python
# coding: utf-8

# # $\color{cyan}{\textbf{4. Previsão de novos casos e mortes por covid-19 }}$

# In[340]:


novos_casos_diarios = Brazil[["Data", "Novos casos (diário)"]]
casos_ativos = Brazil[["Data", "Casos ativos"]]
novas_mortes_diarias = Brazil[["Data", "Novas mortes (diário)"]]
novas_mortes_diarias.head()


# In[341]:


"""
Transformando a data em índices
"""
novos_casos_diarios.set_index("Data", drop = True, inplace = True)
casos_ativos.set_index("Data", drop = True, inplace = True)
novas_mortes_diarias.set_index("Data", drop = True, inplace = True)


# # $\color{cyan}{\textbf{Previsão de novos casos diários}}$

# In[342]:


setup(novos_casos_diarios, fh = 65, fold = 10, seasonal_period="D", n_jobs = -1, use_gpu = True) # Criando um setup


# In[343]:


best_model = compare_models(exclude = "auto_arima") # Comparar modelos


# In[344]:


ets = create_model("ets") # Criar o melhor modelo


# In[345]:


final = finalize_model(ets) # finalizar o modelo
final


# In[346]:


pred = predict_model(final, fh = 60) # 60 dias de previsão
pred = pd.DataFrame(pred, columns = ["Data", "Novos casos (diário)"])
pred["Data"] = pred.index.to_timestamp()
pred = pred.loc[pred["Novos casos (diário)"] > 0]
pred


# In[347]:


fig, axs = plt.subplots(figsize = (14, 7))
axs.plot(Brazil["Data"], 
        Brazil["Novos casos (diário)"], 
        color = "cyan",
        linewidth = 1.5,
        label = "Dados originais (2020-03-01 até 2022-03-17)")
axs.plot(pred["Data"],
         pred["Novos casos (diário)"],
         color = "blue",
         linewidth = 1.5,
         label = "Previsão (2022-03-18 até 2022-05-14)")
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
plt.legend(frameon = False, prop = font2, labelcolor = "gray")
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# $\color{cyan}{\textbf{Muito bom! A previsão é que o número de casos (diário) diminua, como esperávamos.}}$

# # $\color{cyan}{\textbf{Casos ativos}}$

# In[348]:


setup(casos_ativos, fh = 60, fold = 10, seasonal_period="D", n_jobs=-1, use_gpu=True)


# In[349]:


best_model = compare_models(exclude = "auto_arima")


# In[350]:


omp_cds_dt = create_model("omp_cds_dt")


# In[351]:


final2 = finalize_model(omp_cds_dt)
final2


# In[352]:


pred2 = predict_model(final2, fh = 60)
pred2 = pd.DataFrame(pred2, columns = ["Data", "Casos ativos"])
pred2["Data"] = pred2.index.to_timestamp()
pred2 = pred2.loc[pred2["Casos ativos"] > 0]


# In[353]:


fig, axs = plt.subplots(figsize = (14, 7))
axs.plot(Brazil["Data"], 
            Brazil["Casos ativos"], 
            color = "cyan",
            linewidth = 1.5, label = "Dados originais (2020-03-01 até 2022-03-17)")
axs.plot(pred2["Data"],
         pred2["Casos ativos"],
         color = "blue",
         linewidth = 1.5,
         label = "Previsão (2022-03-18 até 2022-05-14)")
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
plt.legend(frameon = False, prop = font2, labelcolor = "gray")
fig.patch.set_facecolor("white")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()


# $\color{cyan}{\textbf{O número de casos ativos aumentou!}}$

# # $\color{cyan}{\textbf{Novas mortes (diário)}}$

# In[354]:


setup(novas_mortes_diarias, fh = 60, fold = 10, seasonal_period="D", n_jobs=-1, use_gpu=True)


# In[355]:


best_model = compare_models(exclude = "auto_arima")


# In[356]:


snaive = create_model("snaive")
final3 = finalize_model(snaive)
final3


# In[357]:


pred3 = predict_model(final3, fh = 60)
pred3 = pd.DataFrame(pred3, columns = ["Data", "Novas mortes (diário)"])
pred3["Data"] = pred3.index.to_timestamp()
pred3 = pred3.loc[pred3["Novas mortes (diário)"] > 0]


# In[358]:


fig, axs = plt.subplots(figsize = (14, 7))
axs.plot(Brazil["Data"], 
            Brazil["Novas mortes (diário)"], 
            color = "cyan",
            linewidth = 1.5, label = "Originais (2020-03-01 até 2022-03-17)")
axs.plot(pred3["Data"],
         pred3["Novas mortes (diário)"],
         color = "blue",
         linewidth = 1.5,
         label = "Previsão (2022-03-18 até 2022-05-14)")
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
plt.legend(frameon = False, prop = font2, labelcolor = "gray")
Cor_fundo = plt.gca()
Cor_fundo.set_facecolor("white")
Cor_fundo.patch.set_alpha(1)
plt.show()

