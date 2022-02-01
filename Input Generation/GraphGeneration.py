import networkit as nk
import networkx as nx
from matplotlib import pyplot as plt

ERDOSGRAPH = nk.generators.ErdosRenyiGenerator(200, 0.2).generate()
print(ERDOSGRAPH.numberOfNodes(), ERDOSGRAPH.numberOfEdges())

BARABASIALBERTGRAPH = nk.generators.BarabasiAlbertGenerator(10, 200, n0=0, batagelj=True).generate()
print(BARABASIALBERTGRAPH.numberOfNodes(), BARABASIALBERTGRAPH.numberOfEdges())

COMPLETEGRAPH = nx.complete_graph(10)
print("COMPLETE GRAPH ARCS:", COMPLETEGRAPH.number_of_edges())

PATHGRAPH = nx.path_graph(10)
print("PATH GRAPH ARCS:", PATHGRAPH.number_of_edges())

WHEIGHTEDGRAPH = nx.er


# DEGREE DISTRIBUTIONS
# Node centrality index which ranks nodes by their degree
dd1 = sorted(nk.centrality.DegreeCentrality(BARABASIALBERTGRAPH).run().scores(), reverse=True)
dd2 = sorted(nk.centrality.DegreeCentrality(ERDOSGRAPH).run().scores(), reverse=True)

#plt.xscale("log")
plt.xlabel("degree")
#plt.yscale("log")
plt.ylabel("number of nodes")
plt.plot(dd1)
plt.plot(dd2)
plt.show()
