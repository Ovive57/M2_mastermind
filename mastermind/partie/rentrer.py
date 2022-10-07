import sys
from ..build import billes



def rentrer():
    couleur = billes.C_billes()
    mcouleurs = [couleur.j, couleur.b, couleur.r, couleur.v, couleur.m, couleur.o]
    print("entrez 4 couleurs parmi :", couleur.j, couleur.b, couleur.r, couleur.v, couleur.m, couleur.o)
    a = input("couleur1:")
    if a not in mcouleurs:
        print("Tu écris n'importe quoi")
    b = input("couleur 2:")
    if b not in mcouleurs:
        print("Tu écris n'importe quoi")
    c = input("couleur 3:")
    if c not in mcouleurs:
        print("Tu écris n'importe quoi")
    d = input("couleur 4:")
    if d not in mcouleurs:
        print("Tu écris n'importe quoi")
    return [a,b,c,d]
