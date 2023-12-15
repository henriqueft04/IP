import matplotlib.pyplot as plt

compostos_indices = {'SiO2':0, 'Fe2O3':1, 'CaO':2, 'MgO':3}

def main():


    menu = """
-------------------------------------------------- 
A -> Carregar ficheiro 
B -> Estatísticas básicas (min, max, media) 
C -> Visualizar gráfico de dispersão 
D -> Visualizar histograma de um composto 
E -> Visualizar mapa dos tipos de granito 
F -> Visualizar percurso de amostragem efetuado 
T -> Terminar 
-------------------------------------------------- 
    """

    print(menu)
    while True:
        choice = str(input("Escolha uma opção: ")).upper()
        if choice == 'A':
            print("Carregar ficheiro selecionado!")
            #filename = str(input("Introduza o nome do ficheiro: "))
            dados = carregar_ficheiro('./geoq.csv')      
        elif choice == 'B':
            composto = str(input("Introduza o nome do composto: "))

            if composto not in compostos_indices.keys():
                print("Composto inválido!")
            else:
                print("Estatisticas basicas selecionado!")
                estatisticas_basicas(dados, composto)
           
        elif choice == 'C':
            print("Visualizar gráfico de dispersão selecionado!")
            composto_x = str('')
            while composto_x not in compostos_indices.keys():
                composto_x = str(input("Introduza o nome do composto para o eixo dos x: "))
                if composto_x not in compostos_indices.keys():
                    print("Composto inválido!")
                else:
                    composto_y = str('')
                    while composto_y not in compostos_indices.keys():
                        composto_y = str(input("Introduza o nome do composto para o eixo dos y: "))
                        if composto_y not in compostos_indices.keys():
                            print("Composto inválido!")
                        else:
                            grafico_dispersao(dados, composto_x, composto_y)
        elif choice == 'D':
            print("Visualizar histograma de um composto selecionado!")

            composto_x = str('')
            while composto_x not in compostos_indices.keys():
                composto_x = str(input("Introduza o nome do composto: "))
                if composto_x not in compostos_indices.keys():
                    print("Composto inválido!")
                else:
                    n_classes = int(input("Introduza o número de classes: "))
                    histograma(dados, composto_x, n_classes) 
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

            dados = {}  # Dicionário que vai guardar a informação do ficheiro
                        # Neste dicionário, a chave são as coordenadas e o valor é uma lista com os valores dos químicos

            next(f)  # Skip tao cabeçalho

            for linha in f:
                linha = linha.strip().split('\t')  # Cria uma lista com os valores da linha
                coordenadas = tuple(linha[:2])  # Os primeiros dois valores são as coordenadas
                valores = linha[2:]  # O resto dos valores são os valores dos químicos
                valores = [float(valor) for valor in valores]
                valores_filtrados = [x for x in valores if x != -9999]
                dados[coordenadas] = valores_filtrados

    except FileNotFoundError:
        print('Ficheiro não encontrado!')
    except Exception as e:
        print('Um erro ocorreu!:', e)

    print("Ficheiro '%s' carregado com sucesso!" % filename)
    return dados

def estatisticas_basicas(dados, composto):

    # Primeiro escolhemos o índice do composto que queremos, indo buscar ao dicionário compostos_indices
    # A função lambda recebe um valor x e retorna o valor x[compostos_indices[composto]]
    minimo = min(dados.values(), key=lambda x: x[compostos_indices[composto]])[compostos_indices[composto]]

    maximo = max(dados.values(), key=lambda x: x[compostos_indices[composto]])[compostos_indices[composto]]

    media = sum([x[compostos_indices[composto]] for x in dados.values()]) / len(dados)

    print('Valor mínimo de %s = %.4f' % (composto, minimo))
    print('Valor máximo de %s = %.4f' % (composto, maximo))
    print('Valor médio de %s = %.4f' % (composto, media))


def grafico_dispersao(dados, composto_x, composto_y):

    x = [x[compostos_indices[composto_x]] for x in dados.values()]
    y = [x[compostos_indices[composto_y]] for x in dados.values()]

    plt.scatter(x, y)
    plt.xlabel(composto_x + '(%)')
    plt.ylabel(composto_y + '(%)')
    plt.title('Gráfico de dispersão')
    plt.show()

def histograma(dados, composto, n_classes):

    valores = [x[compostos_indices[composto]] for x in dados.values()]

    plt.hist(valores, bins=n_classes)
    plt.xlabel(composto + ' (%)')
    plt.ylabel('Frequência absoluta')
    plt.title('Histograma do composto %s (%%) (%d classes)' % (composto, n_classes))
    plt.show()


main()
def histograma(dados, composto, n_classes):
    valores = [x[compostos_indices[composto]] for x in dados.values()]

    plt.hist(valores, bins=n_classes)
    plt.xlabel(composto + ' (%)')
    plt.ylabel('Frequência absoluta')
    plt.title(f'Histograma do composto {composto} (%) ({n_classes} classes)')
    plt.show()