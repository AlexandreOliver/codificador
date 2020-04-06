from letras import codificar
from letras import decodificar
from letras import listapalavra
from letras import newpalavra
from time import sleep


def resultado():
    if inicio[0] in "c":
        print("Palavra codificada:", end="  ")
    else:
        print("Palavra decodificada:", end="  ")
    for p in newpalavra:
        print(p, end="")
    listapalavra.clear()    #limpa todos valores da lista
    newpalavra.clear()
    print("\n")


def codific():
    for ind in listapalavra:  # para cada índice na lista:
        if ind in codificar.keys():  # se esse indice estiver nas chaves do dict codificar
            newpalavra.append(codificar[ind])  # adiciona o valor dessa chave em uma nova lista
        elif ind in " ":    # se tiver um espaço
            newpalavra.append(ind)  # adiciona
    sleep(1)


def decodific():
    for ind in listapalavra:
        if ind in decodificar.keys():
            newpalavra.append(decodificar[ind])
        elif ind in " ":
            newpalavra.append(ind)
    sleep(1)


while True:
    sleep(1)
    print("-=" * 20)
    print("Digite FIM para sair.")
    print("Quer codificar ou decodificar?", end=" ")
    inicio = str(input()).strip().lower()

    if inicio in "fim":
        sleep(0.3)
        print("Codificador desligado.")
        break

    sleep(0.3)
    print("-=" * 20)
    palavra = str(input("Palavra: (palavra sem acento) ")).strip().lower()

    for i in palavra:
        listapalavra.append(i)

    if inicio[0] in "c":
        codific()
        resultado()

    elif inicio[0] in "d":
        decodific()
        resultado()
    else:
        print("Erro entre escolher codificar e decodificar! Digite novamente.")
        sleep(0.5)
