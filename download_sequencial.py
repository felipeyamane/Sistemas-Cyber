'''

'''

from wget import download #Import Apenas da função de download da biblioteca wget
from time import time #


endereco = 'http://arquivos.afonsomiguel.com/'
arquivo_string = 'arquivo_'
num_arquivo = ''
extensao = '.jpg'


inicio = time()

for i in range(0,10):
    num_arquivo = str(i)
    download(endereco+arquivo_string+num_arquivo+extensao, arquivo_string+num_arquivo+extensao)

fim = time()
print('\n--------------------------------------------------\n')
print(f'\nTempo de Download das Imagens é de {fim-inicio:.3} Segundos')
print('\n--------------------------------------------------')
