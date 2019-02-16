"""
Here we use the dp technique to solve the tsp problem in less time than the Branch and Bound algorithm
and also brute force technique who take O(n!) time. but this dp algithm will take only O(n^2 * 2^n) time

Description of the algorithm:
**************************
instead of find the Hamiltonian path of the graph immediately we divide it into subgraphs or subsets of nodes
and solve every small subgraphs then bigger subgraphs are based on the smaller ones. It is like building a tower
for our problem TSP
* start from vertex 0. Hamiltonian path here is zero where the start vertex and the end vertex are the same
* find all subsets of nodes that include 0 as a start vertex {0,1}, {0,2}, {0,3}, {0,1,2}, ......, {0,1, ...., n-1}
* solve the smaller subsets by finding the optimal path from zero that visits all verteces
* do that in increasing subsets untill reach the bigger one {0,1,2,....., n-1}
* find the optimall Hamiltonian path that covers all verteces
* find the optimal Hamiltonian cycle that ends at zero
"""
import networkx as nx
from itertools import chain, combinations
import math

# create all subsets that contains vertex 0 as an element of it
def powerset(s):
	subsets = tuple(chain.from_iterable(combinations(s, r) for r in range(2, len(s) + 1))) 
	return [subset  for subset in subsets if 0 in subset]


# This function finds an optimal Hamiltonian cycle using the dynamic programming approach.
def dynamic_programming(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    # subsets that contains only vertex 0 as an element of it
    power = powerset(range(n))
    
    # T contains optimal paths for vertex i in subset s
    T = {}
    T[(0, ), 0] = 0

    # For every subset s of [0,...,n-1] find optimal paths for i vertex
    for s in power:
    	# For every vertex i from s which we consider as the ending vertex of a path going through vertices from s.
    	for i in s:
    		# vertex 0 is the start vertex so its optimal path is always know zero
    		if i == 0 : continue
    		# Define the tuple which contains all elements from s without *the last vertex* i.
    		t = tuple([x for x in s if x != i])		
    		# Now we compute the optimal value of a cycle which visits all vertices from s and ends at the vertex i.
    		T[s, i] = T[s, 0] = float("Inf")

    		# find the optimal path for i in current subgraph
    		for j in t :
    			T[s, i] = min((T[t, j] + g[i][j]['weight']), T[s, i])

    # Return the weight of on optimal cycle - this is the minimum of the following sum:
    # weight of a path + the last edge to the vertex 0.
    return min(T[tuple(range(0, n)), i] + g[i][0]['weight'] for i in range(1, n))

def dist(point1, point2) :
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def main():
	G = nx.Graph()
	points = [(199, 59), (152, 117), (68, 87), (281, 161), (11, 53), (254, 227)]
	for i in range(len(points)) :
	    for j in range(i+1, len(points)) :
	        G.add_edge(i, j, weight=dist(points[i], points[j]))
                
	print(dynamic_programming(G))
if __name__ == '__main__':
	main()