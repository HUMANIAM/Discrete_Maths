"""
Minimum spanning tree is a tree connect all nodes of graph with unique simple paths and with
minimum cost.
* There are 2 types of algorithms (both are gready to construct MST)
1- Prime's algorithm >> vertex_based algorithm
2- Kruskal's algorithm >> edge_based algorithm
"""

import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph()
G.add_edges_from([
        ('a', 'b', {'weight':2, 'label': 2}), 
        ('a', 'c', {'weight':3, 'label': 3}), 
        ('a', 'd', {'weight':1, 'label': 1}), 
        ('a', 'e', {'weight':3, 'label': 3}), 
        ('b', 'c', {'weight':4, 'label': 4}), 
        ('c', 'd', {'weight':5, 'label': 5}), 
        ('d', 'e', {'weight':4, 'label': 4}), 
        ('e', 'a', {'weight':1, 'label': 1})
    ])
draw(G, layout='circo')

#draw minimum spanning tree
T = nx.minimum_spanning_tree(G)
MST = nx.Graph()

for e in T.edges():
    MST.add_edges_from([(e[0], e[1], {'label' : G[e[0]][e[1]]['weight'], 'color':'blue'})])
draw(MST, layout='circo')