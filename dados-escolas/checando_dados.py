"""
Recriando o erros.txt que perdi
"""

import csv
  
with open("municipios-2013.txt") as arquivo:
    municipios = arquivo.readlines()
    mun_lista = [m.strip() for m in municipios]
 
with open('dados-municipios-2013.csv') as dados:
    feitos = csv.reader(dados)
    mun_feitos = [m[0].strip() for m in feitos]
    
erros = [m for m in mun_lista if m not in mun_feitos]

with open('erros.txt', 'w') as f:
    for mun in erros:
        f.write(mun + "\n")
print("feito")
