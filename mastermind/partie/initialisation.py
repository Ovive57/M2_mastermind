import random
from ..build import pegs

"""
retourne une matrice de 4 couleurs alétoires
"""

def initialisation():
    couleur = pegs.Pegs()
    choix = [couleur.b, couleur.o, couleur.r, couleur.g, couleur.y, couleur.p]
    achoix = [random.choice(choix) for i in range(4)]
    return achoix
