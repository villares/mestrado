"""
The Art of COMPUTER GRAPHICS Programming - chapter 9
Conversão para o Processing Modo Python da conversão para Processing feita pro Viviane Alencar
http://lapac.fec.unicamp.br/index.php/re/programming/projects/taocgp/
"""


def setup():
    size(800,600)

def draw():     
    length1 = 200
    width1 = 50
     
    x_increment = 50
    y_increment = 50
    num_of_steps = 10
     
    x = 50
    y = 50
     
    for i in range(num_of_steps):
        rect(x,y,length1,width1)
        x += x_increment
        y += y_increment
