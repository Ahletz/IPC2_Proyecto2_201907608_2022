import xml.etree.ElementTree as ET

class Lecturas:

    def Lectura_Empresa(self):


        tree = ET.parse('Xml1.xml') #abrir xml

        root = tree.getroot() #obtener xml


        for i in root.findall('empresa'):

            Id_empresa = i.attrib.get('id') #id empresa

            print('NOMBRE DE LA EMPRESA: '+i.find('nombre').text) #nombre empres
            print('CODIGO DE LA EMPRESA: '+i.find('abreviatura').text) #codigo de la empresa

            puntos = i.find('listaPuntosAtencion') #lista de puntos de atencion

            for j in puntos.findall('puntoAtencion'): #ciclo para encontrar todos los puntos de atencion

                print('\t'+'ID PUNTO ATENCION: '+j.attrib.get('id')) #id punto de atencion 
                print('\t'+'\t'+'NOMBRE PUNTO DE ATENCION: '+j.find('nombre').text) #nombre empres
                print('\t'+'\t'+'DIRECCION PUNTO DE ATENCION: '+j.find('direccion').text) #codigo de la empresa

                escritorios = j.find('listaEscritorios') #lista de escritorios

                for k in escritorios.findall('escritorio'):

                    print('\t'+'\t'+'\t'+'ID ESCRITORIO: '+k.attrib.get('id')) #id escritorio
                    print('\t'+'\t'+'\t'+'NIDENTIFICACION ESCRITORIO: '+k.find('identificacion').text) #nombre escritorio
                    print('\t'+'\t'+'\t'+'ENCARGADO DE ESCRITORIO: '+k.find('encargado').text) #encargado escritorio

            
            
            
            print()

            transacciones = i.find('listaTransacciones') #lista de transacciones

            for l in transacciones.findall('transaccion'):

                print('\t'+'ID TRANSACCION: '+l.attrib.get('id')) #id transaccion
                print('\t'+'\t'+'NOMBRE TRANSACCION: '+l.find('nombre').text) #nombre transaccion
                print('\t'+'\t'+'TIEMPO ATENCION: '+    l.find('tiempoAtencion').text) #tiempo transaccion


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

                print('\t'+'\t'+'DPI: '+k.attrib.get('dpi')) #dpi cliente
                print('\t'+'\t'+'NOMBRE CLIENTE: '+k.find('nombre').text) #nombre cliente

                transacciones = k.find('listadoTransacciones') #lista de transacciones

                for l in transacciones.findall('transaccion'):

                    print('\t'+'\t'+'\t'+'ID TRANSACCION: '+l.attrib.get('idTransaccion')) #dpi cliente
                    print('\t'+'\t'+'\t'+'MONTO: '+l.attrib.get('cantidad')) #dpi cliente




                





















            





