from Lectura import *
from tkinter import filedialog

class Acciones:

    def __init__(self) -> None:
        
        self.analisis = Lecturas()


    def Abrir_Archivo1(self):

        print('|| ABIENDO ||')

        self.ruta_sistema = filedialog.askopenfilename(title='abrir', initialdir='C:/')

        print(self.ruta_sistema)

    def Abrir_Archivo2(self):

        print('|| ABIENDO ||')

        self.ruta_config = filedialog.askopenfilename(title='abrir', initialdir='C:/')

        print(self.ruta_config)

    def Crear_empresa(self):

        self.analisis.Agregar_empresa()


    
