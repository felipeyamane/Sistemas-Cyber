#
# @author Felipe Yamane
#


from wget import download #Import apenas da função de download da biblioteca wget
from time import time #Import apenas da função time da biblioteca time que será usado para calcular tempo de download 


endereco = 'http://arquivos.afonsomiguel.com/' #String com o endereço de hospedagem dos arquivos na web
num_arquivo = '' #String que será iterada com o número do arquivo sequêncial


inicio = time() #Variável que armazena o tempo inicial da execução

for i in range(0,10): #Estrutura de repetição para execução do download de todos os arquivos
    num_arquivo = str(i) #Conversão de numero inteiro para string para que na sequência seja concatenado de forma correta
    download(f'{endereco}arquivo_{num_arquivo}.jpg', f'arquivo_{num_arquivo}.jpg')
    print(f'\nBaixando arquivo_{num_arquivo}.jpg .....\n')

fim = time() #Variável que armazena o tempo final da execução
print('\n-----------------------------------------------------\n')
print(f'\nTempo de Download das {i+1} Imagens foi de {fim-inicio:.3} Segundos') #Impressão do tempo total de execução
print('\n-----------------------------------------------------')
