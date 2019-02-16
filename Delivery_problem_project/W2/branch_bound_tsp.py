"""
Branch and bound algorithm is based on using Heuristics as guidence during search where this Heuristics
will keep us from so much useless computation
* Heuristics must be computed efficiently
* First Heuristic we already used is nearest neighbor (greedy heuristic ) (in most times you 
will not get the optimal solution)
* Lower Bound Heuristic : that we will implement it in this program is based on MST weight.
where TSP cost > MST cost if we find an extended branch will result in solution that is not better than
the one we have we will avoid this branch from the beginning.
"""

import networkx as nx
import time
import math
from itertools import permutations


# Lower bound used as a hueristic in this searching problem where there are many extensions of
# the current subpth but we need to invade only the subgraphs that may have a solution (cycle)
# better than the one we have Lower Bound Here is the MST cost plus the cost of the subpth
# if this Low_bound >= the current solution we ignore this branch of extension
def lower_bound(g, sub_cycle):
    # The weight of the current path.
    current_weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])

    # For convenience we create a new graph which only contains vertices not used by g.
    unused = [v for v in g.nodes() if v not in sub_cycle]
    h = g.subgraph(unused)
    

    # Compute the weight of a minimum spanning tree.
    t = list(nx.minimum_spanning_edges(h))
    print(t)
    mst_weight = sum([h.get_edge_data(e[0], e[1])['weight'] for e in t])

    # If the current sub_cycle is "trivial" (i.e., it contains no vertices or all vertices), then our lower bound is
    # just the sum of the weight of a minimum spanning tree and the current weight.
    if len(sub_cycle) == 0 or len(sub_cycle) == g.number_of_nodes():
        return mst_weight + current_weight

    # If the current sub_cycle is not trivial, then we can also add the weight of two edges connecting the vertices
    # from sub_cycle and the remaining part of the graph.
    # s is the first vertex of the sub_cycle
    s = sub_cycle[0]
    # t is the last vertex of the sub_cycle
    t = sub_cycle[-1]
    # The minimum weight of an edge connecting a vertex from outside of sub_sycle to s.
    min_to_s_weight = min([g[v][s]['weight'] for v in g.nodes() if v not in sub_cycle])
    # The minimum weight of an edge connecting the vertex t to a vertex from outside of sub_cycle.
    min_from_t_weight = min([g[t][v]['weight'] for v in g.nodes() if v not in sub_cycle])

    # Any cycle which starts with sub_cycle must be of length:
    # the weight of the edges from sub_cycle +
    # the minimum weight of an edge connecting sub_cycle and the remaining vertices +
    # the minimum weight of a spanning tree on the remaining vertices +
    # the minimum weight of an edge connecting the remaining vertices to sub_cycle.
    return current_weight + min_from_t_weight + mst_weight + min_to_s_weight


# The branch and bound procedure takes
# 1. a graph g;
# 2. the current sub_cycle, i.e. several first vertices of cycle under consideration.
# Initially sub_cycle is empty;
# 3. currently best solution current_min, so that we don't even consider paths of greater weight.
# Initially the min weight is infinite
def branch_and_bound(g, sub_cycle=None, current_min=float("inf")):
    # If the current path is empty, then we can safely assume that it starts with the vertex 0.
    if sub_cycle is None:
        sub_cycle = [0]

    # If we already have all vertices in the cycle, then we just compute the weight of this cycle and return it.
    if len(sub_cycle) == g.number_of_nodes():
        weight = sum([g[sub_cycle[i]][sub_cycle[i + 1]]['weight'] for i in range(len(sub_cycle) - 1)])
        weight = weight + g[sub_cycle[-1]][sub_cycle[0]]['weight']
        return weight

    # Now we look at all nodes which aren't yet used in sub_cycle.
    unused_nodes = list()
    for v in g.nodes():
        if v not in sub_cycle:
            unused_nodes.append((g[sub_cycle[-1]][v]['weight'], v))

    # We sort them by the distance from the "current node" -- the last node in sub_cycle.
    unused_nodes = sorted(unused_nodes)

    for (d, v) in unused_nodes:
        assert v not in sub_cycle
        extended_subcycle = list(sub_cycle)
        extended_subcycle.append(v)
        # For each unused vertex, we check if there is any chance to find a shorter cycle if we add it now.
        if lower_bound(g, extended_subcycle) < current_min:
            # If there is such a chance, we add the vertex to the current cycle, and proceed recursively.
            temp_min = branch_and_bound(g, extended_subcycle, current_min)
            # If we found a short cycle, then we update the current_min value.
            current_min = temp_min if temp_min < current_min else current_min


    # The procedure returns the shortest cycle length.
    return current_min

def dist(point1, point2) :
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def main():
    G = nx.Graph()
    points = [(199, 59), (152, 117), (68, 87), (281, 161), (11, 53), (254, 227)]
    for i in range(len(points)) :
        for j in range(i+1, len(points)) :
            G.add_edge(i, j, weight=dist(points[i], points[j]))
                

    print(list(nx.minimum_spanning_tree(G)))
    # start_time = time.time()
    # print(branch_and_bound(G))
    # end_time = time.time()
    # print(end_time - start_time)

if __name__ == '__main__':
    main()