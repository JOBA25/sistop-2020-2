from threading import RLock, Thread #RLock usado en caso de usar .acquiare por segunda vez desde el mismo hilo
from time import sleep

# Modulos propios ->Carpeta modulo
from modulos.agencia import agencia
from modulos.compania import compania
from modulos.cliente import cliente


if __name__ == "__main__":


    lock = RLock()
    lock.acquire()
    lock.release()

    hilosList = []
    clienteList = []
    companiaList = []
    agenciaList = []

    #Compañias de vuelo
    aereomar = compania('Aeromar')
    aereomexico = compania('Aereomexico')
    interjet = compania('InterJet')
    volaris = compania('volaris')
    companiaList = [aereomar,aereomexico,interjet,volaris]

    #Agencias de vuelo
    coppel = agencia(companiaList,'coppelViajes')
    despegar = agencia(companiaList, 'despegar.com')
    mundo  = agencia(companiaList, "mundomex")
    best = agencia(companiaList, 'bestday')
    palacio = agencia(companiaList, 'viajesPalacio')
    agenciaList = [coppel,despegar,mundo,best,palacio]

    for agencias in agenciaList:
        agencias.run()

    sleep(2)

    # creando clientes y corriendo los hilos correspondientes
    #No poner menos de 4 clientes pues nunca se venderían todos los asientos
    for i in range(6):
        clienteList.append( cliente(agenciaList))
        hilosList.append(Thread(target=clienteList[i].run).start())