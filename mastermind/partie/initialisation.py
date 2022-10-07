import sys
import random
from ..build import billes

"""
retourne une matrice de 4 couleurs alétoires
"""

def initialisation():
    couleur = billes.C_billes()
    choix = [couleur.b, couleur.o, couleur.r, couleur.v, couleur.j, couleur.m]
    achoix = [random.choice(choix) for i in range(4)]
    return achoix
