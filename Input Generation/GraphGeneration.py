import networkit as nk
import networkx as nx
from matplotlib import pyplot as plt

ERDOSGRAPH = nk.generators.ErdosRenyiGenerator(500, 0.2).generate()
print(ERDOSGRAPH.numberOfNodes(), ERDOSGRAPH.numberOfEdges())

