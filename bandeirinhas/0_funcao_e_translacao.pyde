def bandeirinha(px, py, tamanho):
    metade = tamanho / 2
    with pushMatrix():
        translate(px, py)
        beginShape()
        vertex(-metade, -metade)
        vertex(-metade, metade)
        vertex(0, 0)
        vertex(metade, metade)
        vertex(metade, -metade)
        endShape(CLOSE)

bandeirinha(50, 50, 50)
