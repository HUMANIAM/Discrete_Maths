"""
Drawing the graphs but specifing objects and each relationship between objects
"""
import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams

G = nx.DiGraph()
G.add_edge("a", "b")
G.add_edge("b", "c")
G.add_edge("c", "d")
G.add_edge("d", "e")
G.add_edge("e", "c")
G.add_edge("a", "d")

draw(G, layout='circo')