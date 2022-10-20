from ..build import pegs
from rich import print


def entry():
    p = pegs.Pegs()
    colors = [p.y, p.y_c, p.b, p.b_c, p.r, p.r_c, p.g, p.g_c, p.p, p.p_c, p.o, p.o_c]
    print("Enter 4 colors among :", ' '.join(colors))
    
    c = [0.,0.,0.,0.]
    for i in range(4):
        c[i] = input(f"color {i+1}:")
        while c[i] not in colors:
            print("You're writing nonsense ! Redo")
            c[i] = input(f"color {i+1}:")
        print(colors[colors.index(c[i])+1])
            
            
    return c
