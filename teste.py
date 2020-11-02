import time
from threading import Thread


# rodando = True


def minhaThreadLegal(msg, t):
    for i in range(10):
        time.sleep(t)
        print(msg)
#       if not rodando:
#           break


t1 = Thread(target=minhaThreadLegal, args=('Oi... Estou aqui também!', 1))
t1.start()

t2 = Thread(target=minhaThreadLegal, args=('Oi... Sou a segunda thread!', 1.5))
t2.start()


while t1.is_alive() or t2.is_alive():
    print('Oi... estou aqui.')
    time.sleep(.5)