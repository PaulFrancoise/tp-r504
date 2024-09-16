def puissance(a, b):
    """
    Cette fonction prend deux arguments a et b,
    vérifie qu'ils sont des entiers, et renvoie le résultat de a élevé à la puissance b.
    Lève une exception TypeError si les arguments ne sont pas des entiers.
    """
    # Vérification des types des arguments
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")

    # Calcul de la puissance
    return a ** b

