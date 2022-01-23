"""
Created on Tue Aug 31 10:17:21 2021

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


# doub=[50,100,200,400, 800, 1600, 3200, 6400, 12000,24000]

xt=[]
xt2=[]
nn=[101,202]
mm=[30,80]

with open('es7_out.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['n', 'm', 'hfn', 'hfm', 'time'])

    for n in nn:
        for m in mm:
            
            # cpu = time.process_time()
        
            G = nx.barabasi_albert_graph(n, m, 33)
            # # pos = graphviz_layout(G)
            # # nx.draw(G)
            # # plt.show()
            # elapsed2 = (time.process_time()-cpu)
            # xt2.append(elapsed2)
            
            count=[]
            best = sys.maxsize
            
            cpu = time.process_time()
            for attempt in range(10):
                
                d = nx.coloring.greedy_color(G, strategy='connected_sequential_bfs')
                col = set()
                for j in d.values():
                    col.add(j)
                    count.append(len(col))    
                if len(col) < best:
                    best = len(col)
                        
            print(best, col)
            elapsed = (time.process_time()-cpu)
            # xt.append(elapsed)
            writer.writerow([n, m, "High" if n==nn[1] else "Low", "High" if  m==mm[1]  else "Low", elapsed])


# plt.plot(doub, xt, label= 'Time GC')
# plt.plot(doub, xt2, label= 'Time GENERATING')
# plt.legend()
df = pd.read_csv('es7_out.csv')
sns.set(style="ticks", color_codes=True, font_scale=1)
ax = sns.lineplot(x="n", y="time",style="m",data=df,linewidth=5)
sns.despine()
plt.show()