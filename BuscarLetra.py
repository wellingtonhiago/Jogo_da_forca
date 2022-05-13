magic = "abracadabra"  # Quatas letras tem na palavra
print(magic.count("abra"))  # 2
print(magic.count("a"))     # 5
print(magic.count("l"))     # 0


best = "friend"  # Posição da letra na palavra
print(best.find("i"))   # 2
print(best.find("u"))   # -1
print(best.index("i"))  # 2
print(best.index("u"))  # ValueError
