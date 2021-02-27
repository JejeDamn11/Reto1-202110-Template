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
    catalog = {'title': None,
               'cannel_title': None,
               'trending_date': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'category': None}
    catalog['title'] = lt.newList()
    catalog['channel_title'] = lt.newList(ARRAY_LIST,
                                    cmpfunction=None)
    catalog['trending_date'] = lt.newList(ARRAY_LIST,
                                    cmpfunction=None)
    catalog['country'] = lt.newList(ARRAY_LIST,
                                    cmpfunction=None)
    catalog['views'] = lt.newList(ARRAY_LIST,
                                    cmpfunction=None)
    catalog['likes'] = lt.newList(ARRAY_LIST,
                                    cmpfunction=None)
    catalog['dislikes'] = lt.newList(ARRAY_LIST,
                                    cmpfunction=None)
    catalog['category'] = lt.newList()
#Construcción modelo linked
def newCatalog_Linked():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los canales,
    una lista vacia para la fecha de tendencia, el país, las visitas, los likes, 
    los dislikes y adicionalmente el id de la categoría.
    . Retorna el catalogo inicializado.
    """
    catalog = {'title': None,
               'cannel_title': None,
               'trending_date': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'id_category': None}
    catalog['title'] = lt.newList()
    catalog['channel_title'] = lt.newList(SINGLE_LINKED,
                                    cmpfunction=None)
    catalog['trending_date'] = lt.newList(SINGLE_LINKED,
                                    cmpfunction=None)
    catalog['country'] = lt.newList(SINGLE_LINKED,
                                    cmpfunction=None)
    catalog['views'] = lt.newList(SINGLE_LINKED,
                                    cmpfunction=None)
    catalog['likes'] = lt.newList(SINGLE_LINKED,
                                    cmpfunction=None)
    catalog['dislikes'] = lt.newList(SINGLE_LINKED,
                                    cmpfunction=None)
    catalog['category'] = lt.newList()
# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['title'], videos)
    title = videos['title'].split(",")
    for title_video in title:
        addVideoTitle(catalog, title_video.strip(), videos)

def addVideoTitle(catalog, title, videos):
    
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    video_list = catalog['title']
    posvideo = lt.isPresent(video_list, title)
    if posvideo > 0:
        author = lt.getElement(video_list, posvideo)
    else:
        video_list = newVideoTitle(title)
        lt.addLast(video_list, author)
    lt.addLast(video_list['title'], videos)

def newVideoTitle(title1):
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('ARRAY_LIST')
    return author
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento