#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 10:32:21 2021

@author: luca
"""

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import sys
import numpy as np
import time
import pandas as pd
import csv
import seaborn as sns
import random

rr=[5, 69]
nn=[8000, 20000]

with open('esame_out.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['n','m','hfn','hfm','tempo']) #numero archi totali (m)

    tempii=[]
    for n in nn:
        for r in rr:
            # Grafo G
            G = nx.barabasi_albert_graph(n, r, seed=37)
            # Con m archi totali
            m = G.number_of_edges()

            tempi = []

            for i in range(10):

                cpu=time.process_time()
                d,p = nx.single_source_dijkstra(G, source = random.choice(list(G.nodes())))
                tempi.append(time.process_time()-cpu)
                assert  max(d.values()) < n # Mi assicuro che il grafo non sia pesato: tra tutti i percorsi, dalla source, la distanza ad ogni vertice non può essere maggiore di n

            elapsed = np.median(tempi) # Faccio la media dei tempi

            tempii.extend(tempi) #vettore per plot tempi

            writer.writerow([n, m, "High" if n==nn[1] else "Low", "High" if  r==rr[1]  else "Low", elapsed])

#Grafico dei tempi
plt.xlabel("n")
plt.ylabel("tempi")
plt.plot(range(len(tempii)), tempii)
plt.show()


df = pd.read_csv('esame_out.csv')
print(df)

sns.set(style="ticks", color_codes=True)
sns.lineplot(x="n", y="tempo", style="hfm", data=df, linewidth=5)
plt.show()

sns.lineplot(x="m", y="tempo", style="hfn", data=df, linewidth=5)
plt.show()
