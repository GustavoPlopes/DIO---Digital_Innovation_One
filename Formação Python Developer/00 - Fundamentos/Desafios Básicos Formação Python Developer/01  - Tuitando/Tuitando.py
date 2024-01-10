T = input()

numero_de_caracteres = int(len(T))

if (numero_de_caracteres <= 140 and numero_de_caracteres > 1):
    print("TWEET")

elif (numero_de_caracteres > 140 or numero_de_caracteres < 1):
    print("MUTE")