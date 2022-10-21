"""
Mastermind
doc doc doc
"""
from itertools import chain
import random
from rich import print as rprint

class Pegs:
    """
    This class is the Pegs class
    """
    pegs = {'yellow':'[bold yellow]\u25CF[/bold yellow]',
                'blue':'[blue]\u25CF[/blue]',
                'red':'[bold red]\u25CF[/bold red]',
                'green':'[bold green]\u25CF[/bold green]',
                'purple':'[bold purple]\u25CF[/bold purple]',
                'orange':'[bold orange3]\u25CF[/bold orange3]'}

    ans = {'black':'[black]\u25CF[/black]',
                'white':'[bold white]\u25CF[/bold white]',
                'nul':'.'}

    def __init__(self):
        """
        Retourne une matrice de 4 couleurs aléatoires
        """
        self.names = list(self.pegs.keys())
        self.colors = list(self.pegs.values())
        self.choix = [random.choice(self.names) for i in range(4)]
        #dictionary transformed in list :
        self.liste = list(chain.from_iterable([[i,j] for i,j in self.pegs.items()]))

    def entry(self):
        """
        Retourne un set entré par le joueur
        """
        rprint("Enter 4 colors among :", ' '.join(self.liste))
        entries = [0.,0.,0.,0.]
        for i in range(4):
            entries[i] = input(f"color {i+1}:")
            while entries[i] not in self.names:
                print("You're writing nonsense ! Redo")
                entries[i] = input(f"color {i+1}:")
            rprint(self.pegs[f'{entries[i]}'])
        return entries

    def comparaison(self, seq):
        """
        Comparation between the computer sequence i.e the answer to find
        and the user sequence (seq).
        Returns a list with a 4-colors sequence:
        - black if the user find a color in the right place
        - white if the user find a color but not in the right place
        - a '.' if the color chosen by the user is not in the computer sequence.
        """
        black = list(i for i,j in zip(self.choix,seq) if i==j)
        
        #indices associés:
        index_b = list(index for (index, item) in enumerate(seq) if item==self.choix[index])
        
        #Nouvelles matrices:
        seq2 = list(value for (index, value) in enumerate(seq) if index not in index_b)
        choix2 = list(value for (index, value) in enumerate(self.choix) if index not in index_b)
        
        
        #liste des valeurs communes: (ne compte pas les doublons)
        vals = list(set(seq2).intersection(choix2))
        
        black = len(black)
        white = len(vals)
        nul = len(seq) - black - white
        
        sol = [self.ans['black']]*black+[self.ans['white']]*white+[self.ans['nul']]*nul
        random.shuffle(sol)
        return sol

    def evolve(self, win):
        """
        something
        """
        essai = self.entry()
        print(self.choix)
        matrice_reponse = self.comparaison(essai)
        print("The key pegs are:")
        rprint(' '.join(matrice_reponse))
        if matrice_reponse == [self.ans['black']]*4:
            win = True
            rprint("[bold red]WIN ![/bold red]")
        return win
