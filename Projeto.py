import random

lista_palavras = ["python", "java", "swift", "javascript"]

print("Palavra Achada\n")

palavra_escondida = random.choice(lista_palavras)
letras_ocultas = "-" * (len(palavra_escondida))
letras_ocultas_lista = list(letras_ocultas)
attempts = 8

print(letras_ocultas)

while(attempts > 0):
    resposta = input("Input a letter: ")
    indice = 0
    if resposta in palavra_escondida:
        for letra in palavra_escondida:
            if resposta == letra:
                letras_ocultas = letras_ocultas[:indice] + resposta + letras_ocultas[indice + 1:]
            indice += 1
    else:
        print("That letter doesn't appear in the word.")
    print(letras_ocultas)
    attempts -= 1

print("Thanks for playing!")