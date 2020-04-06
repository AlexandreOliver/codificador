from LettersCode import listapalavra
from LettersCode import newpalavra
from LettersCode import codificar
from Main import inicio


def codific():
    for ind in listapalavra:  # para cada índice na lista:
        if ind in codificar.keys():  # se esse indice estiver nas chaves do dict codificar
            newpalavra.append(codificar[ind])  # adiciona o valor dessa chave em uma nova lista
        elif ind in " ":  # se tiver um espaço
            newpalavra.append(ind)  # adiciona


def resultado():
    if inicio[0] in "c":
        print("Palavra codificada:", end="  ")
    else:
        print("Palavra decodificada:", end="  ")
    for p in newpalavra:
        print(p, end="")
    listapalavra.clear()  # limpa todos valores da lista
    newpalavra.clear()
    print("\n")
