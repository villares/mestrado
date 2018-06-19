"""
Comparando itens em duas listas carregadas de arquivos texto
"""

y_inicial = 0
entrelinha = 14

def setup():
    global list1, list2, font
    size(400, 720)
    stroke(255)
    frameRate(12)
    font = createFont("Open Sans", 12)
    textFont(font)
    list1 = list(loadStrings("list1.txt"))
    list2 = list(loadStrings("list2.txt"))
    
def draw():
    background(0)
    highlight_not_in_second_list(list1, list2, 10)
    highlight_not_in_second_list(list2, list1, width/2)
    
def highlight_not_in_second_list(listA, listB, x_pos):
    for i, item in enumerate(listA):
        if item not in listB:
            fill(255, 200, 0)
        else: 
            fill(255)
        text(item, x_pos, 20 + y_inicial + i * entrelinha)

def mouseDragged():
    global y_inicial
    y_inicial += mouseY - pmouseY
        
