"""
Consumindo Estatisticas Municipios
Exemplo: http://educacao.dadosabertosbr.com/api/estatisticas?tipoLocal=MUN&codMunicipio=5300108
Inspirado no material do prof. Fernando Masanori
"""
from socket import timeout
import urllib.request
import json
 
def detalhe(cod):
    url = 'http://educacao.dadosabertosbr.com/api/estatisticas?tipoLocal=MUN&codMunicipio='
    try:
        resp = urllib.request.urlopen(url+str(cod), timeout=1).read()
        resp = json.loads(resp.decode('utf-8'))
    except:
        with open('erros.txt', 'a') as e:
            e.write(cod)
        print(cod + " Timeout")
        resp = None
    if resp:
        det =','.join(map(str,(
                    resp['codMunicipio'],
                    resp['computadoresAlunos'],
                    resp['internet'],
                    resp['bandaLarga'],
                    resp['datashows'],
                    resp['televisores'],
                    resp['laboratorioInformatica'],
                    resp['salasUtilizadas'],
                    resp['ano']
                         )))
        #print(det)
        return det
    else:
        return None
 
with open("municipios-2013.txt") as arquivo:
    municipios = arquivo.readlines()
 
with open('dados-municipios-2013.csv', 'a') as dados:
    dados.write('codMunicipio,'+
                'computadoresAlunos,'+
                'internet,'+
                'bandaLarga,'+
                'datashows, televisores'+
                'laboratorioInformatica,'+
                'salasUtilizadas,'+
                'ano'+'\n')

    for m in municipios:
        m = m.strip()
        if m:
            linha = detalhe(m)
            if linha: dados.write(linha + '\n')
            print(m + " OK")
 
print('feito, verifique o arquivo erros.txt para as localidades que faltaram')
