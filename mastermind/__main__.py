from mastermind.partie.dynamique import dynamique


print("Exécution du main:")
#cfg = dynamique()
#print(cfg['DEFAULT']['version'])


def main():                 # Sera utilisé comme point d'entrée dans setup.cfg
    print("Programme principal")
    dynamique()


if __name__ == "__main__":  # Sera utilisé par `python -m mypackage`
    main()
