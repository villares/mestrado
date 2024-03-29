""" 
Para executar, instale Processing Modo Python
http://villares.github.io/como-instalar-o-processing-modo-python/
crie um arquivo a.txt na pasta deste sketch, contando uma lista de ambientes
"""

import csv
import random as rnd  # para não conflitar com o random do Processing

with open("a.txt") as f:
    ambientes = list(csv.reader(f))
print ambientes

pontos = set()  # conjunto de Pontos
arestas = []    # lista de Arestas

TAM_PONTO = 50  # TAM_PONTO dos Pontos \
TAM_BARRA = 100
VEL_MAX = 2  # velocidade máxima nas ortogonais vx e vy
PONTOS_INI = 5  # númer inicial de pontos

def setup():
    size(600, 600)
    strokeWeight(3)
    for a in ambientes: #range(PONTOS_INI):
        x, y = random(width), random(height)
        novo_ponto = Ponto(x, y)
        novo_ponto.nome = a[0].strip()
        pontos.add(novo_ponto)  # acrescenta um Ponto
    for a in ambientes: #range(PONTOS_INI):
        p1 = Ponto.de_nome(a[0].strip())
        for n2 in a[2:]:
            p2 =  Ponto.de_nome(n2.strip())
            nova_aresta = Aresta(p1, p2)
            arestas.append(nova_aresta)     

def draw():
    background(128)        # limpa a tela
    # para cada ponto
    # para cada aresta
    for aresta in arestas:  # checa se há Arestas com Pontos já removidos
        if (aresta.p1 not in pontos) or (aresta.p2 not in pontos):
            arestas.remove(aresta)   # nesse caso remove a Aresta também
        else:                # senão
            aresta.desenha()  # desenha a linha
            Aresta.puxa_empurra(aresta.p1, aresta.p2, TAM_BARRA)  # altera a velocidade dos pontos

    for ponto in pontos:
        ponto.desenha()  # desenha
        ponto.move()    # atualiza posição
  
# Sob clique do mouse seleciona/deseleciona Pontos ou Arestas
def mouseClicked():
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            ponto.sel = not ponto.sel  # inverte status de seleção

def keyPressed():   # Quando uma tecla é pressionada
    # Barra de espaço acrescenta Pontos na posição atual do mouse
    if key == ' ':
        pontos.add(Ponto(mouseX, mouseY))  # acrescenta Ponto no set
    # 'd' remove os Pontos previamente selecionandos com clique, marcados em preto.
    if key == 'd':
        for ponto in pontos:
            # se a lista tiver pelo menos 2 pontos
            if ponto.sel and len(pontos) > 1:
                pontos.remove(ponto)           # remove pontos selecionados
        for aresta in arestas:
            if aresta.sel:  # se a lista tiver pelo menos 2 pontos
                arestas.remove(aresta)           # remove pontos selecionados
    if key == "z":
        for ponto in pontos:
            for outro in pontos:
                Aresta.puxa_empurra(ponto, outro, TAM_BARRA*1.5)

def mouseDragged():        # quando o mouse é arrastado
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouseX, mouseY
            ponto.vx = 0
            ponto.vy = 0

class Ponto():

    " Pontos num grafo, VEL_MAX inicial sorteada, criam Arestas com outros Pontos "

    def __init__(self, x, y):
        self.nome = int(random(255))
        self.x = x
        self.y = y
        self.z = 0  # para compatibilidade com PVector...
        self.vx = random(-VEL_MAX, VEL_MAX)
        self.vy = random(-VEL_MAX, VEL_MAX)
        self.sel = False   # se está selecionado, começa sem seleção
        self.cor = color(random(128, 255),  # R
                         random(128, 255),  # G
                         random(128, 255),  # B
                         255)              # Alpha ~50%

    def desenha(self):
        if self.sel:
            stroke(0)
        else:
            noStroke()
        fill(self.cor)
        ellipse(self.x, self.y, TAM_PONTO, TAM_PONTO)
        if dist(mouseX, mouseY, self.x, self.y) < TAM_PONTO:
            stroke(255)
            noFill()
            ellipse(self.x, self.y, TAM_PONTO + 5, TAM_PONTO + 5)
            # fill(0)
            # text(str(len(pontos)) + " " + str(len(arestas)), self.x, self.y)
        fill(0)
        textAlign(CENTER, CENTER)
        text(str(self.nome), self.x, self.y)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy
        self.vx = self.limitar(self.vx, VEL_MAX)
        self.vy = self.limitar(self.vy, VEL_MAX)

    def limitar(self, v, v_max):
        if -.5 < v < .5: v=0
        if v > v_max:
            return v_max
        elif v < -v_max:
            return -v_max
        else:
            return v
        
    @staticmethod
    def de_nome(nome):
        for p in pontos:
            if p.nome == nome:
                return p
        return None    
    
class Aresta():

    """ Arestas contém só dois Pontos e podem ou não estar selecionadas """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.sel = False

    def desenha(self):
        if self.sel:
            stroke(0)
        else:
            stroke(255)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        noStroke()
        fill(255)
        ellipse(self.p1.x, self.p1.y, TAM_PONTO / 6, TAM_PONTO / 6)
        ellipse(self.p2.x, self.p2.y, TAM_PONTO / 6, TAM_PONTO / 6)

    @staticmethod    
    def puxa_empurra(p1, p2, tamanho):
        d = dist(p1.x, p1.y, p2.x, p2.y)
        delta = tamanho - d
        dir = PVector.sub(p1, p2)
        dir.mult(delta / 2000)
        p1.vx += dir.x
        p1.vy += dir.y
        p2.vx -= dir.x
        p2.vy -= dir.y
