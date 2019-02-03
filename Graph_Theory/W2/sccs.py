import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
from itertools import product
nxpdParams['show'] = 'ipynb'


G = nx.DiGraph()
G.add_edges_from([('a', 'b'), ('b', 'c'), ('b', 'd'), ('d', 'c'), ('a', 'd'), ('e', 'd'), ('f', 'a'), ('b', 'f')])
draw(G, layout='circo')

print("Strongly connected components:")
SCCs = []
for scc in nx.strongly_connected_components(G):
    SCCs.append(scc)
print(SCCs)


# draw the meta graph of SCCs
print("MetaGraph of SCCs")
MG = nx.DiGraph()
sccs_str = [''.join(str(x) for x in scc) for scc in SCCs]

for i in range(len(SCCs)-1) :
    for j in range(i+1, len(SCCs)):
        for p in product(SCCs[i], SCCs[j]):
            yes, src, des = False, None, None
            
            if G.has_edge(p[0], p[1]):
                yes = True
                src, des = sccs_str[i], sccs_str[j]
                
            elif G.has_edge(p[1], p[0]):
                yes = True
                src, des = sccs_str[j], sccs_str[i]
                
            if yes :
                MG.add_edge(src, des)
                break
        
 
draw(MG, layout = 'circo')
