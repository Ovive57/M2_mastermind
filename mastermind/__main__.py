"""
c'est le main
"""
from rich import print as rprint
from . import dynamique

def main():
    """
    something
    """
    print("Bienvenue au Jeu du Mastermind !")
    pegs = dynamique.Pegs()
    round_ = 1.
    win = False
    while (round_<13 and win is not True):
        print("ROUND ", round_)
        win = pegs.evolve(win)
        round_ +=1
    if round_==13:
        rprint("[bold red]GAME OVER ![/bold red]")


if __name__ == "__main__":
    main()
