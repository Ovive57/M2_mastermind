

version = 'A1'

class PegsAns:
    
    def __init__(self):
        """
        
        Color pegs with the answers:
        
        Black if right color in the right place
        White if the right color but not in the right place
        . if the color is not in the sequence
        
        """
        
        self.B = "[bold black]\u25CF[/bold black]"
        self.W = "[bold white]\u25CF[/bold white]"
        self.N = "."
        
