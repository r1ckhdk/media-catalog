import csv
import os

dir_filmes = '(diretorio_pasta_filmes)'

# Busca o nome dos diretórios e os armazena na lista filmes
filmes = os.listdir(dir_filmes)

# Reordena os filmes em ordem alfabética
filmes.sort(key=str.casefold)

ano_filme = []
titulo_filme = []

# Armazena somente o ano de cada filme na lista ano_filme
for a in filmes:
    ano_filme.append(a[-5:-1])

# Armazena somente o título de cada filme na lista titulo_filme
for t in filmes:
    titulo_filme.append(t[:-7])


rows = zip(titulo_filme, ano_filme)

# Em uma planilha csv, escreve cada item das listas em uma coluna separada
dir_csv = '(diretorio_output_csv).csv'
with open(dir_csv, 'w', encoding='UTF-8') as filmes_csv:
    writer = csv.writer(filmes_csv)
    for row in rows:
        writer.writerow(row)
    filmes_csv.close()