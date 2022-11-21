"""
Module de tests
"""
import random
import builtins
import pytest
import mastermind.__main__ as mm
from mastermind import game


pegs = game.Mastermind()

names = ['yellow','blue','red','green','purple','orange']

liste = ['yellow','[bold yellow]\u25CF[/bold yellow]',
                'blue','[blue]\u25CF[/blue]',
                'red','[bold red]\u25CF[/bold red]',
                'green','[bold green]\u25CF[/bold green]',
                'purple','[bold purple]\u25CF[/bold purple]',
                'orange','[bold orange3]\u25CF[/bold orange3]']

colors = ['[bold yellow]\u25CF[/bold yellow]',
                '[blue]\u25CF[/blue]',
                '[bold red]\u25CF[/bold red]',
                '[bold green]\u25CF[/bold green]',
                '[bold purple]\u25CF[/bold purple]',
                '[bold orange3]\u25CF[/bold orange3]']


def test_version():
    """
    Teste la version du module
    """
    assert game.__version__ == "top-level module"


def test_init():
    """
    Vérifie les listes et la liste de 4 couleurs aléatoires.
    """
    assert pegs.names == names
    assert pegs.colors == colors

    assert pegs.list == liste


@pytest.mark.parametrize("expected_output",
                        [
                        "\nEnter 4 colors among :  yellow \u25CF blue \u25CF red \u25CF green \u25CF purple \u25CF orange \u25CF\n\u25CF\n\u25CF\n\u25CF\n\u25CF\n"
                        ]
                        )
def test_entry_form(monkeypatch, capsys, expected_output):
    """
    Teste la forme de l'output
    """
    monkeypatch.setattr(builtins, 'input', lambda _: names[0])

    pegs.entry()
    captured, err = capsys.readouterr()
    assert captured == expected_output


@pytest.mark.parametrize("expected_output",
                        [['blue', 'blue', 'blue', 'blue']]
                        )
def test_entry(monkeypatch, expected_output):
    """
    Teste une entrée où le joueur:
    1. a bien répondu
    2. s'est trompé et a réécrit
    """
    inputs = iter(['blue', 'blue', 'blue', 'blue'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    #monkeypatch.setattr(builtins, 'input', lambda _: 'blue')
    entries = pegs.entry()
    assert entries == expected_output

    inputs2 = iter(['blue', 'bleu', 'blue', 'blue', 'blue'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs2))

    #monkeypatch.setattr(builtins, 'input', lambda _: 'blue')
    entries = pegs.entry()
    assert entries == expected_output


@pytest.mark.parametrize("test_input_black, expected_output_black, \
                        test_input_white, expected_output_white, \
                        test_input_wrong, expected_output_wrong",
                        [
                            # Teste pour tout correct
                            (['blue', 'blue', 'blue', 'blue'],
                            ['[black]\u25CF[/black]', '[black]\u25CF[/black]', '[black]\u25CF[/black]', '[black]\u25CF[/black]'],
                            # Teste pour bon mais pas à la bonne place
                            ['orange', 'red', 'blue', 'red'],
                            ['[bold white]\u25CF[/bold white]','.', '.', '.'],
                            # Teste pour tout faux
                            ['purple', 'red', 'orange', 'blue'],
                            ['.', '.', '.', '.'])
                        ])
def test_comparaison(monkeypatch, test_input_black, expected_output_black,
                    test_input_white, expected_output_white,
                    test_input_wrong, expected_output_wrong):
    """
    Teste une combinaison
    - tout est correct
    - deux sont bons mais pas à la bonne place
    """
    pegs.answer = ['blue', 'blue', 'blue', 'blue']
    assert pegs.comparaison(test_input_black) == expected_output_black

    seed = 0
    inputs = iter(test_input_white)
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    random.seed(seed)
    random.shuffle(expected_output_white)
    pegs.answer = ['blue', 'blue', 'green', 'green']
    assert pegs.comparaison(test_input_white) == expected_output_white

    pegs.answer = ['green', 'green', 'yellow', 'yellow']
    assert pegs.comparaison(test_input_wrong) == expected_output_wrong



@pytest.mark.parametrize("test_input",
                        [
                        (['green', 'orange', 'red', 'red'])
                        ])
def test_comparaison_len_type(test_input):
    """
    Verifie la taille et le type de la variable retournée par comparaison.
    """
    random.seed(0)
    pegs.answer = ['yellow', 'yellow', 'green', 'green']
    assert len(pegs.comparaison(test_input)) == 4
    assert type(pegs.comparaison(test_input)) == list



@pytest.mark.parametrize("test_input_1, test_input_2",
                        [
                            (['blue', 'blue', 'blue', 'blue'],
                            ['black', 'black', 'black', 'black'])
                        ])
def test_fill_board(capfd, test_input_1, test_input_2):
    """
    Teste le output
    """
    pegs.board = []
    pegs.fill_board(test_input_1, test_input_2)
    out, err = capfd.readouterr()
    assert out == '\nThe current board is:\n\nblue blue blue blue   black black black black\n'


@pytest.mark.parametrize("test_input", [(), (1,2), [1,2,3]])
def test_fill_board_args(test_input):
    """
    Teste les cas où:
    - il manque les arguments
    - le type des arguments ne convient pas
    - le nombre d'argument ne convient pas
    """
    with pytest.raises(TypeError):
        pegs.fill_board(*test_input)


@pytest.mark.parametrize("test_input",
                        [
                            (), (True, False)
                        ])
def test_evolve(test_input):
    """
    Teste les cas où:
    - il manque les arguments
    - le nombre d'argument ne convient pas
    """
    with pytest.raises(TypeError):
        pegs.fill_board(*test_input)


def test_evolve_form(monkeypatch):
    """
    Teste une partie gagnée
    """
    inputs = iter(pegs.answer)
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    pegs.board = []
    win = pegs.evolve(False)
    assert win is True


def test_main(monkeypatch):
    """
    Test la fin du jeu.
    """
    inputs = iter([random.choice(names) for i in range(4*13)])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    win = mm.main()
    assert win is False
