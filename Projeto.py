import random

lista_palavras = ["python", "java", "swift", "javascript"]
sair = False
won = 0
lost = 0


print("Palavra Achada\n")
while sair == False:
    attempts = 8
    palpites = []
    palavra_escondida = random.choice(lista_palavras)
    letras_ocultas = "-" * (len(palavra_escondida))
    letras_permitidas = "qwertyuiopasdfghjklzxcvbnm"

    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:' )
    escolha = input()

    if escolha == "play":
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
                    won += 1
                    break

            else:
                print("That letter doesn't appear in the word.")
                palpites.append(resposta)
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
                    lost += 1
                    break
            print(letras_ocultas)
        continue

    elif escolha == "results":
        print(f"You won: {won} times")
        print(f"You lost: {lost} times")
        continue

    elif escolha == "exit":
        break

    else:
        continue

