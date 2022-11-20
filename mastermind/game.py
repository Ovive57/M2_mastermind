"""
The class Mastermind
"""
import random
from itertools import chain
from rich import print as rprint

__all__ = ['__version__']

__version__ = "top-level module"



class Mastermind:
    """
    This class is the Mastermind class. Pegs and board definitions.
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

    board =[]

    def __init__(self):
        """
        Initialitation. Generate a 4-list with random colors.
        """
        self.names = list(self.pegs.keys())
        self.colors = list(self.pegs.values())
        self.answer = [random.choice(self.names) for i in range(4)]
        #dictionary transformed in list :
        self.list = list(chain.from_iterable([[i,j] for i,j in self.pegs.items()]))

    def entry(self):
        """
        Takes the user input

        Returns:
            entries(list): user chosen colors
        """
        rprint("\nEnter 4 colors among : ", ' '.join(self.list))
        # Matrice avec une longueur = 4 à remplir par le joueur
        entries = [0.,0.,0.,0.]
        for i in range(4):
            entries[i] = input(f"\ncolor {i+1}:")
            while entries[i] not in self.names:
                print("You're writing nonsense ! Redo")
                entries[i] = input(f"color {i+1}:")
            # Imprime la couleur de la boule à chaque itération
            rprint(self.pegs[f"{entries[i]}"])
        return entries

    def comparaison(self, seq):
        """
        Comparation between the computer sequence i.e the answer to find
        and the user sequence.

        Args:
            seq(list): User choice

        Returns:
            sol(list): 4-colors list:
                black: if the user find a color in the right place
                white: if the user find a color but not in the right place
                '.': if the color chosen by the user is not in the computer sequence.
        """
        black = list(i for i,j in zip(self.answer,seq) if i==j)
        #indices associés:
        index_b = list(index for (index, item) in enumerate(seq) if item==self.answer[index])

        #Nouvelles matrices 'entry' et 'réponse' sans les boules pareilles:
        seq2 = list(value for (index, value) in enumerate(seq) if index not in index_b)
        answer2 = list(value for (index, value) in enumerate(self.answer) if index not in index_b)

        #liste des valeurs communes: (ne compte pas les doublons)
        vals = list(set(seq2).intersection(answer2))

        black = len(black)
        white = len(vals)
        nul = len(seq) - black - white
        sol = [self.ans['black']]*black+[self.ans['white']]*white+[self.ans['nul']]*nul
        random.seed(0) #Pour les tests, ne change pas la difficulté du jeu
        random.shuffle(sol)
        return sol


    def fill_board(self, new, matrix_response):
        """
        Add the turn in the board and print it
        """
        self.board.append([new,matrix_response])
        print("\nThe current board is:\n")
        for round_ in self.board:
            rprint(' '.join(round_[0]), ' ', ' '.join(round_[1]))


    def evolve(self, win):
        """
        Function that keep the game runing until you win

        Args:
            win (bool): True if you have everything right

        Returns:
            win (bool): True if you have everything right
        """
        attempt = self.entry()
        color_try = [self.pegs[f'{attempt[i]}']for i in range(len(attempt))]
        matrix_response = self.comparaison(attempt)
        self.fill_board(color_try, matrix_response)
        if matrix_response == [self.ans['black']]*4:
            win = True
            rprint("[bold red] \nYOU WIN ! YOU ARE THE MASTERMIND ![/bold red]")
        return win
