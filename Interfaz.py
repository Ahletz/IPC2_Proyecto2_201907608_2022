from Config import *
class Menus: 

    def __init__(self):

        self.llamado = Acciones()
        
        print('------------------------------------------------------------------')
        print('||--------------------------BIENVNIDO---------------------------||')
        print('------------------------------------------------------------------')
        print()

    def Menu_principal(self):
        salida = True

        while salida: 
            print('------------------------------------------------------------------')
            print('||-----------------------------MENU-----------------------------||')
            print('------------------------------------------------------------------')

            print('|| SELECCIONE UNA OPCION: --------------------------------------||')
            print('|| 1. CONFIGURACION EMPRESA.                                    ||')
            print('|| 2. SELECCIONE EMPRESA Y PUNTO DE ATENCION.                   ||')
            print('|| 3. MANEJO DE PUNTO DE ATENCION.                              ||')
            print('|| 4. SALIR.                                                    ||')

            print()

            seleccion = input()

            if seleccion == '1':

                self.Menu_configuracion()

            elif seleccion == '2':

                pass

            elif seleccion == '3':

                self.Menu_manejo()

            elif seleccion == '4':

                salida = False
            
            else:
                
                print()
                print('||----------------SU SELEECION NO ES VALIDA----------------||')
                print()

    def Menu_configuracion(self):

        salida = True

        while salida:

            print('------------------------------------------------------------------')
            print('||------------------------CONFIGURACION-------------------------||')
            print('------------------------------------------------------------------')

            print('|| SELECCIONE UNA OPCION: --------------------------------------||')
            print('|| 1. LIMPIAR SISTEMA.                                          ||')
            print('|| 2. CARGAR ARCHIVO CONFIGURACION DE SISTEMA.                  ||')
            print('|| 3. CREAR EMPRESA.                                            ||')
            print('|| 4. CARGAR CONFIGURACION INICIAL DE PRUEBA.                   ||')
            print('|| 5. SALIR.                                                    ||')

            print()

            seleccion = input()

            if seleccion == '1':

                self.llamado = Acciones()

            elif seleccion == '2':

                self.llamado.Abrir_Archivo1()

            elif seleccion == '3':

                self.llamado.Crear_empresa()
            
            elif seleccion == '4':

                self.llamado.Abrir_Archivo2()

            elif seleccion == '5':

                salida = False
            
            else:
                
                print()
                print('||-------------------SU SELEECION NO ES VALIDA------------------||')
                print()

    
    def Menu_manejo(self):

        salida = True

        while salida:

            print('------------------------------------------------------------------')
            print('||-------------------MANEJO PUNTO DE ATENCION-------------------||')
            print('------------------------------------------------------------------')

            print('|| SELECCIONE UNA OPCION: --------------------------------------||')
            print('|| 1. VER PUNTO DE ATENCION.                                    ||')
            print('|| 2. ACTIVAR ESCRITORIO DE SERVICIO.                           ||')
            print('|| 3. DESACTIVAR ESCRITORIO DE SERVICIO.                        ||')
            print('|| 4. ATENDER CLIENTE.                                          ||')
            print('|| 5. SOLICITUD DE ATENCION.                                    ||')
            print('|| 6. SILMULAR PUNTO DE ATENCION.                               ||')
            print('|| 7. SALIR.                                                    ||')

            print()

            seleccion = input()

            if seleccion == '1':

                pass

            elif seleccion == '2':

                pass

            elif seleccion == '3':

                pass

            elif seleccion == '4':

                pass

            elif seleccion == '5':

                pass

            elif seleccion == '6':

                pass

            elif seleccion == '7':

                salida = False
            
            else:
                
                print()
                print('||----------------SU SELEECION NO ES VALIDA----------------||')
                print()











