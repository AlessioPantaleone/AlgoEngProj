#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:37:19 2021

@author: luca
"""

class Graph:

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return self._graph_dict[vertice]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a list """
        return list(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        for i in edge:
            i = list(i)
            vertex1, vertex2 = tuple(i)
            for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
                if x in self._graph_dict:
                    self._graph_dict[x].append(y)
                else:
                    self._graph_dict[x] = [y]
                    
    def visita(self, vertex, tipo = "ampiezza"):
        """
        Riceve il nodo sorgente da cui iniziare la visita in ampiezza
        Restituisce un albero
        """
        T = Graph({vertex:[]})
        mark = self.__mark()
        F = []
        mark[vertex] = True
        F.append(vertex)
        while F:
            u = F.pop()
            for v in self._graph_dict[u]:
                if mark[v] == False:
                    if tipo == "ampiezza":
                        F.insert(0,v)
                    elif tipo == "profondità": F.append(v)
                    mark[v] = True
                    T.add_edge([[u,v]])
        return T
            
            

        
    def __mark(self):
        d = {}
        for i in self._graph_dict:
            d[i] = False
        return d    
            
    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if [neighbour, vertex] not in edges:
                    edges.append([vertex, neighbour])
        return edges



g = { 
        "a": ["b","c"], 
        "b": ["c","a"], 
        "c": ["a","b"]
    }

G = Graph(g)

G.add_edge([["c","d"], ["d", "a"],['e','c'],['d','e'],['e','f'],['f','b'],['f','g']])
print('tutti gli archi:', G.all_edges())
print('tutti i vicini di c', G.edges("c"))

B=G.visita('a', "ampiezza")
print('tutti gli archi BFS:', B.all_edges())
B=G.visita('a', "ampiezza")
print('tutti gli archi BFS:', B.all_edges())
B=G.visita('a', "profondità")
print('tutti gli archi DFS:', B.all_edges())


# class node:
#     def __init__(self, value=None):
#         self.value = value
#         self.left = None
#         self.right = None


# class BST:
#     def __init__(self):
#         self.root = None
        
#     def addNode(self, value):
#         if self.root==None:
#             self.root = node(value)
#         else:
#             self._addNode(value, self.root)
    
#     def _addNode(self, value, curr_node):
#         if value < curr_node.value:
#             if curr_node.left==None:
#                 curr_node.left = node(value)
#             else:
#                 self._addNode(value, curr_node.left)
        
#         elif value > curr_node.value:
#             if curr_node.right==None:
#                 curr_node.right = node(value)
#             else:
#                 self._addNode(value, curr_node.right)
        
#         else:
#             print("Nodo già presente")
            
#     def printBST(self):
#         print(self.root.value)
                



# # def getchild(arr, T):
# #     if len(arr) == 1:
# #         T.add_node(arr[0], left = None, right = None)
# #         return T.nodes[arr[0]]
# #     else:
# #         m = floor(len(arr)/2)
# #         T.add_node(arr[m], left = getchild(arr[0:m], T), right = getchild(arr[m:len(arr)], T))
# #         return T.nodes[arr[m]]

# def viewBST(B):
#     T = nx.DiGraph()
#     T.add_node(B.root, value=B.root.value)

#     def addChild(current):
#         if current.left is not None:
#             T.add_edge(current, current.left)
            
#             T.nodes[current.left]["value"] = current.left.value
            
#             addChild(current.left)

#         if current.right is not None:
#             T.add_edge(current, current.right)
            
#             T.nodes[current.right]["value"] = current.right.value

#             addChild(current.right)
            
#     addChild(B.root)      

#     return T


# # T = buildBST(arr)
# # nx.draw(T, graphviz_layout(T, prog="dot"), with_labels=True)



# def loadtoBST(B, a):
#     print(a)
#     if len(a) == 1:
#         B.addNode(a[0])
#     elif len(a) ==0:
#         pass
#     else:
#         m = floor(len(a)/2)
#         B.addNode(a[m])
#         loadtoBST(B, a[0:m])
#         loadtoBST(B, a[m+1:len(a)])
#     return B
    
    




# # creo un cazzo di bst
# B = BST()
# # aggiungo i dati da un array al bst
# B = loadtoBST(B, sorted(arr))
# # converto il bst in un nx.digraph
# T = viewBST(B)

# B.printBST()

# nx.draw(T, graphviz_layout(T, prog="dot"), with_labels=True, labels=nx.get_node_attributes(T, "value"))

