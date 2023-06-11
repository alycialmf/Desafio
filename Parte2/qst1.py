import matplotlib.pyplot as plt

arquivo = open('Parte2/CrashData.csv', 'r')

qnt_masculino, qnt_feminino = 0 , 0
idade_masculino, idade_feminino = 0 , 0
media_masculino, media_feminino, media_total = 0 , 0 , 0

dados = arquivo.readline().split(',')

while(True):
    dados_linha = arquivo.readline().split(',')

    if(not dados_linha[dados.index('Year')] == '2021'):
        break

    if(dados_linha[dados.index('Gender')] == 'Male'):
        qnt_masculino += 1
        idade_masculino += float(dados_linha[dados.index('Age')])
    else:
        qnt_feminino += 1
        idade_feminino += float(dados_linha[dados.index('Age')])

media_feminino =  idade_feminino/qnt_feminino
media_masculino = idade_masculino/qnt_masculino
media_total = (idade_feminino+ idade_masculino)/(qnt_feminino + qnt_masculino)

categorias = ['Masculino',  'Total' , 'Feminino']
medias_idades = [media_masculino , media_total , media_feminino]
cores = ['blue', 'yellow', 'pink']

plt.title('Média da idade em acidentes de trânsito na Austrália por gênero (2021)', fontsize = 10.5, fontweight = 'bold')

plt.bar(categorias, medias_idades, width = 0.5, color = cores)

plt.xlabel('Gênero')
plt.ylabel('Média da Idade')

plt.ylim(0, max(medias_idades) + 20)

for i, valor in enumerate(medias_idades):
    plt.text(i, valor + 0.5, f'{valor:.2f}', ha='center')

plt.show()

arquivo.close()