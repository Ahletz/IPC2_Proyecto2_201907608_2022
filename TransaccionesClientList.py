


class Nodo:

    def __init__(self,Id, cantidad, dpi):
        self.id = Id 
        self.cantidad = cantidad
        self.dpi = dpi

        self.siguienteId = None
        self.siguienteCantidad = None
        self.siguienteDpi = None

    #obtener datos

    def obtenerId(self):
        return self.id

    def obtenerCantidad(self):
        return self.cantidad

    def obtenerDpi(self):
        return self.dpi

    #obtener siguientes

    def obtenerSiguienteId(self):
        return self.siguienteId

    def obtenerSiguienteCantidad(self):
        return self.siguienteCantidad

    def obtenerSiguienteDpi(self):
        return self.siguienteDpi

    #asignar nuevos datos

    def asignarDato(self, Id, cantidad, Dpi):
        self.id = Id
        self.cantidad = cantidad
        self.dpi = Dpi

    def asignarSiguiente(self,nuevoid, nuevacantidad, nuevodpi):
        self.siguienteId = nuevoid
        self.siguienteCantidad = nuevacantidad
        self.siguienteDpi = nuevodpi 

    
class ListaclientTransacciones:

    def __init__(self):
        self.head = None

    def agregar(self,Id,cantidad, dpi):
        current = Nodo(Id,cantidad,dpi)
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
            print('ID: '+actual.obtenerId()+' CANTIDAD: '+actual.obtenerCantidad())
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

    def Eliminar(self,Id, dpi):
        actual = self.head
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerId() == Id and actual.obtenerDpi() == dpi:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguienteId()

        if previo == None:
            self.head = actual.obtenerSiguienteId()
        else:
            previo.asignarSiguiente(actual.obtenerSiguienteId(),actual.obtenerSiguienteCantidad(),actual.obtenerSiguienteDpi())



    def Obtener_cantidad_transacciones(self, dpi):

        actual = self.head
        contador = 0

        while actual != None:

            if actual.obtenerDpi() == dpi:

                contador +=1

            actual = actual.obtenerSiguienteDpi()

        return contador

    def Obtener_id_transacciones(self, dpi, no_transaccion):

        actual = self.head
        contador = 0

        while actual != None:

            if actual.obtenerDpi() == dpi:

                contador +=1

            if contador == no_transaccion:

                id_transaccion = actual.id

            actual = actual.obtenerSiguienteDpi()

        return id_transaccion




        
    


