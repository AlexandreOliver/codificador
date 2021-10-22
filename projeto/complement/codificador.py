from complement.combination import *

def codific():
    for ind in listapalavra:  # para cada índice na lista:
        if ind in codificar.keys():  # se esse indice estiver nas chaves do dict codificar
            newpalavra.append(codificar[ind])  # adiciona o valor dessa chave em uma nova lista
        elif ind in " ,.:´~^`;!?@#$%&*(){}[]<>_-+=''/°":
            newpalavra.append(ind)  # add
        elif ind in '1234567890¹²³""':
            newpalavra.append(ind)  # add
