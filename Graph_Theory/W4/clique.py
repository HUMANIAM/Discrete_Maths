"""
Clique : is a complete subgraph where every 2 vertices of it are connected by an edge
*****
Maximum Clique : is a clique that can't be extended to a larger one
*************
Independent set : is a set of vertices that there are no edges between any 2 vertices of it
**************
Maximum IS : is a IS that can't ve extended to a larger one
**********

relation : maximum IS in a graph = maximum clique in a complement graph
******

# we use networkx algorithms to focus on concepts and approaches rather than implementation
# we already implemented these algorithms in algorithms specialization before with C++
"""
import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('e', 'a'),
                  ('f', 'a'), ('g', 'b'), ('h', 'c'), ('i', 'd'), ('j', 'e'), 
                  ('f', 'h'), ('h', 'j'), ('j', 'g'), ('g', 'i'), ('i', 'f'),
                  ('j', 'i'), ('j', 'd'), ('d', 'g')])

# draw(G, layout='circo')

#identify the max clique in the graph
cliques=nx.find_cliques(G)

max_clique = max(list(nx.find_cliques(G)), key = lambda c : len(c))

# color it in the original graph
for v in max_clique:
    G.node[v]['color'] = 'blue'
    for u in max_clique:
        if u != v:
            G[u][v]['color']='red'

#draw the the Maximum clique seperately
MCG = nx.Graph()
for v in max_clique :
    if len(MCG.nodes()) == 0 : MCG.add_node(v)
    MCG.add_edges_from([(v, u) for u in MCG.nodes()])

# maximum independent set 
print(list(nx.maximal_independent_set(G)))

#visualize the max clique           
draw(MCG, layout='circo')

#visualize the Graph with max clique
draw(G, layout = 'circo')

