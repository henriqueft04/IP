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
            filename = str(input("Introduza o nome do ficheiro: "))
            dados = carregar_ficheiro(filename)      
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
            print("Visualizar mapa dos tipos de granito selecionado!")
            dispersao_granito(dados)
        elif choice == 'F':
            print("Visualizar percurso de amostragem efetuado selecionado!")
            percurso_amostragem(dados)
        elif choice == 'H':
            print("Visualizar dados repetidos selecionado!")
            verificar_linhas_repetidas(filename)
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
                valores_filtrados = [x for x in valores if x != -99999.0]
                dados[coordenadas] = valores_filtrados

    except FileNotFoundError:
        print('Ficheiro não encontrado!')
        
        return None

    except Exception as e:
        print('Um erro ocorreu!:', e)

    print("Ficheiro '%s' carregado com sucesso!\n" % filename)
    return dados

def estatisticas_basicas(dados, composto):

    # Primeiro escolhemos o índice do composto que queremos, indo buscar ao dicionário compostos_indices
    # A função lambda recebe um valor x e retorna o valor x[compostos_indices[composto]]
    minimo = min(dados.values(), key=lambda x: x[compostos_indices[composto]])[compostos_indices[composto]]

    maximo = max(dados.values(), key=lambda x: x[compostos_indices[composto]])[compostos_indices[composto]]

    media = sum([x[compostos_indices[composto]] for x in dados.values()]) / len(dados)

    print('------------------------------------------------')
    print('Valor mínimo de %s = %.4f' % (composto, minimo))
    print('Valor máximo de %s = %.4f' % (composto, maximo))
    print('Valor médio de %s = %.4f' % (composto, media))
    print('------------------------------------------------')

def grafico_dispersao(dados, composto_x, composto_y):

    x = [x[compostos_indices[composto_x]] for x in dados.values()]
    y = [x[compostos_indices[composto_y]] for x in dados.values()]

    plt.scatter(x, y, s=7) # parametro s torna pontos mais finos
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

def dispersao_granito(dados):

    coord_x_tipo1 = []
    coord_y_tipo1 = []
    coord_x_tipo2 = []
    coord_y_tipo2 = []

    for key, value in dados.items():
        print(key, value)
        if len(value) == 4:
            if value[3] < 2:
                coord_x_tipo1.append(float(key[0]))
                coord_y_tipo1.append(float(key[1]))
            elif value[3] >= 2:
                coord_x_tipo2.append(float(key[0]))
                coord_y_tipo2.append(float(key[1]))

    # Criar o gráfico de dispersão
    plt.scatter(coord_x_tipo1, coord_y_tipo1, label='Granito de tipo I', color='blue')
    plt.scatter(coord_x_tipo2, coord_y_tipo2, label='Granito de tipo II', color='red')

    # Configurar labels e título do gráfico
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Mapa de amostragem')
    plt.legend()
    plt.show()
    
def percurso_amostragem(dados):
    
    # Se as coordenadas forem strings, converta-as em números
    coordenadas = [(float(x), float(y)) for x, y in dados.keys()]

    distancia_total = 0
    for i in range(1, len(coordenadas)):
        x1, y1 = coordenadas[i - 1]
        x2, y2 = coordenadas[i]
        distancia_total += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Plotar o percurso
    x, y = zip(*coordenadas)  # Separar as coordenadas em listas x e y
    plt.scatter(x, y) # Pontos
    plt.plot(x, y, linestyle='dashed')  # Linha que conecta os pontos

    # Adicionar marcador para o ponto inicial (primeiro elemento)
    plt.scatter(coordenadas[0][0],coordenadas[0][1] , label='Ponto Inicial',color='r', marker='<',zorder=3)

    # Adicionar marcador para o ponto final (último elemento)
    plt.scatter(coordenadas[-1][0],coordenadas[-1][1], label='Ponto Final', color='r', marker='s',zorder=3)

    # Configurar rótulos e título do gráfico
    plt.xlabel('X (Km)')
    plt.ylabel('Y (Km)')
    plt.title('Percurso de amostragem (distância percorrida: %.1f Km)' % distancia_total)
    plt.legend()

    # Exibir o gráfico
    plt.show()


def verificar_linhas_repetidas(filename):
    
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            # Encontrar linhas duplicadas

            linhas_vistas = set()
            linhas_unicas = []
            linhas_duplicadas = []

            for linha in linhas:
                if linha in linhas_vistas:
                    linhas_duplicadas.append(linha)
                else:
                    linhas_vistas.add(linha)
                    linhas_unicas.append(linha)
            
            if not linhas_duplicadas:
                print(f"O arquivo '{filename}' não possui linhas iguais.")
            else:
                print(f"Linhas duplicadas encontradas no arquivo '{filename}':")
                for linha in linhas_duplicadas:
                    print(linha.strip())
                
                # Perguntar ao utilizador se deseja remover as linhas duplicadas
                resposta = input("Deseja remover as linhas duplicadas? (S/N): ").strip().lower()
                if resposta == 's':
                    # Remover as linhas duplicadas
                    with open(filename, 'w', newline='', encoding='utf-8') as novo_arquivo:
                        novo_arquivo.writelines(linhas_unicas)
                    print("Linhas duplicadas removidas com sucesso.")
                else:
                    print("Linhas duplicadas não foram removidas.")

    except FileNotFoundError:
        print(f"O arquivo '{filename}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")


main()