from Lectura import *
from tkinter import filedialog

class Acciones:

    def __init__(self) -> None:
        
        self.analisis = Lecturas()
        print()
        print('||------------------------SISTEMA LIMPIO------------------------||')
        print()


    def Abrir_Archivo1(self):

        print('|| ABIENDO ||')

        self.ruta_sistema = filedialog.askopenfilename(title='abrir', initialdir='C:/')

        self.analisis.Lectura_Empresa(self.ruta_sistema)



    def Abrir_Archivo2(self):

        print('|| ABIENDO ||')

        self.ruta_config = filedialog.askopenfilename(title='abrir', initialdir='C:/')

        self.analisis.Lectura_config(self.ruta_config)

    def Crear_empresa(self):

        self.analisis.Agregar_empresa()

    def Seleccion(self):

        print()
        print('||----------------------SELECCION DE DATOS----------------------||')
        print()
        print('|| SELECCIONE UNA EMPRESA:                                      ||')
        print()

        self.analisis.Mostrar_empresa()

        print()

        seleccion = int(input())

        print()

        self.id_empresa=self.analisis.Obtener_id_empresa(seleccion)

        print('|| ID EMPRESA SELECCIONADO: '+self.id_empresa+'                     ||')

        print()

        print('|| SELECCIONE UN PUNTO:                                        ||')
        print()

        self.analisis.Mostrar_puntos(self.id_empresa)

        print()

        seleccion = int(input())

        print()

        self.id_punto=self.analisis.Obtener_id_punto(seleccion, self.id_empresa)

        print('|| ID EMPRESA SELECCIONADO: '+self.id_punto+'                     ||')

        print()

    def Activar_escritorio_especifico(self):

        self.analisis.Activar_escritorio_especifico(self.id_punto, self.id_empresa)


    def Desacrivar_escritorio_esécifico(self):

        self.analisis.Desactivar_escritorio_especifico(self.id_punto, self.id_empresa)

    def Ver_info_punto(self):

        self.analisis.Tiempos_atencion(self.id_empresa, self.id_punto)

    def Solicitud_atencion(self):

        self.analisis.Solicitud_clientes(self.id_empresa, self.id_punto)


    
    
