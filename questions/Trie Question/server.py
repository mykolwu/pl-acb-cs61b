import prairielearn as pl
import numpy as np
import networkx as nx
import random

import itertools
import random
import string
import numpy.linalg as la


pos = {}

def returnGraph():
    # G = nx.Graph()


    # G.add_node("Z")
    # G.add_node("S")

    # Define a binary tree
    T = nx.DiGraph()
    T.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])

    # Draw the binary tree
    pos = nx.nx_agraph.graphviz_layout(T, prog="dot")
    nx.draw_networkx(T, pos=pos, with_labels=True, node_size=800, font_size=20, font_weight="bold")
    # data["params"]["G"] = pl.to_json(T)



    return T


### inputList should be list of nodes you want to be inputs
### locationGraph should be where graph you want as input is stored in data[params]

def getPos(data, inputList, Graph ,defaultProg="dot"):

    G = Graph
    
    pos = nx.nx_agraph.graphviz_layout(G, prog=defaultProg)
    counter = 0

    for i in inputList:
        if i in pos.keys():
            inputTuple = pos.get(i)
            
            
            data["params"]["x" + str(counter)] = inputTuple[0] 
            data["params"]["y" + str(counter)] = inputTuple[1]
            counter += 1

    data["params"]["G"] = pl.to_json(G)


def generate(data):
    getPos(data, [0, 1], returnGraph())

    random_graph = nx.gnm_random_graph(5, 6)
    