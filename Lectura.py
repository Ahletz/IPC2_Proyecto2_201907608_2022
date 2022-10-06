
import xml.etree.ElementTree as ET
from EmpresaList import *
from PuntosList import *
from EscritorioList import *
from ClienstesList import *
from TransaccionesList import *
from TransaccionesClientList import*
from AtenderList import *

class Lecturas:

    def __init__(self):

        self.Empresa = ListaEmpresas()
        self.Punto = ListaPuntos()
        self.Escritorios = ListaEscritorios()
        self.Cliente = ListaClientes()
        self.Transacciones = ListaTransacciones()
        self.ClientesTransacciones = ListaclientTransacciones()
        self.Atencion = ListaAtenciones()

    def Lectura_Empresa(self, direccion):


        tree = ET.parse(direccion) #abrir xml

        root = tree.getroot() #obtener xml


        for i in root.findall('empresa'):

            Id_empresa = i.attrib.get('id') #id empresa
            Nombre_empresa = i.find('nombre').text #nombre empres
            Codigo_empresa = i.find('abreviatura').text #codigo de la empresa

            self.Empresa.agregar(Id_empresa, Nombre_empresa, Codigo_empresa) #agregar la empresa

            
            puntos = i.find('listaPuntosAtencion') #lista de puntos de atencion

            for j in puntos.findall('puntoAtencion'): #ciclo para encontrar todos los puntos de atencion

                id_punto = j.attrib.get('id') #id punto de atencion 
                Nombre_punto = j.find('nombre').text #nombre punto
                Direccion_punto = j.find('direccion').text #direccion

                self.Punto.agregar(id_punto,Nombre_punto,Direccion_punto,Id_empresa) #agregar los puntos

                escritorios = j.find('listaEscritorios') #lista de escritorios

                for k in escritorios.findall('escritorio'):

                    id_escritorio = k.attrib.get('id') #id escritorio
                    identificacion = k.find('identificacion').text #identificacion escritorio
                    encargado_escritorio = k.find('encargado').text #encargado escritorio

                    Estado = 'Inactivo' #estado de todos los escritorios

                    self.Escritorios.agregar(id_escritorio, identificacion, encargado_escritorio, Estado, id_punto,Id_empresa) #agregar los escritorios

           
            print()

            transacciones = i.find('listaTransacciones') #lista de transacciones

            for l in transacciones.findall('transaccion'):

                Id_transaccion = l.attrib.get('id') #id transaccion
                Nombre_transaccion = l.find('nombre').text #nombre transaccion
                Tiempo = l.find('tiempoAtencion').text #tiempo transaccion

                self.Transacciones.agregar(Id_transaccion, Nombre_transaccion,Tiempo, Id_empresa )

        print()
        print('|| DATOS AGREGADOR CORRECTAMENTE.                               ||')
        print()
        

    def Agregar_empresa(self):

        verificacion = True

        print('------------------------------------------------------------------')
        print('||---------------------------AGREGAR----------------------------||')
        print('------------------------------------------------------------------')
        while verificacion:
            print()
            print('------------------------------------------------------------------')
            print('||------------------------DATOS EMPRESA-------------------------||')
            print('------------------------------------------------------------------')
            print()
            print('|| INGRESE EL ID DE LA EMPRESA:                                 ||')
            print()
            Id_empresa = input()
            print()
            print('|| INGRESE EL NOMBRE DE LA EMPRESA:                             ||')
            print()
            Nombre_empresa = input()
            print()
            print('|| INGRESE EL CODIGO DE LA EMPRESA:                             ||')
            print()
            Codigo_empresa = input()
            print()
            print('|| LOS DATOS INGRESADOS SON CORRECTOS?                          ||')
            print('------------------------------------------------------------------')
            print('ID: '+Id_empresa+' NOMBRE: '+Nombre_empresa+' CODIGO: '+Codigo_empresa)
            print('------------------------------------------------------------------')
            print('||--------------------- 1. SI  -  2. NO ------------------------||')
            quest = input()

            if quest == '1':

                self.Empresa.agregar(Id_empresa, Nombre_empresa, Codigo_empresa) #agregar la empresa
                verificacion = False
                print()

            elif quest == '2':

                print('||----------------INGRESE LOS DATOS CORRECTOS.------------------||')

            else:
                print('||-------------------SU SELEECION NO ES VALIDA------------------||')

        
        print('|| INGRESE LA CANTIDAD DE PUNTOS DISPONIBLES:                   ||')
        print()
        puntos = int(input())
        print()
        for i in range(puntos):
            print()
            print('------------------------------------------------------------------')
            print('||-------------------------DATOS PUNTO--------------------------||')
            print('------------------------------------------------------------------')
            print()
            print('|| INGRESE EL ID DEL PUNTO:                                     ||')
            print()
            id_punto = input()
            print()
            print('|| INGRESE EL NOMBRE DEL PUNTO:                                 ||')
            print()
            Nombre_punto = input()
            print()
            print('|| INGRESE LA DIRECCION DEL PUNTO:                              ||')
            print()
            Direccion_punto = input()
            print()
            print('|| DATOS INGRESADOS                                             ||')
            print('------------------------------------------------------------------')
            print('ID: '+id_punto+' NOMBRE: '+Nombre_punto+' DIRECCION: '+Direccion_punto)
            print('------------------------------------------------------------------')
            print()
            self.Punto.agregar(id_punto,Nombre_punto,Direccion_punto,Id_empresa) #agregar los puntos


            print('|| INGRESE LA CANTIDAD DE ESCRITORIOS DISPONIBLES:              ||')
            print()
            escritorios = int(input())
            print()
            for i in range(escritorios):

                print()
                print('------------------------------------------------------------------')
                print('||----------------------DATOS ESCRITORIO------------------------||')
                print('------------------------------------------------------------------')
                print()
                print('|| INGRESE EL ID DEL ESCRITORIO:                                ||')
                print()
                id_escritorio = input()
                print()
                print('|| INGRESE LA IDENTIFICACION DEL ESCRITORIO:                    ||')
                print()
                identificacion = input()
                print()
                print('|| INGRESE EL NOMBRE DEL ENCARGADO DEL ESCRITORIO:              ||')
                print()
                encargado_escritorio = input()
                print()
                print('|| INGRESE EL ESTADO DEL ESCRITORIO:                            ||')
                print()
                Estado = input()
                print()
                print('|| DATOS INGRESADOS                                             ||')
                print('------------------------------------------------------------------')
                print('ID: '+id_escritorio+' IDENTIFICACION: '+identificacion+' ENCARGADO: '+encargado_escritorio+ ' ESTADO: '+Estado)
                print('------------------------------------------------------------------')
                print()
                self.Escritorios.agregar(id_escritorio, identificacion, encargado_escritorio, Estado, id_punto,Id_empresa) #agregar los escritorios

        print('|| INGRESE LA CANTIDAD DE TRANSACCIONES DISPONIBLES:            ||')
        print()
        puntos = int(input())
        print()
        for i in range(puntos):
            print()
            print('------------------------------------------------------------------')
            print('||---------------------DATOS TRANSACCIONES----------------------||')
            print('------------------------------------------------------------------')
            print()
            print('|| INGRESE EL ID DE LA TRANSACCION:                             ||')
            print()
            Id_transaccion = input()
            print()
            print('|| INGRESE EL NOMBRE DE LA TRANSACCION:                         ||')
            print()
            Nombre_transaccion = input()
            print()
            print('|| INGRESE EL TIEMPO DE LA TRANSACCION:                         ||')
            print()
            Tiempo = input()
            print()
            print('|| DATOS INGRESADOS                                             ||')
            print('------------------------------------------------------------------')
            print('ID: '+Id_transaccion+' NOMBRE: '+Nombre_transaccion+' TIEMPO: '+Tiempo)
            print('------------------------------------------------------------------')
            print()
            self.Transacciones.agregar(Id_transaccion, Nombre_transaccion,Tiempo, Id_empresa )

        print()
        print('||------------------DATOS AGREGADOS CON EXITO!------------------||')
        print()
        self.Escritorios.Mostrar()

        


            
    def Lectura_config(self, direccion):

        print('------------------------------------------------------------------')

        tree = ET.parse(direccion) #abrir xml

        root = tree.getroot() #obtener xml

        for i in root.findall('configInicial'):

            id_configuracion = i.attrib.get('id') #id configuracion inicial
            id_empresa= i.attrib.get('idEmpresa') #id empresa
            id_punto = i.attrib.get('idPunto') #id punto

            activos = i.find('escritoriosActivos')

            for j in activos.findall('escritorio'):
                
                Id_escritorio = j.attrib.get('idEscritorio') #id escritorio activo

                self.Escritorios.Acrivar_escritorios(Id_escritorio, id_punto, id_empresa)

            clientes = i.find('listadoClientes') #listado de clientes

            for k in clientes.findall('cliente'):

                dpi = k.attrib.get('dpi') #dpi cliente
                cliente = k.find('nombre').text #nombre cliente

                self.Cliente.agregar(dpi,cliente, id_empresa, id_punto) #agregar cliente

                transacciones = k.find('listadoTransacciones') #lista de transacciones

                for l in transacciones.findall('transaccion'):

                    Id = l.attrib.get('idTransaccion') #id transaccion
                    cantidad = l.attrib.get('cantidad') #cantidad de transacciones

                    self.ClientesTransacciones.agregar(Id, cantidad, dpi)

            

        print()
        print('|| DATOS AGREGADOR CORRECTAMENTE.                               ||')
        print()

        

    def Solicitud_clientes(self, id_empresa, id_punto):

        

        print()
        print('------------------------------------------------------------------')
        print('||---------------------SOLICITUD ATENCION-----------------------||')
        print('------------------------------------------------------------------')
        print()
        print('|| INGRESE SU NUMERO DE DPI::                                   ||')
        print()
        dpi = input()
        print()
        print('|| INGRESE SU NOMBRE:                                           ||')
        print()
        nombre = input()
        print()
        print('|| DATOS INGRESADOS                                             ||')
        print('------------------------------------------------------------------')
        print('DPI: '+dpi+' NOMBRE: '+nombre)
        print('------------------------------------------------------------------')
        print()
        self.Cliente.agregar(dpi,nombre,id_empresa,id_punto)
        print()
        print('|| INGRESE CANTIDAD DE TRANSACCIONES A REALIZAR:                ||')
        print()
        cantidad = int(input())
        print()
        
        for i in range(cantidad):

            self.Transacciones.Mostrar_Transacciones(id_empresa)

            print()
            print('|| INGRESE LA TRANSACCION QUE DESEA REALIZAR:                   ||')
            print()

            seleccion = int(input())

            id_transaccion = self.Transacciones.Obtener_id(id_empresa, seleccion)

            print()
            print('|| INGRESE LA CANTIDAD DE VECES A REALIZAR LA TRANSACCION:      ||')
            print()

            cantidad = input()

            print()
            print('|| DATOS INGRESADOS                                             ||')
            print('------------------------------------------------------------------')
            print('ID: '+id_transaccion+' CANTIDAD: '+cantidad)
            print('------------------------------------------------------------------')
            print()

            self.ClientesTransacciones.agregar(id_transaccion, cantidad,dpi)


        


    #OPERACIONES CON EMPRESA

    def Mostrar_empresa(self): #mostrar los nombres de la empresa

        self.Empresa.Mostrar()

    def Obtener_id_empresa(self,seleccion): #seleccionar la empresa por medio del id

        Id = self.Empresa.Obtener_id(seleccion)

        return Id


    #OPERACIONES CON PUNTOS

    def Mostrar_puntos(self, id_empresa): #mostrar nombres de la empresa seleccionada

        self.Punto.Mostrar_puntos(id_empresa)


    def Obtener_id_punto(self, seleccion, id_empresa): #seleccionar el punro por medio del id de la empresa

        Id = self.Punto.Obtener_id(seleccion, id_empresa)

        return Id



    #OPERACIONES CON ESCRITORIOS


    def Activar_escritorio_especifico(self, id_punto, id_empresa):

        self.Escritorios.Activar(id_punto, id_empresa)

        print()
        print('||----------------------ESCRITORIO ACTIVADO---------------------||')
        print()

        self.Escritorios.Mostrar_escritorios(id_empresa, id_punto)

    def Desactivar_escritorio_especifico(self, id_punto, id_empresa):

        self.Escritorios.Desactivar(id_punto, id_empresa)

        print()
        print('||--------------------ESCRITORIO DESACTIVADO--------------------||')
        print()

        self.Escritorios.Mostrar_escritorios(id_empresa, id_punto)


    #OPERACIONES CON TRANSACCIONES 

    def Tiempos_atencion(self, id_empresa, id_punto):

        self.Escritorios.Cantidad_activos(id_punto, id_empresa)
        self.Escritorios.Cantidad_inactivos(id_punto, id_empresa)

        self.Transacciones.Tiempo_promedio(id_empresa)
        self.Transacciones.Tiempo_maximo(id_empresa)
        self.Transacciones.Tiempo_minimo(id_empresa)


    #OPERACIONES TRANSACCIONES CLIENTES

    def Atender_cliente(self, id_empresa, id_punto):

        print()
        print('||-------------------ATENDIENDO PRIMER CLIENTE------------------||')
        print()

        dpi = self.Cliente.Obtener_primer_cliente(id_empresa, id_punto)

        nombre = self.Cliente.Obtener_nombre_primer_cliente(id_empresa, id_punto)

        id_escritorio = self.Escritorios.Seleccionar_escritorio(id_empresa, id_punto)

        cantidad_transacciones = self.ClientesTransacciones.Obtener_cantidad_transacciones(dpi)

        tiempo_total = 0
        tiempo_transaccion = 0

        if cantidad_transacciones > 0:

            for i in range(1,cantidad_transacciones):

                #obtener el id de la transaccion y agregar dentro de la lista de atender y obtener el tiempo 

                id_transaccion = self.ClientesTransacciones.Obtener_id_transacciones(dpi,i)

                tiempo = self.Transacciones.Obtener_tiempo(id_empresa, id_transaccion)

                tiempo_transaccion = float(tiempo)

                tiempo_total = tiempo_transaccion * cantidad_transacciones

                


                self.Atencion.agregar(dpi,nombre,id_empresa, id_punto, id_escritorio, id_transaccion, tiempo)


            print()
            print('||------------------DATOS DEL CLIENTE ATENDIDO------------------||')
            print()
            print('|| DPI: '+dpi+' NOMBRE: '+nombre+' CANTIDAD TRANSACCIONES: '+str(cantidad_transacciones)+' TIEMPO TOTAL: '+str(tiempo_total)+' ESCRITORIO DE ATENCION: '+id_escritorio+' ||')
            print()
            print('||------------------SACANDO CLIENTE DE LA FILA------------------||')
            print()

            #eliminar el cliente y las transacciones de las listas
            self.Cliente.Eliminar(dpi)

            for i in range(1,cantidad_transacciones):

                #eliminar todas las transacciones pendientes

                id_transaccion = self.ClientesTransacciones.Obtener_id_transacciones(dpi,i)

                self.ClientesTransacciones.Eliminar(id_transaccion, dpi)

        
        


    #OPERACIONES CLIENTES
        




    


    


                





















            





