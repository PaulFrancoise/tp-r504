# Importer la fonction puissance depuis le fichier fonctions.py en utilisant un alias 'f'
import fonctions as f

try:
    # Saisie des deux nombres
    a = float(input("Entrez la base (a) : "))
    b = float(input("Entrez l'exposant (b) : "))

    # Appel de la fonction puissance avec vérification des entiers
    res = f.puissance(int(a), int(b))  # On convertit les entrées en entiers ici

    # Affichage du résultat
    print(f"{int(a)} élevé à la puissance {int(b)} est {res}")

except ValueError:
    # Gérer l'erreur si la conversion en entier échoue
    print("Veuillez entrer des nombres valides.")

except TypeError as e:
    # Gestion de l'erreur si les arguments ne sont pas des entiers
    print(f"Erreur : {e}")

