import sys
from ..build import billes_reponses
from rich import print
import random

def comparaison(A, B):
    """
    On compare la sequence donnée par l'ordinateur (A) i.e la reponse à trouver
    avec la sequence donnée par l'utilisateur.

    Returns:
        list : avec une sequence de 4 couleurs telles que:
            noir si l'utilisateur a trouvé une couleur dans le bon endroit.
            blanc si l'utilisateur a trouvé une couleur mais pas dans le bon endroit.
            . si l'utilisateur a mis des couleurs qui ne sont pas dans la sequence de l'ordinateur.
    """
    repon = billes_reponses.C_billes_reponse()
    bl = [i for i,j in zip(A,B) if i==j] # Bon endroit et couleur
    wh_bl = list(set(A)&set(B)) # Bonne couleur
    wh = len(wh_bl) - len(bl)
    nul = len(A) - len(wh_bl)
    
    sol = [repon.N]*len(bl)+[repon.B]*wh+[repon.R]*nul
    random.shuffle(sol)
    
    return sol
