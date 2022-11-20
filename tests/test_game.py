import pytest
import mastermind.game as game


pegs = game.Mastermind()


def test_version():
    """
    Teste la version du module
    """
    assert game.version == "top-level module"
    
    
def test_init():
    """
    Vérifie les listes et la liste de 4 couleurs aléatoires.
    """
    assert pegs.names == ['yellow','blue','red','green','purple','orange']
    assert pegs.colors == ['[bold yellow]\u25CF[/bold yellow]',
                '[blue]\u25CF[/blue]',
                '[bold red]\u25CF[/bold red]',
                '[bold green]\u25CF[/bold green]',
                '[bold purple]\u25CF[/bold purple]',
                '[bold orange3]\u25CF[/bold orange3]']
    
    assert pegs.list == ['yellow','[bold yellow]\u25CF[/bold yellow]',
                'blue','[blue]\u25CF[/blue]',
                'red','[bold red]\u25CF[/bold red]',
                'green','[bold green]\u25CF[/bold green]',
                'purple','[bold purple]\u25CF[/bold purple]',
                'orange','[bold orange3]\u25CF[/bold orange3]']
    
    
    
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
@pytest.mark.parametrize("test_input, expected_output",
                        [
                            # Teste pour pas au bon endroit
                            (['yellow', 'yellow', 'green', 'green'], 
                            ['[bold white]\u25CF[/bold white]', '[bold white]\u25CF[/bold white]', '[bold white]\u25CF[/bold white]', '[bold white]\u25CF[/bold white]'])
                        ])
def test_comparaison_white(test_input, expected_output):
    random.seed(5)
    pegs.answer = random.choice()
    
    assert pegs.comparaison(test_input) == expected_output
"""

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


