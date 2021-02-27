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
               'title': None,
               'cannel_title': None,
               'trending_date': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'category': None}
    catalog['videos'] = lt.newList()
    catalog['title'] = lt.newList("ARRAY_LIST",
                                    cmpfunction=None)
    catalog['trending_date'] = lt.newList("ARRAY_LIST",
                                    cmpfunction=None)
    catalog['country'] = lt.newList("ARRAY_LIST",
                                    cmpfunction=None)
    catalog['views'] = lt.newList("ARRAY_LIST",
                                    cmpfunction=None)
    catalog['likes'] = lt.newList("ARRAY_LIST",
                                    cmpfunction=None)
    catalog['dislikes'] = lt.newList("ARRAY_LIST",
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
    catalog = {'videos': None,
               'title': None,
               'cannel_title': None,
               'trending_date': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'id_category': None}
    catalog['videos'] = lt.newList()
    catalog['title'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['channel_title'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['trending_date'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['country'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['views'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['likes'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['dislikes'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=None)
    catalog['category'] = lt.newList()
# Funciones para agregar informacion al catalogo
def addVideo(catalog, videos):
    # Se adiciona el video a la lista de videos
    print(videos)
    print("")
    print(catalog['videos'])
    lt.addLast(catalog['videos'], videos)
    title = videos['channel_title'].split(",")
    for title_video in title:
        addVideoChannel(catalog, channel_title.strip(), videos)

def addVideoChannel(catalog, channel_title, videos):
    
    """
    Adiciona un canal a lista de canales, la cual guarda referencias
    a los videos de dicho canal
    """
    video_channels = catalog['channel_title']
    posvideo = lt.isPresent(video_channels, channel_title)
    if posvideo > 0:
        video_channel = lt.getElement(video_channels, posvideo)
    else:
        video_channel = newVideoTitle(channel_title)
        lt.addLast(video_channels, video_channel)
    lt.addLast(video_channel['videos'], videos)

# Funciones para creacion de datos
def newChannelTitle(channel_name):
    channel_list = {'channel_title': "", "videos": None,  "views": 0}
    channel_list['channel_title'] = channel_name
    author['videos'] = lt.newList('ARRAY_LIST')
    return channel_list

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
# def cmpVideosByViews(videos1, videos2):
#     if int(video1['videos']['elements'][0]['views']) < int(video2['videos']['elements'][0]['views']):
#         return 1
#     else:
#         return 0