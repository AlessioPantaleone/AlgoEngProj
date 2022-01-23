#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:08:12 2021

@author: luca
"""


import pandas as pd
from heapq import heappush, heappop
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

# Import da file CSV tramite Pandas
df = pd.read_csv("dati.csv", header=None, nrows=1)
datain = df.values.tolist()[0]
print("Dati grezzi:          ", datain)


def inssort(arr):
    for k in range(1, len(arr)):
        x = arr[k]
        for j in range(k-1, -1, -1):
            if(j>0 and arr[j]<=x): break
        if(j<k):
            for t in range(k, j, -1):
                arr[t] = arr[t-1]
            arr[j] = x
    return arr

def partition(arr, i, f):
    p = arr[f]
    while f>=i:
        if(arr[i] > p):
            x = arr[i]
            arr[i] = arr[f]
            arr[f] = x
            f -= 1
        elif arr[i] < p:
            i += 1
        elif arr[f] > p:
            f -= 1
        else:
            x = arr[i]
            arr[i] = arr[f]
            arr[f] = x
            i += 1
    return f              
def quicksort(arr, i, f):
    if(i>=f): return
    m = partition(arr, i, f)
    quicksort(arr, i, m-1)
    quicksort(arr, m+1, f)
    return arr
    
def heapsort(arr):
    heap = []
    for item in arr:
        heappush(heap, item)
    for i in range (len(arr)):
        arr[i] = heappop(heap)
    return arr


aux = datain.copy()
final1 = inssort(aux)

aux = datain.copy()
final2 = quicksort(aux, 0, len(aux)-1)

aux = datain.copy()
final3 = heapsort(aux)

del aux

print("Ordinamento InsSort:  ", final1)
print("Ordinamento QuickSort:", final2)
print("Ordinamento HeapSort: ", final3)


