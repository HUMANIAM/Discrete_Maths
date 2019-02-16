"""
Travel salesman problem is very popular problem in computer science and used in many many apps
Description: given a set of nodes and edges between them. find the shortest path that visit every
**********   node exactly once

* we can think in this problem as a permutation problem where we find the order of nodes that gives
the shortest path

* complexity of this solution is n!
"""
import time 
import networkx as nx
from itertools import permutations

def all_permutations(g):
    n = g.number_of_nodes()
    shortest_tour = None

    for tour in permutations(range(n)) :
      tour_len = 0
      valid = True

      # length of the tour 
      for i in range(len(tour)) :
      	if not g.has_edge(tour[i], tour[i-1]) :
      		valid = False
      		break
      	else :
      		tour_len += g[tour[i-1]][tour[i]]['weight']

      # may be a valid cycle with the shortest length
      if valid and (shortest_tour is None or tour_len < shortest_tour) :
        shortest_tour = tour_len

    return shortest_tour

def main():
	G = nx.Graph()
	for i in range(9) :
		for j in range(9) :
			if i != j :
				G.add_edge(i, j, weight=i+j)


	start_time = time.time()
	print(all_permutations(G))
	end_time = time.time()
	print(end_time - start_time)

if __name__ == '__main__':
	main()