# Orientação a objetos<br> com bandeirinhas

![output passo quatro](s4.gif)

## Um exemplo em 7 passos
*Para executar [instale o Processing com o modo Python](http://villares.github.io/como-instalar-o-processing-modo-python/)*

Apresentamos aqui um exemplo de orientação a objetos utilizado em diversas aulas com pequenas variações. Para poder aproveitar o exemplo os alunos tem em aulas anteriores tiveram contato com programação procedural/imperativa[1] além de vocabulário específico da plataforma Processing:
* Declaração de variáveis e noções de tipagem;
* Métodos de desenho `rect`, `line`, `ellipse`, `beginShape`, `vertex` e `endShape`;
* Controle de atributos gráficos `fill`, `stroke`, `noStroke`, `noFill`, `background`;
* Controle de fluxo de execução e laços `if`, `else`, `for`;
* Declaração de funções com e sem parâmetros;
* Controle do sistema de coordenadas `pushMatrix`, `translate`, `rotate`, `scale`, `popMatrix`.

### 0. Definindo funções e deslocando o sistema de cordenadas
 ```python
def setup():
    """ Código chamado uma vez no início da execução pelo Processing """
    size(100, 100)  # define as dimensões do 'canvas' do Processing
    bandeirinha(50, 50)  # chama a função bandeirinha
 
def bandeirinha(px, py, tamanho=50):
    """ Desenha polígono em torno das coordenadas passadas, com tamanho padrão 50 """
    metade = tamanho / 2
    with pushMatrix():   # preseservando o sistema de coordenadas anterior,
        translate(px, py)  # translada o sistema de coordenadas
        beginShape()  # inicia polígono
        vertex(-metade, -metade)
        vertex(-metade, metade)
        vertex(0, 0)
        vertex(metade, metade)
        vertex(metade, -metade)
        endShape(CLOSE)  # encerra polígono, fechando no primeiro vértice
```
A definição da função `setup()` não é obrigatória no Modo Python, mas é a parte inicial da estrutura `setup()`/`draw()` usada na maior parte dos programas que trabalham com interação ou movimento, e é invocada uma única vez no início da execução. Note que neste momento já estará definida a função `bandeirinha()`. 

A função `bandeirinha()`recebe como parâmetros as coordenadas onde deve ser desenhada; Faz uma translação do sistema de cordenadas, move a origem, mas antes disso preserva o sistema orginal de coordenadas com `pushMatrix().


### 1. Redesenhando formas e atualizando variáveis no loop principal

### 2. Primeira aproximação da classe Bandeirinha

### 3. Instanciando mais alguns objetos

### 4. Ampliando a classe, mudando o comportamento e adicionando outras propriedades.

### 5. Uma lista de objetos

### 6. Acrescentando e removendo objetos; Mudança da cor com o mouse próximo.

[1] http://cs.lmu.edu/~ray/notes/paradigms/
