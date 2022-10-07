import sys
import random
from . import initialisation
from . import comparaison
from . import rentrer
from ..build import billes
from ..build import billes_reponses

def dynamique():
    n= 1.
    gagne = False
    repon = billes_reponses.C_billes_reponse()
    reponse = initialisation.initialisation()  # matrice à chercher
    while (n<13 and gagne!=True):
        print("ROUND ", n)
        essai = rentrer.rentrer()
        matrice_reponse = comparaison.comparaison(reponse, essai)
        print(matrice_reponse)
        if matrice_reponse == [repon.N]*4:
            gagne = True
            print("C'est gagné!")
            break
        n += 1
    print("GAME OVER")
