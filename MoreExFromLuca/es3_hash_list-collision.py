#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:08:12 2021

@author: luca
"""


import pandas as pd
# from heapq import heappush, heappop
# import networkx as nx
# from networkx.drawing.nx_pydot import graphviz_layout
# import numpy as np

# Import da file CSV tramite Pandas
df = pd.read_csv("es3_dati.csv")
print("Dati grezzi: \n", df, "\n\n")

# Modulo, numero primo non troppo vicino ad una potenza di 2
m = 701;

# Tabella Hash di lunghezza m
T = [[None] for _ in range(m)]

# Funzione Hash, prende in input un intero e restituisce il valore Hash
# utilizzando il metodo della divisione
def hashk(key, modulo = m):
    value = key%modulo
    return value

        


# Funzione che inserisce un elemento list nella tabella Hash
# utilizzando le liste di collisione
# Prende in input una list
def insertht(o):
    key = hashk(o[0])
    if T[key] == [None]:
        T[key].insert(0,o)
    else:
        for j in range(0, len(T[key])):
            if T[key][j] == None:    
                T[key].insert(j, o)

# Funzione che cerca una chiave nella tabella Hash
# Prende in input una chiave (non Hashata), e la cerca nella rispettiva posizione
# Restituisce una coppia list(key, element)
def search(x):
    key = hashk(x)
    if T[key] == [None]:
        return "No Key ({}) found.".format(x)
    elif len(T[key]) == 2:
        elem = T[key][0]
        return "Found key ({}): {}".format(elem[0], elem[1])
    else:
        for i in T[key]:
            if i == None:
                return "No Key ({}) found.".format(x)
            if i[0] == x: return "Found key ({}): {}".format(i[0], i[1])



def delete(e):
    key = hashk(e)
    if T[key] == [None]:
        return "No Element with ({}) key found.".format(e)
    elif len(T[key]) == 2:
        deleted = T[key][0]
        T[key] = [None]
        return "Elemento {} eliminato.".format(deleted)
    else:
        for i in T[key]:
            if i == None:
                return "No Element with ({}) key found.".format(e)
            if i[0] == e:
                T[key].remove(i)
                return "Elemento {} eliminato.".format(i)

for i in df.iterrows():
    insertht(i[1].tolist())


TT = pd.DataFrame(T).dropna(how="all")
print(TT, "\n")


print(search(444))
print(search(690))
print(search(702))
print(search(1))
print(search(1404))
print(search(2))
print("\n")
print(delete(444))
print(delete(700))
print(delete(1404))
print(delete(702))
print(delete(702))
print(delete(703))
print(delete(2))
print(delete(705))
print(delete(706))
print("\n")

TT = pd.DataFrame(T).dropna(how="all")
print(TT, "\n")