from pydoc import cli
import xml.etree.ElementTree as ET
from EmpresaList import *
from ClienstesList import *

class Lecturas:

    def Lectura_Empresa(self):


        tree = ET.parse('Xml1.xml') #abrir xml

        root = tree.getroot() #obtener xml

        self.Empresa = ListaEmpresas()




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




    def Lectura_config(self):

        print('------------------------------------------------------------------')

        tree = ET.parse('Xml2.xml') #abrir xml

        root = tree.getroot() #obtener xml

        self.Cliente = ListaClientes()

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




                





















            





