import random
import numpy as np
import prairielearn as pl
import graphviz


def generate(data):

    G = graphviz.Digraph('G')
    G.attr('node', shape='triangle')
    G.node('1', 'A')
    G.node('2', 'B')

    data["params"]["matrix"] = pl.to_json(G)
