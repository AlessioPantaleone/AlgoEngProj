"""
@author: Pantaleone
"""

from Imports.myimports import *
from Imports.myfunctions import *

def heapSort(array):
    n = len(array)

    #Costruisco un heap in formato di massimo alla radice
    for i in range(n//2, -1, -1):
        heapify(array, n, i)

    #Estraggo la radice e fixo l'heap
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]

        # Heapify root element
        heapify(array, i, 0)

def heapify(array, n, i):
    # Trovo il valore maggiore tra tutti
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    #  Se la radice non è il valore maggiore, scambio con la radice e continuo a fare heapify
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

#Facciamo un doubling experiment

if __name__ == "main":

    for n in range(50, 500, 50):
        Start= timer()
        array = numpy.random.randint(1000, size=(n))
        heapSort(array)
        print(timer() - Start)
        #print(array)
        print("---------------")