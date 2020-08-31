"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv

from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt

from time import process_time 



def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Mejores peliculas de un director")
    print("3- Ranking de peliculas(personalizado)")
    print("4- Conocer un director")
    print("5- Conocer un actor")
    print("6- Entender un genero")
    print("7- Crear ranking por genero(personalizado)")
    print("0- Salir")




def compareRecordIds (recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return -1



def loadCSVFile (file, cmpfunction):
    lst=lt.newList("ARRAY_LIST", cmpfunction)
    dialect = csv.excel()
    dialect.delimiter=";"
    try:
        # cf.data_dir
        with open("C:/Users/Jacob Hall/Desktop/2020-20/ISIS 1225/Reto1/Reto1_202020_template/Data/"+file,"r", encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row: 
                lt.addLast(lst,elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


def loadMovies ():
    SinD = loadCSVFile("theMoviesdb/SmallMoviesDetailsCleaned.csv",compareRecordIds)
    ConD = loadCSVFile("theMoviesdb/MoviesCastingRaw-small.csv",compareRecordIds)
    #ConD = loadCSVFile("theMoviesdb/AllMoviesCastingRaw.csv",compareRecordIds)
    #SinD = loadCSVFile("theMoviesdb/AllMoviesDetailsCleaned.csv",compareRecordIds)
    print("Datos cargados, " + str(lt.size(SinD)) + " elementos cargados con "+str(lt.size(ConD))+" elementos complementarios")
    return [SinD,ConD]

def info(list):
    lawiki=lt.newList()
    for peliSD in loadMovies()[0]:
        for peliCD in loadMovies()[1]:
            if peliSD[1]==peliCD[1]:
                pel={'id':peliSD[1],'average':peliSD[7],'count':peliSD[9],'genre':peliSD[2],
                'director':peliCD[2],'actor1':[peliCD[1]],'actor2':peliCD[3],
                'actor3':peliCD[5],'actor4':peliCD[7],'actor5':peliCD[9]}
                lt.addLast(lawiki,pel)
                
    return lawiki
                

def mejorespelisD(director,list):
    best=lt.newList()
    promedio=0
    for eta in info(loadMovies):
        if str(eta['director'])==str(director):
            if eta['average']>=6:
                lt.addLast(best,eta)
            else:
                promedio+=eta['average']
    return ("Sus mejores pelis: "+str(best)+"\n Total de mejores pelis: "+str(len(best))+
            "\n Promedio de las mejores: "+str(promedio/len(best)))


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """


    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:

            if int(inputs[0])==1: #Carga de pelis
                lstmovies = loadMovies()
                return lstmovies
            elif int(inputs[0])==2: #Mejores pelis de X
                return mejorespelisD(input("Quiero mirar las mejores pelis de "),info(loadMovies))

            elif int(inputs[0])==3: #Ranking de pelis personalizado
                pass

            elif int(inputs[0])==4: #Info de X
                pass

            elif int(inputs[0])==5: #Info de Y
                pass

            elif int(inputs[0])==6: #Info de un genero
                pass
            elif int(inputs[0])==7:#Ranking de genero personalizado
                pass
            elif int(inputs[0]==9):
                return info(loadMovies)

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()