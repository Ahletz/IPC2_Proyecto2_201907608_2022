

class Nodo:

    def __init__(self,Dpi, nombre, id_empresa, id_punto):
        self.Dpi = Dpi 
        self.nombre = nombre
        self.id_empresa = id_empresa
        self.id_punto = id_punto

        self.siguienteDpi = None
        self.siguienteNombre = None
        self.siguienteId_empresa = None
        self.siguienteId_punto = None

    #obtener datos

    def obtenerDpi(self):
        return self.Dpi

    def obtenerNombre(self):
        return self.nombre
    
    def obtenerId_empresa(self):
        return self.id_empresa

    def obtenerId_punto(self):
        return self.id_punto

    #obtener siguientes

    def obtenerSiguienteDpi(self):
        return self.siguienteDpi

    def obtenerSiguienteNombre(self):
        return self.siguienteNombre

    def obtenerSiguienteId_empresa(self):
        return self.siguienteId_empresa

    def obtenerSiguienteId_punto(self):
        return self.siguienteId_punto

    #asignar nuevos datos

    def asignarDato(self, Dpi, nombre, id_empresa, id_punto):
        self.Dpi = Dpi
        self.nombre = nombre
        self.id_empresa = id_empresa
        self.id_punto = id_punto

    def asignarSiguiente(self,nuevoDpi, nuevonombre, nuevoid_empresa, nuevoid_punto):
        self.siguienteDpi = nuevoDpi
        self.siguienteNombre = nuevonombre
        self.siguienteId_empresa = nuevoid_empresa
        self.siguienteId_punto = nuevoid_punto 

    
class ListaClientes:

    def __init__(self):
        self.head = None

    def agregar(self,Dpi,nombre, id_empresa, id_punto):
        current = Nodo(Dpi,nombre,id_empresa, id_punto)
        current.asignarSiguiente(self.head,self.head,self.head,self.head)
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
            print('DPI: '+actual.obtenerDpi()+' NOMBRE: '+actual.obtenerNombre())
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
            if actual.obtenerDpi() == Dpi:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguienteDpi()

        if previo == None:
            self.head = actual.obtenerSiguienteDpi()
        else:
            previo.asignarSiguiente(actual.obtenerSiguienteDpi(),actual.obtenerSiguienteNombre(),actual.obtenerSiguienteId_empresa(),actual.obtenerSiguienteId_punto())

    

    def Obtener_primer_cliente(self, id_empresa, id_punto):

        actual = self.head
        while actual != None:

            if actual.obtenerId_empresa() == id_empresa and actual.obtenerId_punto() == id_punto:

                dpi = actual.Dpi

            actual = actual.obtenerSiguienteDpi()

        return dpi

    def Obtener_nombre_primer_cliente(self, id_empresa, id_punto):

        actual = self.head
        while actual != None:

            if actual.obtenerId_empresa() == id_empresa and actual.obtenerId_punto() == id_punto:

                name = actual.nombre

            actual = actual.obtenerSiguienteDpi()

        return name


    def Cantidad_clientes(self, id_empresa, id_punto):

        actual = self.head
        contador = 0

        while actual != None:

            if actual.obtenerId_empresa() == id_empresa and actual.obtenerId_punto() == id_punto:

                contador +=1

            actual = actual.obtenerSiguienteDpi()

        return contador


        
        