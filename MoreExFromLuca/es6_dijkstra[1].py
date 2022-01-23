"""
Created on Tue Aug 31 10:17:21 2021

@author: luca
"""

import pandas as pd
import csv
import seaborn as sns
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib.pyplot as plt    
import time
import random

G = nx.Graph()

e = [('a', 'b', 0.3), ('a', 'c', 0.9), ('c', 'b', 0.5), ('b', 'f', 1.2),
     ('c', 'd', 0.5), ('d', 'f', 1.2), ('f', 'g', 0.5), ('d', 'g', 1.2),
     ('d', 'e', 0.5), ('e', 'l', 1.2), ('l', 'm', 0.5), ('g', 'h', 1.2),
     ('h', 'i', 0.5), ('i', 'j', 1.2), ('e', 'j', 0.5), ('j', 'k', 1.2),
     ('h', 'j', 0.5), ('l', 'c', 0.8), ('m', 'j', 0.2)]

G.add_weighted_edges_from(e)

doubling=[100,200,400,800,1600,3200,6400,10000,20000]

ti=[]
ti1=[]
dj=[]
for i in doubling:
    cpu=time.process_time();
    G = nx.erdos_renyi_graph(i,0.01, seed=1)
    elapsed=time.process_time()-cpu;
    ti.append(elapsed)
    
    cpu=time.process_time();
    H = nx.fast_gnp_random_graph(i,0.01, seed=1)
    elapsed=time.process_time()-cpu;
    ti1.append(elapsed)

    cpu=time.process_time();
    nx.single_source_dijkstra(G, random.choice(list(G.nodes())))
    elapsed=time.process_time()-cpu;
    dj.append(elapsed)


plt.plot(doubling,ti1, label='fast')
plt.plot(doubling,ti, label='erdos')
plt.plot(doubling,dj, label='dijkstra')
plt.legend()
plt.show()

# ti1=[[],[]]
# for i in [random.choice(list(G.nodes())) for x in range(30)]:
#     cpu=time.process_time();
#     ti1[1].append(i)
#     w, P = nx.single_source_dijkstra(G, 1)
#     elapsed=time.process_time()-cpu;
#     ti1[0].append(elapsed)
    
# plt.plot(range(30), ti1[0], label='dijkstra')
# plt.legend()
# plt.show()

# a=pd.DataFrame(ti1)
# a=a.transpose()
# a=a.sort_values([0], ascending=False)
# a=a.astype({1:int})
# print(a)

m=[0.01, 0.2]
n=[70, 1400]

with open('es6_out.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Fm", "Fn","hFm", "hFn", "Time"])
        for mm in m:
            for nn in n:
                cpu=time.process_time();

                H = nx.erdos_renyi_graph(nn,mm, seed=1)
            
                elapsed=time.process_time()-cpu;
                writer.writerow([mm, nn, "High" if mm==m[1] else "Low", "High" if  nn==n[1]  else "Low", elapsed])




df = pd.read_csv('es6_out.csv')  
print(df) 

sns.set(style="ticks", color_codes=True, font_scale=1)
ax = sns.lineplot(x="Fm", y="Time",style="hFn",data=df,linewidth=5)
sns.despine()
plt.show()
# print(D)

# nx.draw(G, graphviz_layout(G, prog="fdp"), with_labels=True)
# plt.show()
# nx.draw(H, graphviz_layout(H, prog="fdp"), with_labels=True)
# plt.show()
# T = nx.Graph()

# for i in P:
#     path = P[i]
#     path_edges = list(zip(path,path[1:]))
#     T.add_edges_from(path_edges)
#     T.add_node(i, weight=w[i])

# nx.draw(T,graphviz_layout(G, prog="fdp"),edge_color='r',width=4, labels=nx.get_node_attributes(T, "weight"))


# G = nx.karate_club_graph()
# pos = nx.spring_layout(G)
# nx.draw(G,pos,node_color='b')
# draw path in red
# path = nx.shortest_path(G,source=14,target=16)
# path_edges = list(zip(path,path[1:]))

# nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
# nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=5)


