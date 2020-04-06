from Functions import codific
from Functions import resultado
from LettersCode import listapalavra
from time import sleep

while True:
    sleep(0.5)
    print("-=" * 20)
    print("Digite FIM para sair.")
    print("Codificação ou Decodificação?", end=" ")
    inicio = str(input()).strip().lower()

    if inicio in "fim":
        sleep(0.3)
        print("Codificador desligado.")
        break
    elif inicio not in "cd":
        print("Erro entre escolher codificar e decodificar! Digite novamente.")
        sleep(0.5)

    sleep(0.1)
    print("-=" * 20)
    palavra = str(input("Palavra: (palavra sem acento) ")).strip().lower()

    for i in palavra:
        listapalavra.append(i)

    codific()
    resultado()
