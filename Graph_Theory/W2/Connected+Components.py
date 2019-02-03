
# coding: utf-8

# In[1]:


import networkx as nx
import pygraphviz as pgv
from nxpd import draw, nxpdParams
nxpdParams['show'] = 'ipynb'


G = nx.Graph()
G.add_edges_from([('a', 'b'), ('t', 'c'), ('b', 'x'), ('c', 'q'), ('q', 't')])
draw(G, layout='circo')


# In[2]:


print("G has {} connected components".format(nx.number_connected_components(G)))
for cc in nx.connected_components(G):
    print(cc)


# In[ ]:




