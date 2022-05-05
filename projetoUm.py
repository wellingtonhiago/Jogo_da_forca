import random

print("""Palavra Achada
The game will be available soon.""")

lista_palavras = ["python", "java", "swift", "javascript"]

print("Palavra Achada")

palavra_escondida = random.choice(lista_palavras)
resposta = input("Guess the word: ")

if resposta == palavra_escondida:
    print("You survived!")
else:
    print("You lost!")
