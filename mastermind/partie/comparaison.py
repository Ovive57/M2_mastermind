from ..build import pegs_ans
import random

def comparaison(A, B):
    """
    Comparation between the computer sequence (A) i.e the answer to find
    and the user sequence (B).
    
    Returns:
        list : with a 4-colors sequence:
            black if the user find a color in the right place
            white if the user find a color but not in the right place
            . if the color chosen by the user is not in the computer sequence.
    """
    
    repon = pegs_ans.PegsAns()
    bl = [i for i,j in zip(A,B) if i==j] # Right place right color.
    wh_bl = list(set(A)&set(B)) # Right color
    wh = len(wh_bl) - len(bl) # Right color but not right place
    nul = len(A) - len(wh_bl) # Nothing right
    
    sol = [repon.B]*len(bl)+[repon.W]*wh+[repon.N]*nul
    random.shuffle(sol)
    
    return sol
