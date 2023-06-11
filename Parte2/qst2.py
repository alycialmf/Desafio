import matplotlib.pyplot as plt

arquivo = open('Parte2/CrashData.csv', 'r')

age_group = ['0_to_16', '17_to_25', '26_to_39', '40_to_64', '65_to_74', '75_or_older']

crash_type = ['Single', 'Multiple']

numero_pessoas_por_type = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

dados = arquivo.readline().split(',')
numero_linhas_arquivo = arquivo.read().count('\n')

arquivo.seek(0)
arquivo.readline()

for i in range(numero_linhas_arquivo):
    dados_linha = arquivo.readline().split(',')

    try:
        grupo = age_group.index(dados_linha[dados.index('Age Group')])
    except Exception as e:
        continue

    if dados_linha[dados.index('Crash Type')] == crash_type[0]:
        numero_pessoas_por_type[grupo][0] += 1    
    else:
        numero_pessoas_por_type[grupo][1] += 1

categorias = crash_type
cores = ['blue', 'orange']
num_linhas = 2
num_colunas = 3

fig, axes = plt.subplots(num_linhas, num_colunas, figsize = (10, 6))

fig.suptitle('Representatividade dos grupos etários por tipo de acidente na Austrália (1989-2021)', fontsize = 14, fontweight = 'bold')

for i, sublista in enumerate(numero_pessoas_por_type):
    row = i // num_colunas
    col = i % num_colunas

    ax = axes[row, col]
    ax.pie(sublista, labels = categorias, colors = cores, autopct = '%1.1f%%')

    grupo = age_group[i].split('_')
    ax.set_title(f'Grupo de {grupo[0]} - {grupo[2]} anos')

plt.tight_layout()

plt.show()

arquivo.close()