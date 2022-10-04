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


    
    
