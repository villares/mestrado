""" 
Para executar, instale Processing Modo Python
http://villares.github.io/como-instalar-o-processing-modo-python/
crie um arquivo a5.txt na pasta deste sketch, contando uma lista de ambientes
Código, Zona, Descrição, Cod1, Cod2, Cod3 [, CodN]... 
"""
from __future__ import unicode_literals
from __future__ import division
from __future__ import print_function

pontos = set()  # conjunto de Pontos
arestas = []    # lista de Arestas

TAM_PONTO = 50  # Diâmetro dos Pontos
TAM_BARRA = 100  # Distância sugerida para arestas

def setup():
    size(800, 800)
    strokeWeight(3)
    ambientes = leitura_tabela("a5.txt")
    print(ambientes)
    # cria pontos para cada ambiente
    for a in ambientes:
        x = random(width * .25, width * .75)
        y = random(height * .25, height * .75)
        cod, zona, desc = a[0], a[1], a[2]
        novo_ponto = Ponto(x, y, cod, zona, desc)  # cria um novo Ponto
        pontos.add(novo_ponto)  # acrescenta o Ponto no conjunto ('set')
    for a in ambientes:
        p1 = Ponto.de_cod(a[0])  # encontra o Ponto pelo codígo no set.
        for n2 in a[3:]:         # da terceira célula em diante na linha
            p2 = Ponto.de_cod(n2)  # descobre qual o Ponto pelo cod
            if not Aresta.existente(p1, p2):
                    nova_aresta = Aresta(p1, p2)
                    arestas.append(nova_aresta)

def draw():
    background(128)        # limpa a tela
    # para cada aresta
    for aresta in arestas:
        aresta.desenha()  # desenha a linha
        # altera a vel. dos pontos (para trazer ao tamanho)
        aresta.ajusta(TAM_BARRA)
    # para cada ponto
    for ponto in pontos:
        ponto.desenha()  # desenha
        ponto.move()    # atualiza posição

# Sob clique do mouse seleciona/deseleciona Pontos ou Arestasho
def mouseClicked():
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            ponto.sel = not ponto.sel  # inverte status de seleção

def keyPressed():   # Quando uma tecla é pressionada
    if key == 'r':  # Se a tecla 'r' for pressionada
        for ponto in pontos:
            # sorteia nova posição
            x = random(width * .25, width * .75)
            y = random(height * .25, height * .75)
            ponto.x, ponto.y = x, y

def mouseDragged():        # quando o mouse é arrastado
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < TAM_PONTO / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouseX, mouseY
            ponto.vx = 0
            ponto.vy = 0

def leitura_tabela(nome_arquivo):
    import csv
    with open(nome_arquivo) as arquivo:
        tabela = []
        for linha in csv.reader(arquivo):
            linha = [unicode(item.strip(), 'utf-8') for item in linha]
            tabela.append(linha)
    return tabela


class Ponto():

    " Pontos num grafo, inicial sorteada numa faixa, criam Arestas com outros Pontos "

    V_MAX = 2  # veloccodade máxima nas ortogonais vx e vy

    def __init__(self, x, y, cod, zona, desc):
        self.cod = cod
        self.zona = zona
        self.desc = desc
        self.x = x
        self.y = y
        self.z = 0  # para compatibilidade com PVector...
        self.vx = random(-Ponto.V_MAX, Ponto.V_MAX)
        self.vy = random(-Ponto.V_MAX, Ponto.V_MAX)
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
        texto = self.cod
        if dist(mouseX, mouseY, self.x, self.y) < TAM_PONTO / 2:
            stroke(255)
            noFill()
            ellipse(self.x, self.y, TAM_PONTO - 5, TAM_PONTO - 5)
            texto = texto + " " + self.desc
        fill(0)
        textAlign(CENTER, CENTER)
        text(texto, self.x, self.y)

    def move(self):
        if not self.sel:
            self.x += self.vx
            self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy
        self.vx = self.limitar(self.vx)
        self.vy = self.limitar(self.vy)

    def limitar(self, v):
        """ limita à velocidade máxima e para se estiver devagar"""
        v_max = Ponto.V_MAX
        if -.5 < v < .5:
            v = 0
        if v > v_max:
            return v_max
        elif v < -v_max:
            return -v_max
        else:
            return v

    @staticmethod
    def de_cod(pcod):
        for p in pontos:
            if p.cod == pcod:
                return p
        return None

class Aresta():

    """ Arestas contém só dois Pontos e podem ou não estar selecionadas """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def desenha(self):
        stroke(255)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def ajusta(self, tamanho):
        p1, p2 = self.p1, self.p2
        d = dist(p1.x, p1.y, p2.x, p2.y)
        delta = tamanho - d
        dir = PVector.sub(p1, p2)
        dir.mult(delta / 2000)
        p1.vx += dir.x
        p1.vy += dir.y
        p2.vx -= dir.x
        p2.vy -= dir.y
        
    @staticmethod
    def existente(p1, p2):
        for aresta in arestas:
            if (aresta.p1==p1 and aresta.p2==p2 or
                aresta.p1==p2 and aresta.p2==p1): 
                return True
        return False
