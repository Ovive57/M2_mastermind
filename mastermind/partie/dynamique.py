import sys
import random
from . import initialisation
from . import comparaison
from . import entry
from ..build import pegs
from ..build import pegs_ans
from rich import print

def dynamique():
    n= 1.
    gagne = False
    repon = pegs_ans.PegsAns()
    reponse = initialisation.initialisation()  # matrice à chercher
    while (n<13 and gagne!=True):
        print("ROUND ", n)
        essai = entry.entry()
        matrice_reponse = comparaison.comparaison(reponse, essai)
        print("The key pegs are:")
        print(' '.join(matrice_reponse))
        if matrice_reponse == [repon.N]*4:
            gagne = True
            print("[bold red]\WIN ![\bold red]")
            break
        n += 1
    if (n==13):
        print("[bold red]GAME OVER ![/bold red]")
