"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos Array
def newCatalog_Array():
    catalog = {'videos': None,
               'tagvideos': None,
               'tags': None,
               'categories': None}
    catalog['videos'] = lt.newList()
    catalog['tagvideos'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=None)
    catalog['tags'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=None)
    catalog['categories'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=None)

    return catalog
#Construcción modelo linked
def newCatalog_Linked():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los canales,
    una lista vacia para la fecha de tendencia, el país, las visitas, los likes, 
    los dislikes y adicionalmente el id de la categoría.
    . Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'tagvideos': None,
               'tags': None,
               'categories': None,
               'country': None}
    catalog['videos'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=cmpvideos)
    catalog['tagvideos'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['tags'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['categories'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)

    return catalog
# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], videos)
    country_info = videos['country'].split(",")
    lt.addLast(video[''])

def addVideoCountry(catalog, country_name, videos):
    """
    Adiciona un canal a lista de canales, la cual guarda referencias
    a los videos de dicho canal
    """
    country = catalog['country']
    posvideo = lt.isPresent(country, country_name)
    if posvideo > 0:
        video_country = lt.getElement(country, posvideo)
    else:
        video_country = newVideoCountry(country)
        lt.addLast(country, video_country)
    lt.addLast(video_country['videos'], videos)

# Funciones para creacion de datos
def newVideoCountry(country):
    country_list = {'country': "", "videos": None,  "views": 0}
    country_list['country'] = country
    country_list['videos'] = lt.newList('ARRAY_LIST')
    return country_list

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def cmpvideos(country1, country2):
    if (country1.lower() in country2['country'].lower()):
        return 0
    return -1

# def cmpVideosByViews(videos1, videos2):
#     if int(video1['videos']['elements'][0]['views']) < int(video2['videos']['elements'][0]['views']):
#         return 1
#     else:
#         return 0