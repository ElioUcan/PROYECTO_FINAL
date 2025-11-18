'''Título del Proyecto: Sistema de Gestión Académica "StudentTask Manager"


• Descripción General: El proyecto consiste en el diseño y desarrollo de un sistema en
Python para la administración eficiente de una institución educativa. El sistema permitirá
registrar estudiantes, gestionar sus calificaciones, administrar una cola de atención para
servicios escolares y mantener un historial de operaciones. El objetivo es resolver la
necesidad de organizar grandes volúmenes de datos académicos y optimizar el flujo de
atención a los alumnos.'''


class Node:
    def __init__(self,nombre,next,previous):
        self.nombre = nombre
        self.next =next
        self.previous = previous

class NodeAB:
    def __init__(self,matricula,izq,der):
        self.matricula = matricula
        self.izq =izq
        self.der = der

#Se utilizará para indexar las matrículas (ID) de los estudiantes, 
#permitiendo búsquedas de alta velocidad para consultar datos específicos.
class Tree:
    def __init__(self):
        pass

    def _search_recursivo(self):
        pass

    def search(self):
        pass

# Se utilizará para almacenar el registro principal de estudiantes
#activos. Permite una inserción dinámica de nuevos alumnos sin un tamaño fijo predefinido.

class LinkedList:
    def __init__(self):
        pass

#Funcionará como un historial de "Deshacer" (Undo). Almacenará las últimas
#acciones realizadas (ej. agregar un estudiante) para poder revertirlas si hubo un error,
#siguiendo el principio LIFO (Last In, First Out).

class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0
    
    def remove(self):
        if self.isEmpty():
            return False
        else:
            self.list.pop(-1)

    def addAction(self, value):
        self.list.append(value)
    
    def top(self):
        print(self.list[-1])

#Gestionará la "Ventanilla de Atención". Los estudiantes que soliciten
#trámites se formarán en esta estructura bajo el principio FIFO (First In, First Out) para ser
#atendidos en orden.
        
class Queue:
    def __init__(self):
        self.list= []

    def isEmpty(self):
        return len(self.list) == 0

    def remove(self):
        if self.isEmpty():
            return False
        else:
            self.list.pop(0)
        
    def add(self,idAlumno):
        self.list.append(idAlumno)

    def peek(self):
        print(self.list[0])

#Se utilizará para ordenar la lista de estudiantes según su promedio
#general (de mayor a menor) para reportes de honor.
   
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#Se implementará para ordenar alfabéticamente los reportes de
#asistencia o listas de nombres
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp
    return arr


#Menú interactivo en consola que permita navegar entre las distintas estructuras
#(Agregar alumno, Atender cola, Buscar en árbol, Generar reporte ordenado).
def menu():
    print('''Elija una opcion:
(1)Agregar Alumno
(2)Atender Cola
(3)Buscar en Arbol
(4)Generar Reporte ordenado
(5)Salir''')
    return input('')

#Uso de archivos .csv o .txt para cargar y guardar la base de datos de
#estudiantes al iniciar y cerrar el programa.

def data():
    pass


def main():
    while True:
        x = menu()
        match x:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                arr = [2,3,10,5,9]
                print(bubble_sort(arr))
            case '5':
                break

if __name__ == '__main__':
    main()