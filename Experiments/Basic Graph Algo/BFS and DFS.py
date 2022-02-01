from Imports.myimports import *

ERDOSGRAPH = networkx.erdos_renyi_graph(200, 0.2)

BFSTree = networkx.algorithms.traversal.breadth_first_search.bfs_tree(G=ERDOSGRAPH,
                                                                      source=random.choice(list(ERDOSGRAPH.nodes())))

DFSTree = networkx.algorithms.traversal.depth_first_search.dfs_tree(G=ERDOSGRAPH,
                                                                    source=random.choice(list(ERDOSGRAPH.nodes())))

assert networkx.number_of_edges(BFSTree) < networkx.number_of_nodes(ERDOSGRAPH)

assert networkx.number_of_edges(DFSTree) < networkx.number_of_nodes(ERDOSGRAPH)
