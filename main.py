import matplotlib.pyplot as plt

def display_menu():


    menu = """
    A -> Carregar ficheiro
    B -> Estatisticas basicas (min, max, media)
    C -> Visualizar gráfico de dispersão
    D -> Visualizar histograma de um composto
    E -> Visualizar mapa dos tipos de granito
    F -> Visualizar percurso de amostragem efetuado
    T -> Terminar
    """

    print(menu)
    while True:
        choice = str(input("Escolha uma opção: ")).upper()
        if choice == 'A':
            #filename = str(input("Introduza o nome do ficheiro: "))
            dados = carregar_ficheiro('./geoq.csv')      
        elif choice == 'B':
            compostos_indices = {'SiO2':0, 'TiO2':1, 'Fe2O3':2, 'MgO':3}
            composto = input("Introduza o nome do composto: ")

            if composto not in compostos_indices:
                print("Composto inválido!")
            else:
                print("Estatisticas basicas selecionado!")
                estatisticas_basicas(dados[compostos_indices[composto]], composto)
           
        elif choice == 'C':
            print("Visualizar gráfico de dispersão")
        elif choice == 'D':
            print("Visualizar histograma de um composto")
        elif choice == 'E':
            print("Visualizar mapa dos tipos de granito")
        elif choice == 'F':
            print("Visualizar percurso de amostragem efetuado")
        elif choice == 'T':
            print("Terminar")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def carregar_ficheiro(filename):
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            print("Successfully opened the file '%s'!" % filename)

            dados = {}  # Dicionário que vai guardar a informação do ficheiro
                        # Neste dicionário, a chave são as coordenadas e o valor é uma lista com os valores dos químicos

            next(f)  # Skip tao cabeçalho

            for linha in f:
                linha = linha.strip()  # Remove leading/trailing whitespace and newline characters
                coordenadas = linha[:2]  # First two characters are coordinates
                valores = linha[2:]  # The rest of the line are chemical values
                dados[coordenadas] = valores

            print(dados)
    except FileNotFoundError:
        print('Ficheiro não encontrado!')
    except Exception as e:
        print('Um erro ocorreu!:', e)

    return dados

def estatisticas_basicas(lista_composto, composto):

    minimo = min(lista_composto)

    maximo = max(lista_composto)

    media = sum(lista_composto)/len(lista_composto)

    print('Valor mínimo de %s = %.4f%', composto,minimo)
    print('Valor máximo de %s = %.4f%', composto,maximo)
    print('Valor médio de %s = %.4f%', composto,media)


display_menu()
   