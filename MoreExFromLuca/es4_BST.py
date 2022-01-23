#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:37:19 2021

@author: luca
"""
import pandas as pd
from heapq import heappush, heappop
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
from math import ceil, floor

arr = range(1,64)


class node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        
    def addNode(self, value):
        if self.root==None:
            self.root = node(value)
        else:
            self._addNode(value, self.root)
    
    def _addNode(self, value, curr_node):
        if value < curr_node.value:
            if curr_node.left==None:
                curr_node.left = node(value)
            else:
                self._addNode(value, curr_node.left)
        
        elif value > curr_node.value:
            if curr_node.right==None:
                curr_node.right = node(value)
            else:
                self._addNode(value, curr_node.right)
        
        else:
            print("Nodo già presente")
            
    def printBST(self):
        print(self.root.value)
                



# def getchild(arr, T):
#     if len(arr) == 1:
#         T.add_node(arr[0], left = None, right = None)
#         return T.nodes[arr[0]]
#     else:
#         m = floor(len(arr)/2)
#         T.add_node(arr[m], left = getchild(arr[0:m], T), right = getchild(arr[m:len(arr)], T))
#         return T.nodes[arr[m]]

def viewBST(B):
    T = nx.DiGraph()
    T.add_node(B.root, value=B.root.value)

    def addChild(current):
        if current.left is not None:
            T.add_edge(current, current.left)
            
            T.nodes[current.left]["value"] = current.left.value
            
            addChild(current.left)

        if current.right is not None:
            T.add_edge(current, current.right)
            
            T.nodes[current.right]["value"] = current.right.value

            addChild(current.right)
            
    addChild(B.root)      

    return T


# T = buildBST(arr)
# nx.draw(T, graphviz_layout(T, prog="dot"), with_labels=True)



def loadtoBST(B, a):
    print(a)
    if len(a) == 1:
        B.addNode(a[0])
    elif len(a) ==0:
        pass
    else:
        m = floor(len(a)/2)
        B.addNode(a[m])
        loadtoBST(B, a[0:m])
        loadtoBST(B, a[m+1:len(a)])
    return B
    
    




# creo un cazzo di bst
B = BST()
# aggiungo i dati da un array al bst
B = loadtoBST(B, sorted(arr))
# converto il bst in un nx.digraph
T = viewBST(B)

B.printBST()

nx.draw(T, graphviz_layout(T), with_labels=True, labels=nx.get_node_attributes(T, "value"))

