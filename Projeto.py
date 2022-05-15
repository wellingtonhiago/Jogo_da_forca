import random

lista_palavras = ["python", "java", "swift", "javascript"]

print("Palavra Achada\n")

palavra_escondida = random.choice(lista_palavras)
letras_ocultas = "-" * (len(palavra_escondida))
attempts = 8
palpites = []
letras_permitidas = "qwertyuiopasdfghjklzxcvbnm"

print(letras_ocultas)
while(attempts > 0):
    resposta = input("Input a letter: ")
    indice = 0

    if len(resposta) != 1:
        print("Please, input a single letter.")
    elif resposta not in letras_permitidas:
        print("Please, enter a lowercase letter from the English alphabet.")

    elif resposta in palpites:
        print("You've already guessed this letter.")
    elif resposta in palavra_escondida:
        palpites.append(resposta)
        for letra in palavra_escondida:
            if resposta == letra:
                letras_ocultas = letras_ocultas[:indice] + resposta + letras_ocultas[indice + 1:]
            indice += 1
        if letras_ocultas == palavra_escondida:
            print(f"You guessed the word {palavra_escondida}!")
            print("You survived!")
            break

    else:
        print("That letter doesn't appear in the word.")
        palpites.append(resposta)
        attempts -= 1
        if attempts == 0:
            print("You lost!")
            break
    print(letras_ocultas)
