"""
MST_based algorithm is another approximation algorithm that find a solution not the optimal but close
to the optimal solution. this algorithm based on the graph of TSP problem is metric this means
if there is 2 verteces u, v and another vertex z then
d(u, v) <= d(u, z) + d(z, v)  (Euclidean property)

MST <= TSP then 2*MST <= 2*TSP

steps of this algorithm
&***********
1- compute MST of TSP
2- duplicate edges of MST  >> D
3- find the Eulerian cycle of D without visit any vertex twic

read more from the specializaion material
complexity (O(n^2))
"""
import networkx as nx
import math

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return a 2-approximation of an optimal Hamiltonian cycle.

def approximation(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # You might want to use the function "nx.minimum_spanning_tree(g)"
    # MST of the graph
    mst = nx.minimum_spanning_tree(g)
    order = list(nx.dfs_preorder_nodes(mst, 0))

    # weight of the cycle
    weight = sum(g[order[i-1]][order[i]]['weight'] for i in range(len(order)))

    return weight


def dist(point1, point2) :
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def main():
    G = nx.Graph()
    points = [(199, 59), (152, 117), (68, 87), (281, 161), (11, 53), (254, 227)]
    for i in range(len(points)) :
        for j in range(i+1, len(points)) :
            G.add_edge(i, j, weight=dist(points[i], points[j]))
    
    print(approximation(G))

if __name__ == '__main__':
    main()