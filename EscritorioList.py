class Nodo:

    def __init__(self,Id, identificacion, encargado, estado, id_punto, Id_empresa):
        self.id = Id 
        self.identificacion = identificacion 
        self.encargado = encargado
        self.estado = estado
        self.id_punto = id_punto
        self.id_empresa = Id_empresa

        self.siguienteId = None
        self.siguienteIdentificacion = None
        self.siguienteEncargado = None
        self.siguienteEstado = None
        self.siguienteId_punto = None
        self.siguienteId_empresa = None

    #obtener datos

    def obtenerId(self):
        return self.id

    def obtenerIdentificacion(self):
        return self.identificacion
    
    def obtenerEncargado(self):
        return self.encargado

    def obtenerEstado(self):
        return self.estado

    def obtenerId_Punto(self):
        return self.id_punto

    def obtenerId_Empresa(self):
        return self.id_empresa

    #obtener siguientes

    def obtenerSiguienteId(self):
        return self.siguienteId

    def obtenerSiguienteIdentificacion(self):
        return self.siguienteIdentificacion
    
    def obtenerSiguienteEncargado(self):
        return self.siguienteEncargado

    def obtenerSiguienteEstado(self):
        return self.siguienteEestado

    def obtenerSiguienteId_punto(self):
        return self.siguienteId_punto

    def obtenerSiguienteId_empresa(self):
        return self.siguienteId_empresa

    #asignar nuevos datos

    def asignarDato(self, Id, identificacion, encargado, estado, Id_punto, Id_empresa):
        self.id = Id 
        self.identificacion = identificacion
        self.encargado = encargado
        self.estado = estado
        self.id_punto = Id_punto
        self.id_empresa = Id_empresa


    def asignarSiguiente(self,nuevoid, nuevaIdentificacion, nuevoEncargado, nuevoestado, nuevoId_punto, nuevoId_empresa):
        self.siguienteId = nuevoid
        self.siguienteIdentificacion = nuevaIdentificacion
        self.siguienteEncargado = nuevoEncargado
        self.siguienteEstado = nuevoestado
        self.siguienteId_punto = nuevoId_punto
        self.siguienteId_empresa = nuevoId_empresa 

    
class ListaEscritorios:

    def __init__(self):
        self.head = None

    def agregar(self,Id, identificacion, encargado, estado, id_punto, id_empresa):
        current = Nodo(Id, identificacion, encargado, estado, id_punto, id_empresa)
        current.asignarSiguiente(self.head, self.head, self.head, self.head, self.head, self.head)
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
            print(actual.obtenerId()+actual.obtenerIdentificacion()+actual.obtenerEncargado(), actual.obtenerEstado())
            actual = actual.obtenerSiguienteId()

    def posicion(self,Id):
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

    def buscar(self,Id):
        actual = self.head
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerId() == Id:
                encontrado = True
            else:
                actual = actual.obtenerSiguienteId()
                

        return encontrado

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
            previo.asignarSiguiente(actual.obtenerSiguienteId(),actual.obtenerSiguienteIdentificacion(),actual.obtenerSiguienteEncargado(), actual.obtenerSiguienteEstado(), actual.obtenerSiguienteId_punto(), actual.obtenerSiguienteId_empresa())
    