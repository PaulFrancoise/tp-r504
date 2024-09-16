def puissance ():
	a=
	b=
def test_2():
    """
    Fonction de test qui vérifie le comportement de la fonction puissance
    avec des valeurs négatives pour a et b.
    """
    print("Test avec des valeurs négatives :")
    
    try:
        # Cas 1 : a négatif, b positif
        a, b = -2, 3
        res = puissance(a, b)
        print(f"puissance({a}, {b}) = {res}")  # Résultat attendu : -8

        # Cas 2 : a négatif, b négatif
        a, b = -2, -3
        res = puissance(a, b)
        print(f"puissance({a}, {b}) = {res}")  # Résultat attendu : -0.125

        # Cas 3 : a positif, b négatif
        a, b = 2, -3
        res = puissance(a, b)
        print(f"puissance({a}, {b}) = {res}")  # Résultat attendu : 0.125

    except TypeError as e:
        print(f"Erreur : {e}")
