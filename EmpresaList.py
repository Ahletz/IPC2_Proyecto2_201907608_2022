



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
        return self.siguiente

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
        while actual != None:
            print(actual.obtenerId()+actual.obtenerNombre()+actual.obtenerAbreviatura())
            actual = actual.obtenerSiguienteId()

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
    


