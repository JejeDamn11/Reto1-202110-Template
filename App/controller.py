﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
    #Inicia el catálogo de videos en Array
def initCatalogArray():
    catalog = model.newCatalog_Array()
    return catalog
    #Inicia el catálogod de videos en Linked list
def initCatalogLinked():
    catalog = model.newCatalog_Linked()
    return catalog
# Funciones para la carga de datos
def Load_Data(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    LoadVideos(catalog)

def LoadVideos(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for videos in input_file:
        model.addVideo(catalog,videos)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
