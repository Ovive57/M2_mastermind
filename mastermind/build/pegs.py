import sys

version = 'A1'

class Pegs:
    
    def __init__(self):
        """
        Color pegs with 6 differents choices between:
        yellow (Y), blue (B), red (R), green (G), purple (P) and orange (O)
        """
        
        self.y = "Y"
        self.y_c = "[bold yellow]\u25CF[/bold yellow]"
        self.b = "B"
        self.b_c = "[bold blue]\u25CF[/bold blue]"
        self.r = "R"
        self.r_c = "[bold red]\u25CF[/bold red]"
        self.g = "G"
        self.g_c = "[bold green]\u25CF[/bold green]"
        self.p = "P"
        self.p_c = "[bold purple]\u25CF[/bold purple]"
        self.o = "O"
        self.o_c = "[bold orange]\u25CF[/bold orange]"
