import csv
import os

def main():
    """"Cataloga as pastas de filmes por Título e Ano"""
    dir_filmes = '(diretorio_pasta_filmes)'

    # Busca o nome dos diretórios e os armazena na lista filmes
    filmes = os.listdir(dir_filmes)

    # Reordena os filmes em ordem alfabética
    filmes.sort(key=str.casefold)

    ano_filme = []
    titulo_filme = []

    # Armazena somente o ano de cada filme na lista ano_filme
    for ano in filmes:
        ano_filme.append(ano[-5:-1])

    # Armazena somente o título de cada filme na lista titulo_filme
    for titulo in filmes:
        titulo_filme.append(titulo[:-7])


    rows = zip(titulo_filme, ano_filme)

    # Em uma planilha csv, escreve cada item das listas em uma coluna separada
    dir_csv = '(diretorio_output_csv).csv'
    with open(dir_csv, 'w', encoding='UTF-8') as filmes_csv:
        writer = csv.writer(filmes_csv)
        for row in rows:
            writer.writerow(row)
        filmes_csv.close()


if __name__ == '__main__':
    main()
