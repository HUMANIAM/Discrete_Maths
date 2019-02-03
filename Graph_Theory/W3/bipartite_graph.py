"""
Bipartite Graph : is a graph that its nodes can be divided into two disjoin sets where there is
no edges between nodes in the same set and every node in one set is connected with one or more node
from the other set
"""
import networkx as nx
from networkx.algorithms import bipartite
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'

B = nx.Graph()
#B.add_nodes_from([1, 2, 3, 4, 5, 6], bipartite=0)
#B.add_nodes_from(['a', 'b', 'c', 'd', 'e', 'f'], bipartite=1)
B.add_edges_from([(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (2, 'd'), (3, 'b'), (3, 'd'), 
                   (4, 'c'), (4, 'd'), (4, 'e'), (4, 'f'),(5, 'c'), (5, 'e'), (5, 'f'), (6, 'd')])
draw(B, layout = 'circo')

# color Left set with Red and Right set with blue
if bipartite.is_bipartite(B) :
    R_set, L_set = bipartite.sets(B)
    for v in R_set :
        B.node[v]['color'] = 'blue'
    for v in L_set :
        B.node[v]['color'] = 'red' 
else :
    print("This is not a bipartite graph")


# maximum weight matching between the left set and the right set
M = nx.max_weight_matching(B)
print(M)
for v1, v2 in M.items():
    B[v1][v2]['color'] = 'green'
draw(B, layout='circo')


#draw matching edges
MG = nx.Graph()

for v1, v2 in M.items():
    MG.add_edge(v1, v2, color = 'green')
    MG.node[v1]['color'] = 'blue'
    MG.node[v2]['color'] = 'red'

draw(MG, layout = 'circo')
