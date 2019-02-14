"""
nearest neighbor is an approximation algorithm used not to find the best solution but finding a 
solution close the best solution.

Nearest Neighbor Algorithm: Start at any city; at each step extend the tour by moving from the 
************************* previous city to its nearest neighbor that has not yet been visited.

* for general graphs may produce a cycle that is much worse than the optimal solution
* using greedy heuristic nearest neighber
* In practice this Heuristic works quite well
* works good with Euclidean TSP
* greedy algorithm

* complexity : O(n**2)
* Significant difference in efficiency between nearest neighbor algorithm and the brute force
"""
import time 
import networkx as nx

def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():
        	if v in path : continue

        	weight = g[v][current_node]['weight']
        	if next_node == None or weight < min_edge :
        		min_edge = weight
        		next_node = v

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    cycle_weight = sum(g[path[i-1]][path[i]]['weight'] for i in range(g.number_of_nodes()))
    return cycle_weight

def main():
	G = nx.Graph()
	for i in range(1000) :
		for j in range(1000) :
			if i != j :
				G.add_edge(i, j, weight=1)

	start_time = time.time()
	print(nearest_neighbors(G))
	end_time = time.time()
	print("Time : ", end_time - start_time)

if __name__ == '__main__':
	main()