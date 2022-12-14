

class Nodo:

    def __init__(self,Id, nombre, tiempo, Id_empresa):
        self.id = Id 
        self.nombre = nombre 
        self.tiempo = tiempo
        self.id_empresa = Id_empresa

        self.siguienteId = None
        self.siguienteNombre = None
        self.siguienteTiempo = None
        self.siguienteId_empresa = None

    #obtener datos

    def obtenerId(self):
        return self.id

    def obtenerNombre(self):
        return self.nombre
    
    def obtenerTiempo(self):
        return self.tiempo

    def obtenerId_Empresa(self):
        return self.id_empresa

    #obtener siguientes

    def obtenerSiguienteId(self):
        return self.siguienteId

    def obtenerSiguienteNombre(self):
        return self.siguienteNombre
    
    def obtenerSiguienteTiempo(self):
        return self.siguienteTiempo

    def obtenerSiguienteId_empresa(self):
        return self.siguienteId_empresa

    #asignar nuevos datos

    def asignarDato(self, Id, nombre, tiempo, Id_empresa):
        self.id = Id 
        self.nombre = nombre 
        self.tiempo = tiempo
        self.id_empresa = Id_empresa


    def asignarSiguiente(self,nuevoid, nuevoNombre, nuevoTiempo, nuevoId_empresa):
        self.siguienteId = nuevoid
        self.siguienteNombre = nuevoNombre
        self.siguienteTiempo = nuevoTiempo
        self.siguienteId_empresa = nuevoId_empresa 

    
class ListaTransacciones:

    def __init__(self):
        self.head = None

    def agregar(self,Id, nombre, tiempo, id_empresa):
        current = Nodo(Id, nombre, tiempo, id_empresa)
        current.asignarSiguiente(self.head, self.head, self.head, self.head)
        self.head = current

    def tamanio(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguienteId()

        return contador

    def Mostrar_Transacciones(self, id_empresa):
        actual = self.head
        contador = 0
        while actual != None:
            if actual.obtenerId_Empresa() == id_empresa:
                contador +=1
                print(str(contador)+'. ID: '+actual.obtenerId()+' NOMBRE: '+actual.obtenerNombre()+' TIEMPO: '+actual.obtenerTiempo())
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
            previo.asignarSiguiente(actual.obtenerSiguienteId(),actual.obtenerSiguienteNombre(),actual.obtenerSiguienteTiempo(), actual.obtenerSiguienteId_empresa())
    

    def Tiempo_promedio(self,id_empresa):

        actual = self.head
        contador = 0
        tiempo = 0

        while actual != None:

            if actual.obtenerId_Empresa() == id_empresa: #contar cantidad de transacciones disponibles en la empresa

                contador +=1
                tiempo += float(actual.tiempo)

            actual = actual.obtenerSiguienteId()

        promedio = tiempo/contador

        print()
        print('||-------------------TIEMPO PROMEDIO ATENCION-------------------||')
        print('TIEMPO PROMEDIO: '+str(promedio))
        print()


    def Tiempo_maximo(self, id_empresa):

        actual = self.head
        tiempo = 0

        tiempo = float(actual.tiempo)

        actual.obtenerSiguienteId()

        while actual != None:

            if actual.obtenerId_Empresa() == id_empresa: #obtener el mayor tiempo de atencion

                if float(actual.obtenerTiempo()) > tiempo:

                    tiempo = float(actual.tiempo)

            actual = actual.obtenerSiguienteId()


        print()
        print('||------------------TIEMPO MAXIMO DE ATENCION-------------------||')
        print('TIEMPO MAXIMO: '+str(tiempo))
        print()


    def Tiempo_minimo(self, id_empresa):

        actual = self.head
        tiempo = 0

        tiempo = float(actual.tiempo)

        actual.obtenerSiguienteId()

        while actual != None:

            if actual.obtenerId_Empresa() == id_empresa: #obtener el mayor tiempo de atencion

                if float(actual.obtenerTiempo()) < tiempo:

                    tiempo = float(actual.tiempo)

            actual = actual.obtenerSiguienteId()


        print()
        print('||-------------------TIEMPO MINIMO DE ATENCION-------------------||')
        print('TIEMPO MINIMO: '+str(tiempo))
        print()


    def Obtener_id(self, id_empresa, seleccion):

        actual = self.head

        contador = 0

        while actual != None:

            if actual.obtenerId_Empresa() == id_empresa:

                contador +=1

                if seleccion == contador:

                    id_transaccion = actual.id

            actual = actual.obtenerSiguienteId()

        print('|| '+id_transaccion+' ||')

        return id_transaccion


    def Obtener_tiempo(self, id_empresa, id_transaccion):


        actual = self.head
        tiempo = 0

        while actual != None:

            if actual.obtenerId_Empresa() == id_empresa and actual.obtenerId() == id_transaccion:

                tiempo = actual.tiempo

            actual = actual.obtenerSiguienteId()

        return tiempo


        
        



        



        