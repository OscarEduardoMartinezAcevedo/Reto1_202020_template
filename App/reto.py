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
from Sorting import shellsort as Sh
from time import process_time 


def loadCSVFile (file, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    #lst = lt.newList("LINKED_LIST") #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #ti
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tf
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst
    


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Elementos de la Lista")
    print("3- Elementos filtrados por palabra clave")
    print("4- Info de un director")
    print("5- Top 10 mejores y peores peliculas por votos y calificación")
    print("6- Info de un actor")
    print("7- Peliculas por genero")
    print("8- Top de peliculas por genero")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("No files found")  
        return 0
    else:
        ti = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        tf = process_time() #tiempo final
        print("Ejecución de ",tf-ti," segundos")
    return counter

def countElementsByCriteria(criteria, lst, lst2):
    if lst['size']==0 or lst2["size"]==0:
        print("No files found on list(s)")  
        return 0
    else:
        t1 = process_time()
        Min = []
        calif = 0
        aidi = 0
        a = 1
        total = 0
        while a <= lst2["size"]:
            P = lt.getElement(lst2, a)
            if criteria == P["director_name"]:
                aidi =  P["id"]
                n = 1
                while n <= lst["size"]:
                    Pa = lt.getElement(lst, n)
                    if aidi == Pa["id"]:
                        total +=1
                        ele = {Pa["original_title"]:Pa["vote_average"]}
                        Min.append(ele)
                        calif += float(Pa["vote_average"])
                    n += 1
            a += 1
        if total != 0:
            calif = float(calif)/float(total)
        t2 = process_time()
        x = {"Autor": criteria,
            "Nombre de Peliculas ": total,
            "Calificacion promedio": calif,
            "Peliculas": Min}
        print("Ejecucion en ",t2-t1," segundos")
        if total == 0:
            print("Unkown Author")
        else:
            return x
    
def orderElementsByCriteria(function, column, lst, elements):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    return 0
def high_vote_count(ele1, ele2):
    if int(ele1["vote_count"]) > int(ele2["vote_count"]):
        return True
    return False
def less_vote_count(ele1, ele2):
    if int(ele1["vote_count"]) < int(ele2["vote_count"]):
        return True
    return False

def less_vote_average(ele1, ele2):
    if float(ele1["vote_average"]) < float(ele2["vote_average"]):
        return True
    return False

def high_vote_average(ele1, ele2):
    if float(ele1["vote_average"]) > float(ele2["vote_average"]):
        return True
    return False


def Mejorespelis(lst):
    if lst["size"]==0:
        print("Empy list")
    else:
        ti = process_time()
        Datos1 = []
        Datos2 = []
        ava = lst
        Sh.shellSort(ava, high_vote_count)
        a = 1
        iteava = it.newIterator(ava)
        while it.hasNext(iteava) and a < 11:
            elnex = it.next(iteava)
            S = [elnex["original_title"], elnex["vote_count"]]
            Datos1.append(S)
            a += 1
        llst = lst
        Sh.shellSort(llst, less_vote_average)
        b = 1
        itellst = it.newIterator(llst)
        while it.hasNext(itellst) and b < 6:
            Alta = it.next(itellst)
            N = [Alta["original_title"], Alta["vote_average"]]
            Datos2.append(N)
            b +=1
        tf = process_time()
        x = {"Mejores peliculas(votos)": Datos1,
            "Peores peliculas(promedio)": Datos2}
        print("Ejecucion en ",tf-ti," segundos")
        return x

def infodelauto(lst, lst2, actor):
    if lst["size"] == 0 or lst2["size"]==0:
        print("Empy list(s)")
    else:
        Datos = []
        idPels = []
        directors = {}
        count = 0
        mayor = 0
        name = None
        prom = 0
        A = 1
        ti = process_time()
        while A < 6:
            ite2 = it.newIterator(lst2)
            while it.hasNext(ite2):
                nex2 = it.next(ite2)
                A = str(A)
                if nex2["actor"+A+"_name"] == actor:
                    idPels.append(nex2["id"])
                    count += 1
                    if nex2["director_name"] in directors:
                        directors[nex2["director_name"]] +=1
                    else:
                        directors[nex2["director_name"]] = 1
            A = int(A)
            A += 1
        for elaidi in idPels:
            ite1 = it.newIterator(lst)
            while it.hasNext(ite1):
                ni1 = it.next(ite1)
                if ni1["id"] == elaidi:
                    Datos.append(ni1["original_title"])
                    prom += float(ni1["vote_average"])
        for big in directors:
            if directors[big] > mayor:
                mayor = directors[big]
                name = big
        if prom != 0:
            prom = round(prom/count, 1)
        tf = process_time()
        x = {"Actor": actor,
            "Peliculas": count,
            "Promedio": prom,
            "Director con mayor colaboracion":name,
            "Titulos de las peliculas":Datos}
        print("Ejecucion en ",tf-ti," segundos")
        if count == 0:
            print("No actors found")
        else:
            return x

def peligen(lst, genero):
    if lst["size"] == 0:
        print("Empy list")
    else:
        ti =process_time()
        gen = genero.lower()
        gen = genero.capitalize()
        a =[]
        count = 0
        prom = 0
        ite = it.newIterator(lst)
        while it.hasNext(ite):
            nexi = it.next(ite)
            if gen in nexi["genres"]:
                a.append(nexi["original_title"])
                prom += float(nexi["vote_average"])
                count += 1
        prom = float(prom/count)
        tf = process_time()
        x = {"Genero": gen,
            "Peliculas": count,
            "Promedio votacion": prom,
            "Lista": a}
        if count == 0:
            print("Unknown genre")
        else:
            print("Ejecucion en ",tf-ti," segundos")
            return x

def generank(lst, genero, orden):
    if lst["size"] == 0:
        print("La lista es vacia")
    else:
        ti = process_time()
        gene = genero.capitalize()
        ordelow = orden.lower()
        Datos1 = []
        Datos2 =[]
        count = 10
        PC = 0
        PCV = 0
        laL = lst
        if ordelow == "ascendente":
            Sh.shellSort(laL, high_vote_count)
        elif ordelow == "descendente":
            Sh.shellSort(laL, less_vote_count)
        a = 1
        b = 0
        iteL = it.newIterator(laL)
        while it.hasNext(iteL) and b < 10 and a < laL["size"]:
            nexL = it.next(iteL)
            if gene in nexL["genres"]:
                F = [nexL["original_title"], nexL["vote_count"]]
                Datos1.append(F)
                PCV += float(nexL["vote_count"])
                b += 1
            a += 1

        
        laO = lst
        if ordelow == "ascendente":
            Sh.shellSort(laO, high_vote_average)
        elif orden == "descendente":
            Sh.shellSort(laO, less_vote_average)
        c = 1
        d = 0
        nexO = it.newIterator(laO)
        while it.hasNext(nexO) and d < 10 and c < laO["size"]:
            Alta = it.next(nexO)
            if gene in Alta["genres"]:
                G = [Alta["original_title"], Alta["vote_average"]]
                Datos2.append(G)
                PC += float(Alta["vote_average"])
                d += 1
            c +=1
        
        if not count == 0:
            PC = float(PC/count)
            PCV = float(PCV/count)
            tf = process_time()
        if count == None:
            print("No movie found with genre")
        else:
            x = {"Genero": gene,
                "El top 10 (votos) "+ordelow+" son": Datos1,
                "Cantidad de votos(promedio)": PCV,
                "El top 10 (orden) "+ordelow+" son": Datos2,
                "Calificacion(promedio)": PC}
            print("Ejecucion en ",tf-ti," segundo(s)")
            return x
            


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = lt.newList()   # se require usar lista definida
    lista2 = lt.newList()
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n')
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                #file = input("Escriba el nombre del archivo: ")
                file = input("ingrese el archivo detalles")
                file2 = input("ingrese el archivo casting")
                lista = loadCSVFile(file) #llamar funcion cargar datos
                lista2 = loadCSVFile(file2)
                print("Loaded files, ",lista['size']," elementos cargados")
                print("Loaded files, ",lista2['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                    a = input("Details o Casting?")
                    if a == "Details": 
                        print("Details tiene ",lista["size"]," elementos")#obtener la longitud de la lista
                    elif a == "Casting":
                        print("Casting tiene ",lista2["size"]," elementos")#obtener la longitud de la lista
                    elif a != "lista" and a != "lista2":
                        print("Unknow list. Please write Details or Casting as here.<Translation: Escriba bien.>")
            elif int(inputs[0])==3: #opcion 3
                if lista==None or lista['size']==0 or lista2['size']==0: #obtener la longitud de la lista
                    print("Empy list")
                else:   
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista) #filtrar una columna por criterio  
                    print("Found ",counter," elements related to : ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista==None or lista['size']==0 or lista['size']==0: #obtener la longitud de la lista
                    print("Empy list")
                else:
                    criteria =input('Ingrese el criterio de búsqueda\n')
                    print(countElementsByCriteria(criteria, lista, lista2))
            elif int(inputs[0])==5:
                if lista==None or lista["size"]==0 or lista2['size']==0:
                    print("Empy list")
                else:
                    print(Mejorespelis(lista))
            elif int(inputs[0])==6:
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("Empy list")
                else: 
                    actor = input("Actor a chismear: ")
                    print(infodelauto(lista, lista2, actor))
            elif int(inputs[0])==7:
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("Empy list")
                else: 
                    genero = input("Genero: ")
                    print(peligen(lista, genero))
            elif int(inputs[0])==8:
                if lista==None or lista['size']==0: #obtener la longitud de la lista
                    print("Empy list")
                else: 
                    genero = str(input("Genero: "))
                    orden = input("Sube o baja?(ascendente o descendente): ")
                    if orden=='ascendente' or orden=='descendente':
                        print(generank(lista, genero, orden))
                    else:
                        print("ascendente o descendente mi rey")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
if __name__ == "__main__":
    main()