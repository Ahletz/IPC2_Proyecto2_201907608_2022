from PuntosList import *
from TransaccionesList import *
from EscritorioList import *



class Nodo:

    def __init__(self,Id, nombre, abreviatura):
        self.id = Id 
        self.nombre = nombre
        self.abreviatura = abreviatura

        self.siguienteId = None
        self.siguienteNombre = None
        self.siguienteAbreviatura = None

    #obtener datos

    def obtenerId(self):
        return self.id

    def obtenerNombre(self):
        return self.nombre

    def obtenerAbreviatura(self):
        return self.abreviatura

    #obtener siguientes

    def obtenerSiguienteId(self):
        return self.siguienteId

    def obtenerSiguienteNombre(self):
        return self.siguienteNombre

    def obtenerSiguienteAbreviatura(self):
        return self.siguienteAbreviatura

    #asignar nuevos datos

    def asignarDato(self, Id, nombre, abreviatura):
        self.id = Id
        self.nombre = nombre
        self.abreviatura = abreviatura

    def asignarSiguiente(self,nuevoid, nuevonombre, nuevoabreviatura):
        self.siguienteId = nuevoid
        self.siguienteNombre = nuevonombre
        self.siguienteAbreviatura = nuevoabreviatura 

    
class ListaEmpresas:
    
    def __init__(self):
        self.head = None
        self.Puntos = ListaPuntos()
        self.Transacciones = ListaTransacciones()
        self.Escritorios = ListaEscritorios()


    def agregar(self,Id,nombre,abreviatura):
        current = Nodo(Id,nombre,abreviatura)
        current.asignarSiguiente(self.head,self.head,self.head)
        self.head = current

    def tamanio(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguienteId()

        return contador

    def Mostrar(self):
        actual = self.head
        contador = 1
        while actual != None:
            print(str(contador)+' ID: '+actual.obtenerId()+' NOMBRE: '+actual.obtenerNombre()+' ABREVIATURA: '+actual.obtenerAbreviatura())
            actual = actual.obtenerSiguienteId()
            contador +=1

    def buscar(self,Id):
        actual = self.head
        encontrado = False
        contador = 0
        while actual != None and not encontrado:
            if actual.obtenerId() == Id:
                encontrado = True
            else:
                actual = actual.obtenerSiguienteId()
                contador +=1

        return contador


    def Obtener_id(self, seleccion):

        actual = self.head

        for i in range(seleccion-1):

            actual = actual.obtenerSiguienteId()

        Id_empresa = actual.obtenerId()

        return Id_empresa


    def Eliminar(self,Id):
        actual = self.head
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDatoId() == Id:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguienteId()

        if previo == None:
            self.head = actual.obtenerSiguienteId()
        else:
            previo.asignarSiguiente(actual.obtenerSiguienteId(),actual.obtenerSiguienteNombre(),actual.obtenerSiguienteAbreviatura())
    

    #operacines de la empresa
    def Agregar_Puntos(self, Id, nombre, direccion, id_empresa):

        self.Puntos.agregar(Id, nombre, direccion,id_empresa)
        

    def Agregar_Transacciones(self,Id, nombre, tiempo, id_empresa):

        self.Transacciones.agregar(Id, nombre, tiempo, id_empresa)
    
    def Agregar_Escritorios(self, Id, identificacion, encargado, estado, id_punto, id_empresa):

        self.Escritorios.agregar(Id, identificacion, encargado, estado, id_punto, id_empresa)


    def Mostrar_puntos(self, id_empresa):

        self.Puntos.Mostrar_puntos(id_empresa)    


    def Obtener_id_punto(self, numero, id_empresa):

        id_punto = self.Puntos.Obtener_id(numero, id_empresa)

        return id_punto


    def Activar_Escritorio(self, Id, id_punto, id_empresa):

        self.Escritorios.Acrivar_escritorios(Id, id_punto, id_empresa)


    def Mostrar_escritorios(self, id_empresa, id_punto):

        self.Escritorios.Mostrar_escritorios(id_empresa, id_punto)

    def Mostrar_todos_escritorios(self):

        self.Escritorios.Mostrar()


    


        
