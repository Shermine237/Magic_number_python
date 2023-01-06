import random


def demander_nombre(nombre_min, nombre_max):
    nombre = 0
    while nombre not in range(nombre_min, nombre_max+1):
        try:
            nombre = int(input(f"Choisissez un nombre entre {nombre_min} et {nombre_max} :  "))
        except:
            print("Mauvaise saisie, veuillez recommencer :")
    return int(nombre)


def resultat(nombre_choisi, nombre_magique):
    if nombre_choisi == nombre_magique:
        print(f"Bravo ! Vous avez trouve le nombre magique : {nombre_magique}")
        return True
    elif nombre_choisi < nombre_magique:
        print(f"Le nombre magique est plus grand que {nombre_choisi}")
    elif nombre_choisi > nombre_magique:
        print(f"Le nombre magique est plus petit que {nombre_choisi}")
    return False


NOMBRE_VIES = 4
NOMBRE_MIN = 1
NOMBRE_MAX = 15
NOMBRE_MAGIC = random.randint(NOMBRE_MIN, NOMBRE_MAX)

print("     NOMBRE MAGIQUE")
print("Devinez le nombre magique")
vie_restante = NOMBRE_VIES
stop = False
while not stop:
    if vie_restante == 0:
        print(f"Vous n'avez plus de vie, le nombre magique etait {NOMBRE_MAGIC}")
        break
    nombre_saisi = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    print()
    stop = resultat(nombre_saisi, NOMBRE_MAGIC)
    vie_restante -= 1
    print(f"Il vous reste {vie_restante} vie(s)")
