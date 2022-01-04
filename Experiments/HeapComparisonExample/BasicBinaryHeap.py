# Python3 implementation of Min Heap


from heapq import heappush, heappop
import math

# Left, right e heapify sono funzioni custom per la
# generazione di un heap come array prone ad errori

def Left(i):
    return 2 * i + 1;


def Right(i):
    return 2 * i + 2;


def heapify(A, i, n, maxh=True):
    l = Left(i);
    r = Right(i);
    if maxh:
        if l < n and A[l] > A[i]:
            Largest = l
        else:
            Largest = i
        if r < n and A[r] > A[Largest]:
            Largest = r;
        if Largest != i:
            A[i], A[Largest] = A[Largest], A[i]
            heapify(A, Largest, n, maxh);
    else:
        if l < n and A[l] < A[i]:
            Smallest = l
        else:
            Smallest = i
        if r < n and A[r] < A[Smallest]:
            Smallest = r;

        if Smallest != i:
            A[i], A[Smallest] = A[Smallest], A[i]
            heapify(A, Smallest, n, maxh);


def build(A, maxh=True):
    for i in range(math.floor(len(A) / 2), -1, -1):  # for i=n/2 to 0
        # print(i)
        heapify(A, i, len(A), maxh)



heap = []
# Non si fa l'hardcoded input, questo è ovviamente solo un esempio
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

for item in data:
    heappush(heap, item)
print("PYTHON HEAP INPUT", heap)

homemadeheap = data.copy()
print("INPUT", homemadeheap)

build(homemadeheap, True)
print("HOMEMADE MAX HEAP INPUT", homemadeheap)

build(homemadeheap, False)
print("HOMEMADE MIN HEAP INPUT (INPUT MAX)", homemadeheap)

homemadeheap = data.copy()
build(homemadeheap, False)
print("HOMEMADE MIN HEAP INPUT (INPUT ORIGINAL)", homemadeheap)
assert heap == homemadeheap


ordered = []
aux = data.copy()

# HEAPSORT
while heap:
    element = heappop(heap)
    #assert blocca l'esecuzione in caso di falsità
    #alternativamente usare logging oppure try catch
    assert element == min(aux)
    # increases running time of test program (remove during workhorse)
    print("MIN HEAP ELEMENT:", element)
    print("MIN SEARCH ELEMENT:", min(aux))
    aux.remove(element)
    print("REMAINING VECTOR", aux)
    ordered.append(element);

print("SORTED", ordered)




