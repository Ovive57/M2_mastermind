from . import dynamique


#cfg = dynamique()
#print(cfg['DEFAULT']['version'])


def main():                 # Sera utilisé comme point d'entrée dans setup.cfg
    print("Programme principal")
    pegs = dynamique.Pegs()
    round_ = 1.
    win = False
    while (round_<13 and win is not True):
        print("ROUND ", round_)
        win = pegs.evolve(round_, win)
        round_ +=1
    if round_==13:
        print("[bold red]GAME OVER ![/bold red]")


if __name__ == "__main__":  # Sera utilisé par `python -m mypackage`
    main()

print("Exécution du main:")
