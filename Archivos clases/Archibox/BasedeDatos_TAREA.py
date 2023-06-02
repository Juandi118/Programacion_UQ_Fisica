import pandas as pd
import numpy as np

""" Se usa la base de datos de cancer de pulmón descargada en Kaggle, misma base de Datos de 
    Sebastián Rivera """"

class TratamientoDatos:
    def __init__(self):
        pass

    def leer(self):
        return pd.read_csv("survey_lung_cancer.csv", sep=",")

    def tabla(self):
        mensaje_1 = "Hola usuario, esta es una base de datos sobre el CANCER DE PULMÓN"
        return mensaje_1, self.leer()

    def info(self):
        mensaje_2 = "Estas son las columnas y el tipo de datos que contienen:"
        print(mensaje_2)
        return self.leer().info()

    def cols_num(self):
        columnas_num = self.leer().select_dtypes(include=[int, float]).columns.tolist()
        for i, columna in enumerate(columnas_num):
            print(i + 1, columna)
        indice_seleccionado = int(input("Seleccione el índice de la columna: ")) - 1
        return self.leer()[columnas_num[indice_seleccionado]]

    def cols_str(self):
        columnas_str = self.leer().select_dtypes(include=[object]).columns.tolist()
        for i, columna in enumerate(columnas_str):
            print(i + 1, columna)
        indice_seleccionado = int(input("Seleccione el índice de la columna: ")) - 1
        return self.leer()[columnas_str[indice_seleccionado]]

    def datos_unicos(self):
        return np.sort(pd.unique(self.cols_num()))

    def filtro(self):
        for i, dato in enumerate(self.datos_unicos()):
            print(dato)
        dato_seleccionado = eval(input("Seleccione un dato: "))
        return self.leer().loc[self.cols_num() == dato_seleccionado]

x = TratamientoDatos()
print(x.filtro())
