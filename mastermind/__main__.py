"""
The main program.
"""
from rich import print as rprint
from . import dynamique

def main():
    """
    Function that calls the class and starts the game.

    Returns
    -------
    Game interface : string prints
    """
    print("\nWelcome to Mastermind game ! Are you going to be the next Mastermind ? ")
    pegs = dynamique.Pegs()
    round_ = 1.
    win = False
    while (round_<13 and win is not True):
        print("\nROUND ", round_)
        pegs.evolve(win)
        round_ +=1
    if round_==13:
        rprint("[bold red]\nGAME OVER ![/bold red]")


if __name__ == "__main__":
    main()
