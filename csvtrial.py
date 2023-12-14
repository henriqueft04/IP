import csv

# Abra o arquivo CSV em modo de leitura
with open('./geoq.csv', 'r') as arquivo_csv:
    # Crie um objeto leitor CSV
    leitor_csv = csv.reader(arquivo_csv)

    # Itere pelas linhas do arquivo CSV
    for linha in leitor_csv:
        # Cada linha será uma lista de valores separados por vírgulas
        # Faça o que quiser com os valores, por exemplo, imprima-os
        print(linha)
