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
        print("\nROUND ", int(round_),"/ 12")
        pegs.evolve(win)
        round_ +=1
    if round_==13:
        rprint("[bold red]\nGAME OVER ![/bold red]")
        print("\nThe right answer was:")
        answer = [pegs.pegs[f'{pegs.choix[i]}']for i in range(len(pegs.choix))]
        rprint(' '.join(answer))



if __name__ == "__main__":
    main()
