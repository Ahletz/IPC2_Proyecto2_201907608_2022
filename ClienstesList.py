from TransaccionesClientList import *

class Nodo:

    def __init__(self,Dpi, nombre):
        self.Dpi = Dpi 
        self.nombre = nombre

        self.siguienteDpi = None
        self.siguienteNombre = None

    #obtener datos

    def obtenerDpi(self):
        return self.Dpi

    def obtenerNombre(self):
        return self.nombre

    #obtener siguientes

    def obtenerSiguienteDpi(self):
        return self.siguienteDpi

    def obtenerSiguienteNombre(self):
        return self.siguienteNombre

    #asignar nuevos datos

    def asignarDato(self, Dpi, nombre):
        self.Dpi = Dpi
        self.nombre = nombre

    def asignarSiguiente(self,nuevoDpi, nuevonombre):
        self.siguienteDpi = nuevoDpi
        self.siguienteNombre = nuevonombre

    
class ListaClientes:

    def __init__(self):
        self.head = None
        self.Tranx = ListaclientTransacciones()

    def agregar(self,Dpi,nombre):
        current = Nodo(Dpi,nombre)
        current.asignarSiguiente(self.head,self.head)
        self.head = current

    def tamanio(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguienteDpi()

        return contador

    def Mostrar(self):
        actual = self.head
        while actual != None:
            print(actual.obtenerDpi()+actual.obtenerNombre())
            actual = actual.obtenerSiguienteDpi()

    def buscar(self,Dpi):
        actual = self.head
        encontrado = False
        contador = 0
        while actual != None and not encontrado:
            if actual.obtenerDpi() == Dpi:
                encontrado = True
            else:
                actual = actual.obtenerSiguienteDpi()
                contador +=1

        return contador

    def Eliminar(self,Dpi):
        actual = self.head
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDatoDpi() == Dpi:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguienteDpi()

        if previo == None:
            self.head = actual.obtenerSiguienteDpi()
        else:
            previo.asignarSiguiente(actual.obtenerSiguienteDpi(),actual.obtenerSiguienteNombre())

    def Agreagar_Transacciones_clientes(self,Id,cantidad, dpi):

        self.Tranx.agregar(Id,cantidad, dpi)

    def Mostrar_clientes(self):

        self.Mostrar()
        print()
        self.Tranx.Mostrar()
