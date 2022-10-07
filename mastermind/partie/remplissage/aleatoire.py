import sys
import random
from ...build import billes

"""
retourne une matrice de 4 couleurs alétoires
"""
def initialisation():
    choix = [C_bille().b, C_bille().o, C_bille().r, C_bille().v, C_bille().j, C_bille().m]
    return [random.choice(choix) for i in range(4)]

