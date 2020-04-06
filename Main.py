from Functions import codific
from LettersCode import listapalavra
from LettersCode import newpalavra
from time import sleep

while True:
    inicio = "c"
    if inicio[0] in "cd":
        sleep(0.5)
        print("-=" * 20)
        print("Digite FIM para sair.")
        print("Codificação ou Decodificação?", end=" ")
        inicio = str(input()).strip().lower()

        if inicio in "fim":
            sleep(0.3)
            print("Codificador desligado.")
            break
        if inicio[0] not in "cd":
            print("Erro entre escolher codificar e decodificar! Digite novamente.")
        sleep(0.5)

    sleep(0.1)
    print("-=" * 20)
    palavra = str(input("Palavra: (palavra sem acento) ")).strip().lower()

    for i in palavra:
        listapalavra.append(i)

    codific()

    if inicio[0] in "c":
        print("Palavra codificada:", end="  ")
    else:
        print("Palavra decodificada:", end="  ")
    for p in newpalavra:
        print(p, end="")
    listapalavra.clear()  # limpa todos valores da lista
    newpalavra.clear()
    print("\n")
    sleep(2)
