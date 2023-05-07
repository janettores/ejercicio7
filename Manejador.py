from ClaseViajeroFrecuente import ViajeroFrecuente
import csv


class ManejadorViajero:
    __lista: list[ViajeroFrecuente]

    def __init__(self):
        self.__lista = []

    def cargar(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader(archivo, delimiter=",")
        next(reader)
        for fila in reader:
            num = int(fila[0])
            dni = int(fila[1])
            nombre = fila[2]
            apellido = fila[3]
            millas = int(fila[4])
            viaj = ViajeroFrecuente(num, dni, nombre, apellido, millas)
            self.__lista.append(viaj)
        archivo.close()

    def funcion123(self):
        viajero1 = self.__lista[0]
        viajero2 = self.__lista[1]
        viajero3 = self.__lista[2]
        print("Por Izquierda: \n")
        print(" {} == 2500".format(viajero1))
        print(viajero1 == 2500)
        print("Por Derecha: \n")
        print(" 2500 == {}".format(viajero1))
        print(2500 == viajero1)
        print("Comparacion entre Objetos")
        print("{} == {}".format(viajero1, viajero2))
        print(viajero1 == viajero2)
        print("{} == {}".format(viajero2, viajero3))
        print(viajero2 == viajero3)
        viajero1.mostrar()
        viajero1 = 1000 + viajero1
        print("\nSe acumularon nuevas millas, a continuacion se muestra su actualizacion: \n")
        viajero1.mostrar()
        viajero1 = 2500 - viajero1
        print("\nSe canjearon las millas, a continuacion se muestra su actualizacion: \n")
        viajero1.mostrar()