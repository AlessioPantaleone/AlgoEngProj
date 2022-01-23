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
array = df.values.tolist()[0]
print("Dati grezzi: ", array)

# Costruzione dell'array con struttura a heap
heap = []
for item in array:
    heappush(heap, item)
print("Struttura a Heap: ", heap)



# Rappresentaione grafica tramite Networkx

def Left(i):
    return 2*i+1;
def Right(i):
    return 2*i+2;
G = nx.Graph()

for i in range(int(len(heap)/2)):
    
    r=Right(i)
    l=Left(i)
        
    if  l >= len(heap) or r >= len(heap):
        
        if l >= len(heap):
            G.add_edge(i, r)
            G.nodes[i]["value"] = heap[i]
            G.nodes[r]["value"] = heap[r]
        else:
            G.add_edge(i, l)
            G.nodes[i]["value"] = heap[i]
            G.nodes[l]["value"] = heap[l]
            
    else:
        G.add_edge(i, l)
        G.add_edge(i, r)
        G.nodes[i]["value"] = heap[i]
        G.nodes[r]["value"] = heap[r]
        G.nodes[l]["value"] = heap[l]

print(G)
nx.draw(G, graphviz_layout(G, prog="dot"), labels=nx.get_node_attributes(G, "value"))
nx.write_weighted_edgelist(G, "output.csv")


ordered = []
while heap:
    ordered.append(heappop(heap))
print("Ordinamento a Heap: ", ordered)
