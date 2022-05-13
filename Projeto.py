import random

print("""Palavra Achada
The game will be available soon.""")

lista_palavras = ["python", "java", "swift", "javascript"]

print("Palavra Achada")

palavra_escondida = random.choice(lista_palavras)
letras_reveladas = palavra_escondida[ : 3]
letras_ocultas = "-" * (len(palavra_escondida) - 3)

resposta = input(f"Guess the word {letras_reveladas}{letras_ocultas}: ")

if resposta == palavra_escondida:
    print("You survived!")
else:
    print("You lost!")
