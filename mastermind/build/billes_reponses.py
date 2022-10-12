import sys
from rich import print

version = 'A1'

class C_billes_reponse:
    
    def __init__(self):
        """ 
        Billes ayant 2 choix de couleurs différentes:
        Noir (N) , Blanc (B)
        N => bon endroit bonne couleur
        B => que la couleur de bonne
        """
        
        self.B = "Blanc"
        self.N = "Noir"
        
