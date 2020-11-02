#
# @author Felipe Yamane
#


from wget import download #Import apenas da função de download da biblioteca wget
from time import time #Import apenas da função time da biblioteca time que será usado para calcular tempo de download
from threading import Thread
from threading import active_count



endereco = 'http://arquivos.afonsomiguel.com/' #String com o endereço de hospedagem dos arquivos na web
num_arquivo = '' #String que será iterada com o número do arquivo sequêncial #estensão do arquivo
arquivo = ''


inicio = time() #Variável que armazena o tempo inicial da execução


def download_img(arquivo):
    download(f'{endereco}arquivo_{arquivo}.jpg', f'arquivo_{arquivo}.jpg')
    print('arquivo...')

for i in range(0,10):
    num_arquivo = str(i)
    arquivo = (f'arquivo_{i}.jpg')
    Thread(target=download_img, args=[i]).start()


while True:
    if active_count() < 2:
        fim = time() #Variável que armazena o tempo final da execução
        print('\n--------------------------------------------------\n')
        print(f'\nTempo de Download das {i+1} Imagens foi de {fim-inicio:.3} Segundos') #Impressão do tempo total de execução
        print('\n--------------------------------------------------')
        break
