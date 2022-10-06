from turtle import color
from graphviz import Digraph

class Nodo:

    def __init__(self,Dpi, nombre, id_empresa, id_punto, id_escritorio, id_transaccion, tiempo):
        self.Dpi = Dpi 
        self.nombre = nombre
        self.id_empresa = id_empresa
        self.id_punto = id_punto
        self.id_escritorio = id_escritorio
        self.id_transaccion = id_transaccion
        self.tiempo = tiempo

        self.siguienteDpi = None
        self.siguienteNombre = None
        self.siguienteId_empresa = None
        self.siguienteId_punto = None
        self.siguienteId_escritorio = None
        self.siguienteId_transaccion = None
        self.siguienteTiempo = None

    #obtener datos

    def obtenerDpi(self):
        return self.Dpi

    def obtenerNombre(self):
        return self.nombre
    
    def obtenerId_empresa(self):
        return self.id_empresa

    def obtenerId_punto(self):
        return self.id_punto
    
    def obtenerId_escritorio(self):
        return self.id_escritorio

    def obtenerId_transaccion(self):
        return self.id_transaccion

    def obtenerTiempo(self):
        return self.tiempo

    #obtener siguientes

    def obtenerSiguienteDpi(self):
        return self.siguienteDpi

    def obtenerSiguienteNombre(self):
        return self.siguienteNombre

    def obtenerSiguienteId_empresa(self):
        return self.siguienteId_empresa

    def obtenerSiguienteId_punto(self):
        return self.siguienteId_punto

    def obtenerSiguienteId_escritorio(self):
        return self.siguienteId_escritorio

    def obtenerSiguienteId_transaccion(self):
        return self.siguienteId_transaccion

    def obtenerSiguienteTiempo(self):
        return self.siguienteTiempo

    #asignar nuevos datos

    def asignarDato(self, Dpi, nombre, id_empresa, id_punto, id_escritorio, id_transaccion, tiempo):
        self.Dpi = Dpi
        self.nombre = nombre
        self.id_empresa = id_empresa
        self.id_punto = id_punto
        self.id_escritorio = id_escritorio
        self.id_transaccion = id_transaccion
        self.tiempo = tiempo

    def asignarSiguiente(self,nuevoDpi, nuevonombre, nuevoid_empresa, nuevoid_punto, nuevoid_escritorio, nuevoid_transaccion, nuevoTiempo):
        self.siguienteDpi = nuevoDpi
        self.siguienteNombre = nuevonombre
        self.siguienteId_empresa = nuevoid_empresa
        self.siguienteId_punto = nuevoid_punto 
        self.siguienteId_escritorio = nuevoid_escritorio
        self.siguienteId_transaccion = nuevoid_transaccion
        self.siguienteTiempo = nuevoTiempo

    
class ListaAtenciones:

    def __init__(self):
        self.head = None

    def agregar(self,Dpi,nombre, id_empresa, id_punto, id_escritorio, id_transaccion, tiempo):
        current = Nodo(Dpi,nombre,id_empresa, id_punto, id_escritorio, id_transaccion, tiempo)
        current.asignarSiguiente(self.head,self.head,self.head,self.head,self.head,self.head,self.head)
        self.head = current

    def tamanio(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguienteDpi()

        return contador

    def Mostrar(self, id_empresa, id_punto):
        actual = self.head
        while actual != None:
            if actual.obtenerId_empresa() == id_empresa and actual.obtenerId_punto() == id_punto:  
                print('DPI: '+actual.obtenerDpi()+' NOMBRE: '+actual.obtenerNombre()+' ESCRITORIO: '+actual.obtenerId_escritorio()+' TRANSACCION: '+actual.obtenerId_transaccion()+ ' TIEMPO: '+ str(actual.obtenerTiempo()))
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
            previo.asignarSiguiente(actual.obtenerSiguienteDpi(),actual.obtenerSiguienteNombre(),actual.obtenerSiguienteId_empresa(),actual.obtenerSiguienteId_punto(),actual.obtenerSiguienteId_escritorio(),actual.obtenerSiguienteId_transaccion(),actual.obtenerSiguienteTiempo())

    
    def Graficar(self, id_escritorio, id_empresa, id_punto):

        dot = Digraph ( 'COLAs' , filename = 'COLA.dot' , engine = 'dot' , format = 'svg' )
        dot.attr ( rankdir = "LR" )
        dot.node_attr.update ( shape = "box" )
        dot.node_attr [ 'style' ] = "filled"
        
        contador = 0
        
        actual = self.head
        while actual != None:

            dot.node('ESCRITORIO: '+ id_escritorio + 'EMPRESA: '+ id_empresa + 'PUNTO: '+ id_punto,id_escritorio, color='brown')
            
            if actual.obtenerId_escritorio() == id_escritorio and actual.obtenerId_empresa() == id_empresa and actual.obtenerId_punto() == id_punto:
                contador +=1
                dot.node('DPI: '+str(actual.obtenerDpi())+' NOMBRE:'+actual.obtenerNombre()+' TRANSACCION:'+actual.obtenerId_transaccion()+' TIEMPO:'+str(actual.obtenerTiempo()))
            actual = actual.obtenerSiguienteDpi()
        

        for i in range ( 1 , contador ) :
            dot.edge ( str ( i ) , str ( i + 1 ) )
        
        dot.view()