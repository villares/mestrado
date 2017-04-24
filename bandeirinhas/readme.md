# Orientação a objetos<br> com bandeirinhas

![output passo quatro](s4.gif)

## Um exemplo em 7 passos
*Para executar [instale o Processing com o modo Python](http://villares.github.io/como-instalar-o-processing-modo-python/)*

Apresentamos aqui um exemplo de orientação a objetos utilizado em diversas aulas com pequenas variações. Para poder aproveitar o exemplo os alunos tem em aulas anteriores contato com programação procedural além de vocabulário específico da plataforma Processing:
* Declaração de variáveis e noções de tipagem;
* Métodos de desenho `rect`, `line`, `ellipse`, `beginShape`, `vertex` e `endShape`;
* Controle de atributos gráficos `fill`, `stroke`, `noStroke`, `noFill`, `background`;
* Controle de fluxo de execução e laços `if`, `else`, `for`;
* Declaração de funções com e sem parâmetros;
* Controle do sistema de coordenadas `pushMatrix`, `translate`, `rotate`, `scale`, `popMatrix`.

### 0. Definindo funções e deslocando o sistema de cordenadas
 ```python
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

bandeirinha(50, 50)
```
Exemplo de declaração de uma função com parâmetros; translação do sistema de cordenadas,
preservando o sistema orginal com `pushMatrix()`.

Quando apenas invocada a função `bandeirinha()` a área de desenho padrão do Processing é 100 x 100 pixels, com um fundo cinza.

### 1. Redesenhando formas e atualizando variáveis no loop principal

### 2. Primeira aproximação da classe Bandeirinha

### 3. Ampliando a classe

### 4. Instanciando mais alguns objetos

### 5. Uma lista de objetos

### 6. Acrescentando e removendo objetos; Mudança da cor com o mouse próximo.
