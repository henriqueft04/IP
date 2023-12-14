import csv

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
        choice = input("Escolha uma opção: ").upper()
        if choice == 'A':
            filename = input("Introduza o nome do ficheiro: ")
            dados = carregar_ficheiro(filename)      
        elif choice == 'B':
            composto = input("Introduza o nome do composto: ")
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
    print("Carregar ficheiro %s selecionado!", filename)

    dados = {} # Dicionário que vai guardar a informação do ficheiro
               # Neste dicionário, a chave são as coordenadas e o valor é uma lista com os valores dos químicos

    with open(filename, 'r',newline='', encoding='utf-8') as f:
        leitor = csv.reader(f)
        
        header = next(leitor) # Passar à frente o cabeçalho

        for linha in leitor:
            
            #tirar as coordenadas
            coordenadas = float(linha[0],float(linha[1]))

            #guardas os químicos até MgO
            quimicos = [float(linha[i]) for i in range(2,5)]

            #cuidado extra com MgO
            if float(linha[6]) == -99999:
                continue
            else:
                quimicos.append(float(linha[6]))

            dados[coordenadas] = quimicos

    print('Ficheiro carregado com sucesso!')

    return dados

def estatisticas_basicas(dados, composto):
    print("Estatisticas basicas selecionado!")

    compostos_indices = {'SiO2':0, 'TiO2':1, 'Al2O3':2, 'Fe2O3':3, 'MgO':4}

    # Verificar se o composto existe
    if composto not in compostos_indices:
        print("Composto inválido!")
        return
    
    #cal
