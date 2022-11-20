import pytest
import mastermind.__main__ as mm
import mastermind.game as game
import random
import builtins
import mock

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
    assert game.version == "top-level module"
    
    
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
def test_entry(monkeypatch, capsys, expected_output):
    import builtins
    monkeypatch.setattr(builtins, 'input', lambda _: names[0])

    pegs.entry()
    captured, err = capsys.readouterr()
    assert captured == expected_output
    
    
@pytest.mark.parametrize("expected_output", 
                        [['blue', 'blue', 'blue', 'blue']]
                        )
def test_entry(monkeypatch, capsys, expected_output):
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
    
    
    
@pytest.mark.parametrize("test_input, expected_output",
                        [
                            # Teste pour tout correct
                            (['blue', 'blue', 'blue', 'blue'], 
                            ['[black]\u25CF[/black]', '[black]\u25CF[/black]', '[black]\u25CF[/black]', '[black]\u25CF[/black]'])
                        ])
def test_comparaison_black(test_input, expected_output):
    """
    Teste une combinaison correcte
    """
    pegs.answer = ['blue', 'blue', 'blue', 'blue']
    assert pegs.comparaison(test_input) == expected_output
    
"""
@pytest.mark.parametrize("test_input",
                        [
                        (['green', 'orange', 'red', 'red'])
                        ])
def test_comparaison_white(monkeypatch, test_input):
    random.seed(0)
    pegs.answer = ['blue', 'blue', 'green', 'green']
    expected_output = ['[bold white]\u25CF[/bold white]','[bold white]\u25CF[/bold white]', '.', '.']
    
    inputs2 = iter(['blue', 'blue', 'blue', 'blue'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs2))
    
    expected_output = random.shuffle(expected_output)
    assert pegs.comparaison(test_input) == expected_output

"""

@pytest.mark.parametrize("test_input",
                        [
                        (['green', 'orange', 'red', 'red'])
                        ])
def test_comparaison_white_len(test_input):
    random.seed(0)
    pegs.answer = ['yellow', 'yellow', 'green', 'green']
    assert len(pegs.comparaison(test_input)) == 4
    assert type(pegs.comparaison(test_input)) == list


@pytest.mark.parametrize("test_input, expected_output",
                        [
                            # Teste pour pas au bon endroit
                            (['purple', 'red', 'orange', 'blue'], 
                            ['.', '.', '.', '.'])
                        ])
def test_comparaison_wrong(test_input, expected_output):
    """
    Teste une combinaison fausse
    """
    pegs.answer = ['green', 'green', 'yellow', 'yellow']
    assert pegs.comparaison(test_input) == expected_output
    
    
    
    
    
    
    
    
    
    

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
    with pytest.raises(TypeError):
        pegs.fill_board(*test_input)
        
 
def test_main(monkeypatch):
    inputs = iter([random.choice(names) for i in range(4*13)])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    win = mm.main()
    assert win == False
        
        
"""
    
def test_main(monkeypatch, capsys):
    win = False
    random.seed(0)
    import builtins
    inputs = iter([random.choice(names) for i in range(4)])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    out = pegs.evolve(win)
    assert out == True
    
""" 

   
"""
@pytest.mark.parametrize("expected_output", 
                        [['blue', 'blue', 'blue', 'blue']]
                        )
def test_main(monkeypatch, capsys, expected_output):
    inputs = iter(['blue', 'blue', 'blue', 'blue'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    mastermind.__main__.main()
    
    assert win == True
    
    
"""
