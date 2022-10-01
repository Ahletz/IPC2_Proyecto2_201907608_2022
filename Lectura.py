
import xml.etree.ElementTree as ET
from EmpresaList import *
from ClienstesList import *

class Lecturas:

    def __init__(self):

        self.Empresa = ListaEmpresas()
        self.Cliente = ListaClientes()

    def Lectura_Empresa(self):


        tree = ET.parse('Xml1.xml') #abrir xml

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

                self.Empresa.Agregar_Puntos(id_punto,Nombre_punto,Direccion_punto,Id_empresa) #agregar los puntos

                escritorios = j.find('listaEscritorios') #lista de escritorios

                for k in escritorios.findall('escritorio'):

                    id_escritorio = k.attrib.get('id') #id escritorio
                    identificacion = k.find('identificacion').text #identificacion escritorio
                    encargado_escritorio = k.find('encargado').text #encargado escritorio

                    Estado = 'Inactivo' #estado de todos los escritorios

                    self.Empresa.Agregar_Escritorios(id_escritorio, identificacion, encargado_escritorio, Estado, id_punto,Id_empresa) #agregar los escritorios

           
            print()

            transacciones = i.find('listaTransacciones') #lista de transacciones

            for l in transacciones.findall('transaccion'):

                Id_transaccion = l.attrib.get('id') #id transaccion
                Nombre_transaccion = l.find('nombre').text #nombre transaccion
                Tiempo = l.find('tiempoAtencion').text #tiempo transaccion

                self.Empresa.Agregar_Transacciones(Id_transaccion, Nombre_transaccion,Tiempo, Id_empresa )

        
        self.Empresa.Mostrar_Empresa()


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
            self.Empresa.Agregar_Puntos(id_punto,Nombre_punto,Direccion_punto,Id_empresa) #agregar los puntos


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
                self.Empresa.Agregar_Escritorios(id_escritorio, identificacion, encargado_escritorio, Estado, id_punto,Id_empresa) #agregar los escritorios

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
            self.Empresa.Agregar_Transacciones(Id_transaccion, Nombre_transaccion,Tiempo, Id_empresa )

        print()
        print('||------------------DATOS AGREGADOS CON EXITO!------------------||')
        print()
            
    def Lectura_config(self):

        print('------------------------------------------------------------------')

        tree = ET.parse('Xml2.xml') #abrir xml

        root = tree.getroot() #obtener xml

        for i in root.findall('configInicial'):

            print('\t'+'ID CONFIGURACION: '+i.attrib.get('id')) #id configuracion inicial
            print('\t'+'ID DE LA EMPRESA: '+i.attrib.get('idEmpresa')) #id empresa
            print('\t'+'ID PUNTO: '+i.attrib.get('idPunto')) #id punto

            activos = i.find('escritoriosActivos')

            for j in activos.findall('escritorio'):
                
                print('ID ESCRITORIO: '+j.attrib.get('idEscritorio')) #id escritorio activo

            clientes = i.find('listadoClientes') #listado de clientes

            for k in clientes.findall('cliente'):

                dpi = k.attrib.get('dpi') #dpi cliente
                cliente = k.find('nombre').text #nombre cliente

                self.Cliente.agregar(dpi,cliente) #agregar cliente

                transacciones = k.find('listadoTransacciones') #lista de transacciones

                for l in transacciones.findall('transaccion'):

                    Id = l.attrib.get('idTransaccion') #id transaccion
                    cantidad = l.attrib.get('cantidad') #cantidad de transacciones

                    self.Cliente.Agreagar_Transacciones_clientes(Id, cantidad, dpi)

        self.Cliente.Mostrar_clientes()




                





















            





