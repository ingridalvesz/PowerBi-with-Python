# 'dataset' tem os dados de entrada para este script

dataset["Estado"] = dataset["Estado"].str.upper()

dataset["Saldos_Gols"] = dataset["Gols_Pro"] - dataset["Gols_Contra"]

dataset["Aprov_%"] =100 * dataset["Pontos"] / (dataset["Jogos"] * 30)
dataset["Aprov_%"] = dataset["Aprov_%"].round(2)