import random

# Générer un nombre aléatoire entre 1 et 100
target = random.randint(1, 100)
essais = 0

print("J'ai choisi un nombre entre 1 et 100. Essaie de deviner !")

while True:
    try :
        guess = int(input("Entrez votre proposition : "))
        essais += 1
    except ValueError :
        print("Erreur ❌, tapez seulement des nombres s'il vous plait !")
        continue
    if guess > target:
        print("C'est plus grand !")
    elif guess < target:
        print("C'est plus petit !")
    else:
        print(f"Bravo 🎉, tu as trouvé le nombre en {essais} essais !")
        break
