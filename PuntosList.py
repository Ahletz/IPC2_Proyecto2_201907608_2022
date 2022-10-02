
class Nodo:

    def __init__(self,Id, nombre, direccion, Id_empresa):
        self.id = Id 
        self.nombre = nombre
        self.direccion = direccion
        self.id_empresa = Id_empresa

        self.siguienteId = None
        self.siguienteNombre = None
        self.siguienteDireccion = None
        self.siguienteId_empresa = None

    #obtener datos

    def obtenerId(self):
        return self.id

    def obtenerNombre(self):
        return self.nombre

    def obtenerDireccion(self):
        return self.direccion

    def obtenerId_Empresa(self):
        return self.id_empresa

    #obtener siguientes

    def obtenerSiguienteId(self):
        return self.siguienteId

    def obtenerSiguienteNombre(self):
        return self.siguienteNombre

    def obtenerSiguienteDireccion(self):
        return self.siguienteDireccion

    def obtenerSiguienteId_empresa(self):
        return self.siguienteId_empresa

    #asignar nuevos datos

    def asignarDato(self, Id, nombre, direccion, Id_empresa):
        self.id = Id
        self.nombre = nombre
        self.direccion = direccion
        self.Id_empresa = Id_empresa

    def asignarSiguiente(self,nuevoid, nuevoNombre, nuevaDireccion, nuevoId_empresa):
        self.siguienteId = nuevoid
        self.siguienteNombre = nuevoNombre
        self.siguienteDireccion = nuevaDireccion
        self.siguienteId_empresa = nuevoId_empresa 

    
class ListaPuntos:

    def __init__(self):
        self.head = None

    def agregar(self,Id, nombre, direccion, id_empresa):
        current = Nodo(Id, nombre,direccion, id_empresa)
        current.asignarSiguiente(self.head,self.head,self.head,self.head)
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
            print(actual.obtenerId()+actual.obtenerNombre()+actual.obtenerDireccion())
            actual = actual.obtenerSiguienteId()


    def Mostrar_puntos(self, id_empresa):
        actual = self.head
        contador = 0
        while actual != None:

            if actual.obtenerId_Empresa() == id_empresa:
            
                contador +=1
                print(str(contador)+' ID: '+actual.obtenerId()+' NOMBRE: '+actual.obtenerNombre()+' DIRECCION: '+actual.obtenerDireccion())
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

    def Obtener_id(self, seleccion, id_empresa):

        actual = self.head
        contador = 0

        while actual != None:

            if id_empresa == actual.obtenerId_Empresa():

                contador +=1

            if contador == seleccion and id_empresa == actual.obtenerId_Empresa():

                id_punto = actual.obtenerId()

            actual = actual.obtenerSiguienteId()


        return id_punto

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
            previo.asignarSiguiente(actual.obtenerSiguienteId(),actual.obtenerSiguienteNombre(),actual.obtenerSiguienteDireccion(),actual.obtenerSiguienteId_empresa())
    
