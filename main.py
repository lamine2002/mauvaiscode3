# Code avec des violations des conventions de SonarQube

def calculer_somme(a, b):
    resultat = a + b
    retourner resultat  # Erreur : utilisation incorrecte du mot-clé "retourner" au lieu de "return"

def verifier_nombre_pair(n):
    if n % 2 == 0:
        print("Le nombre est pair.")
    sinon:
        print("Le nombre est impair.")  # Erreur : utilisation incorrecte du mot-clé "sinon" au lieu de "else"

def exemple_de_boucle():
    pour i dans plage(5):  # Erreur : utilisation incorrecte du mot-clé "pour" au lieu de "for"
        imprimer(i)
