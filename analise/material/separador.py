import re

LISTA_TESTE = []
DATA_SET = []
list_labelled = []
# crio uma lista de listas usando os arquivos txt e cortando ele por linha,
# cada lista possui 1000 linhas
listas = [
        [a.rstrip() for a in open("analise/material/amazon_cells_labelled.txt")],
        [a.rstrip() for a in open("analise/material/imdb_labelled.txt")],
        [a.rstrip() for a in open("analise/material/yelp_labelled.txt")]
        ]

# para cada lista em listas
for m in listas:
    # pego linha por linha
    for l in range(len(m)):
        # e adiciono em list_labelled
        # até que list_labelled possua 3000 linhas
        list_labelled.append(m[l])

# para cada indice em list_labelled
for i in range(len(list_labelled)):
    # todos aqueles em que o resto de divisão por 10 for 0, ou seja 10%
    if i % 10 == 0:
        # eu adiciono la lista de testes LISTA_TESTE
        LISTA_TESTE.append(list_labelled[i])
    # os outros 90%
    else:
        # adiciono la lista de aprendizado DATA_SET
        DATA_SET.append(list_labelled[i])


def separador(opt):
    """
    Método que separa frases de labels criando duas listas e relacionando as
    informações pelo indice.
    """
    text = []
    label = []
    # para cada linha na lista que contém as frases e os labels
    for i in opt:
        # separo esta linha pelo tab em duas partes
        x = re.split(r'\t+', i)
        # a primeira parte é a frase, adiciono ela na lista text
        text.append(x[0])
        # a segunda parte é o label, adiciono ela na lista label
        label.append(x[1])
        # ou seja, com indices correspondentes
    return text, label
