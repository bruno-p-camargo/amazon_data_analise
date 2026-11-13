# %% Configurações do pandas para exibir todas as colunas, ajustar a largura de exibição e formatar os números de ponto flutuante com duas casas decimais.

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.float_format", "{:.2f}".format)

# %% Carregamento e verificação do dataset
CAMINHO = "data/amazon.csv"

df = pd.read_csv(CAMINHO)

print("Dataset carregado com sucesso!")

# %% Inspeção Inicial
print("Dimensões (L , C):", df.shape)
print("\nColunas do dataset:", df.columns.tolist())
print("\nPrimeiras linhas do dataset:\n", df.head())
print("\nTipos e nulos por coluna:\n", df.info())
print("\nResumo estatístico das colunas numéricas:\n", df.describe())

# %%
