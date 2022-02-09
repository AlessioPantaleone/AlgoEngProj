import random
import statistics
from random import randrange

def heapSort(array):
    n = len(array)

    # Costruisco un heap in formato di massimo alla radice
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    # Estraggo la radice e fixo l'heap
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        # Faccio Heapify sull radice
        heapify(array, i, 0)


def heapify(array, n, i):
    # Trovo il valore maggiore tra radice, figlio destro e sinistro
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


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def quickSort(arr, low=0, high="Unset", pivotposition="high"):
    if high == "Unset":
        high = len(arr) - 1
    if len(arr) == 1:
        return arr
    if low < high:
        pi = quickpartition(arr, low, high, pivotposition)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def quickpartition(arr, low, high, pivotposition="high"):

    i = (low - 1)
    if pivotposition == "high":
        pivot = arr[high]  # Ricorda di cambiare questo in caso di modifica scelta del pivot o di aggiungerlo in config
    if pivotposition == "low":
        pivot = arr[low-1]  # Ricorda di cambiare questo in caso di modifica scelta del pivot o di aggiungerlo in config
        arr[low-1], arr[high] = arr[high], arr[low-1]
    if pivotposition == "random":
        ran = randrange(start=low-1, stop=high+1)
        pivot = arr[ran]  # Ricorda di cambiare questo in caso di modifica scelta del pivot o di aggiungerlo in config
        arr[ran], arr[high] = arr[high], arr[ran]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1