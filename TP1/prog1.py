print("taper un nombre")
a=int(input())
print("a+1",a+1)

while True:
    try:
        # Saisir un nombre au clavier
        nombre = float(input("Entrez un nombre: "))
        
        # Afficher le carré du nombre
        print(f"Le carré de {nombre} est {nombre ** 2}")
    
    except ValueError:
        # Gérer le cas où l'utilisateur entre autre chose qu'un nombre
        print("Veuillez entrer un nombre valide.")
    
    except KeyboardInterrupt:
        # Sortir de la boucle infinie avec CTRL-C
        print("\nBoucle interrompue. Au revoir!")
        break


