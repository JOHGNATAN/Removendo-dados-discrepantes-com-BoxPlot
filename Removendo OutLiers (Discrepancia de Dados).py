#!/usr/bin/env python
# coding: utf-8

# # Identificando e Removendo Outliers

get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))



dados= pd.read_csv("C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/aluguel.csv", sep = ';')

dados.boxplot(['Valor'])

valor = dados['Valor']
valor

Q1 = valor.quantile(.25)
Q3 = valor.quantile(.75)

IIQ = Q3 - Q1

limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ


#CRIANDO UM DATAFRAME REMOVENDO OS OUTLIERS

selecao = (valor >= limite_inferior) & (valor <= limite_superior)
dados_new = dados[selecao]

dados_new.boxplot(['Valor'])


# ### Histograma antes da remoção dos dados divergentes 

dados.hist(['Valor'])


# ###  Depois da remoção dos dados divergentes, teremos uma distribuição de barras de forma organizada

dados_new.hist(['Valor'])

# # Identificando e Removendo Outliers por Grupo


dados= pd.read_csv('C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/aluguel_amostra.csv', sep = ';')
dados

dados.boxplot(['Valor'], by = ['Tipo'])


grupo_tipo = dados.groupby('Tipo')['Valor']
type(grupo_tipo)

grupo_tipo.groups

Q1 = grupo_tipo.quantile(.25)
Q3 = grupo_tipo.quantile(.75)

IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ


dados_new = pd.DataFrame()

for tipo in grupo_tipo.groups.keys():
    eh_tipo = dados['Tipo'] == tipo
    
    eh_dentro_limite = (dados['Valor'] >= limite_inferior[tipo]) & (dados['Valor'] <= limite_superior[tipo])
    
    selecao = eh_tipo & eh_dentro_limite
    
    dados_select = dados[selecao]
    
    dados_new = pd.concat([dados_new, dados_select])
    
dados_new.boxplot(['Valor'], by = ['Tipo'])


# # Mais sobre Gráficos

get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15,8))


dados = pd.read_csv("C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/extras/aluguel.csv", sep = ';')

dados.head()

area = plt.figure()

g1 = area.add_subplot(2,2,1)
g2 = area.add_subplot(2,2,2)
g3 = area.add_subplot(2,2,3)
g4 = area.add_subplot(2,2,4)


g1.scatter(dados['Valor'], dados.Area)
g1.set_title('Valor X Área')


g2.hist(dados.Valor)
g2.set_title('Histograma')


dados_g3 = dados.Valor.sample(100)
dados_g3.index = range(dados_g3.shape[0])
g3.plot(dados_g3)
g3.set_title('Amostra de valores')

grupo = dados.groupby('Tipo')['Valor']
label = grupo.mean().index
valores = grupo.mean().values

g4.bar(label, valores)
g4.set_title('Valor médio por Tipo')

# Ao executarmos nosso código teremos quatro tipos diferentes de gráficos na mesma área, 
# sendo o primeiro um gráfico de dispersão, o segundo um histograma, o terceiro uma amostra da variável Valor, 
# e por fim o tradicional gráfico em barras que representa o valor médio por tipos de imóvel.

area

#SALVANDO FIGURA

area.savefig('grafico.png', dpi = 300, bbox_inches = 'tight')

