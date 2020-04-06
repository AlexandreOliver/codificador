from LettersCode import listapalavra
from LettersCode import newpalavra
from LettersCode import codificar


def codific():
    for ind in listapalavra:  # para cada índice na lista:
        if ind in codificar.keys():  # se esse indice estiver nas chaves do dict codificar
            newpalavra.append(codificar[ind])  # adiciona o valor dessa chave em uma nova lista
        elif ind in " ":  # se tiver um espaço
            newpalavra.append(ind)  # adiciona
