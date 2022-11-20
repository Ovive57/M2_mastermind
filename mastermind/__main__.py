"""
The main module.
"""
from rich import print as rprint
from . import game

def main():
    """
    Function that calls the class and starts the game.
    """
    print("\nWelcome to Mastermind game ! Are you going to be the next Mastermind ? ")
    pegs = game.Mastermind()
    round_ = 1.
    win = False
    while (round_<13 and win is not True):
        print("\nROUND ", int(round_),"/ 12")
        win = pegs.evolve(win)
        round_ +=1
    if round_==13:
        rprint("[bold red]\nGAME OVER ![/bold red]")
        print("\nThe right answer was:")
        answer = [pegs.pegs[f'{pegs.answer[i]}']for i in range(len(pegs.answer))]
        rprint(' '.join(answer))
    return win


if __name__ == "__main__":
    main()
