import sys
from ..build import billes_reponses
from rich import print

def comparaison(grilleA, grilleB):
    """ 
    On compare grille A et grille B
    """
    repon = billes_reponses.C_billes_reponse()
    grille_solution = [0]*len(grilleA)
    for i in range(len(grilleA)):
        if grilleB[i] == grilleA[i]:
            grille_solution[i] = repon.N
        elif grilleB[i] in grilleA :
            grille_solution[i] = repon.B
        else:
            grille_solution[i] = "."
    return grille_solution
            
