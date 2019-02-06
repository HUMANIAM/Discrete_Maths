
import matplotlib.pyplot as plt
from random import randint, choice
import networkx as nx
import copy 


def draw_graph(G, nodes, edges, labels) :
	# positions for all nodes
	pos=nx.circular_layout(G)

	# add nodes
	nx.draw_networkx_nodes(G, pos,
	                       nodelist = nodes,
	                       node_color='#FF00FF',
	                       node_size=1000,
	                   alpha=0.8)

	# add labels of nodes
	nx.draw_networkx_labels(G,pos,labels,font_size=16)

	# add edges of the graph
	nx.draw_networkx_edges(G,pos,
	                       edgelist=edges,
	                       width=1,alpha=1,edge_color='r')

	plt.axis('off')
	plt.show()

# independent sets
def independent_sets(G):
	nodes = G.nodes()
	done_nodes = []

	ISs = []
	for v in nodes :
		if v not in done_nodes :
			IS = nx.maximal_independent_set(G, [v])
			sorted_IS = sorted(IS)

			if sorted_IS not in ISs : ISs.append(sorted_IS)
	
	print(ISs)

#main 
def main():
	G = nx.Graph()
	nodes = [v for v in range(1, 6)]
	labels = dict([(v, str(chr(v+96))) for v in range(1, 6)])
	edges = [(1, 4), (1, 6),(1, 8), (2, 4),(2, 8), (3, 5), (3, 7)]
	                  # (6, 1), (7, 2), (8, 3), (9, 4), (10, 5), 
	                  # (6, 8), (8, 10), (10, 7), (7, 9), (9, 6),
	                  # (10, 9), (10, 4), (4, 7)]

	# add nodes to the graph
	G.add_edges_from(edges)

	# Cliques in the graph G
	cliques = nx.find_cliques(G)
	max_clique = max(list(nx.find_cliques(G)), key = lambda c : len(c))
	print(max_clique)


	# independent set in the Graph G
	# independent_sets(G)
	# draw the Graph
	# draw_graph(G, nodes, edges, labels)


if __name__ == '__main__':
	main()

