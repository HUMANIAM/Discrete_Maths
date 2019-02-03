#In this program we will try to solve the Guarini puzzle where we need to cheek is it possible to reach from specific configuration
# to anthor configuration or it is impossible (the main idea is if the two configurations lie in the same strongely connected component)
# then the solution is possible and there is a path from the original one to the target one and if they lie in 2 different strongley connected
# components then it is impossible
# in this program we will consider the 3x3 chessboard

import networkx as nx                  # create Graph
import pygraphviz as pgv               # visualize the Graph
from nxpd import draw, nxpdParams      
nxpdParams['show'] = 'ipynb'

import itertools as it        # enumerate all possible configurations

WIDTH, HEIGHT = 3, 3         # width and height of the chess board
SIZE = WIDTH * HEIGHT
G = nx.Graph()               # create object of type graph

# enumerate all configurations as nodes
for wb_indices in it.permutations(range(SIZE), 4):
    configuration = ['*'] * 9                 # use list where str object is immutable 
    configuration[wb_indices[0]] = 'W'
    configuration[wb_indices[1]] = 'W'
    configuration[wb_indices[2]] = 'B'
    configuration[wb_indices[3]] = 'B'

    G.add_node("".join(configuration))        # join chars in list and make string represent the current config

# draw(G, layout = 'circo')      # the graph without add edges between configurations


#list all possible movements in 3x3 chess board
def create_movements():
    movements = {}
    for v in range(SIZE) :
        movements[v] = []
        
        # Top L
        if v - 2*Width >= 0 :
            vv = v - 2*Width
            if vv%Width !=  0 :
                movements[v].append(vv - 1)
            if (vv+1)%Width != 0 :
                movements[v].append(vv+1)
        
        # Bottom L
        if v + 2*Width < SIZE :
            vv = v + 2*Width
            if vv%Width !=  0 :
                movements[v].append(vv - 1)
            if (vv+1)%Width != 0 :
                movements[v].append(vv+1)
        
        # Left L
        r = int(v/Width)
        if (v-2) > 0 and int((v-2)/Width) == r :
            vv = v - 2
            if (vv + Width) < SIZE :
                movements[v].append(vv + Width)
            if (vv - Width) >= 0 :
                movements[v].append(vv - Width)
        
        # Right L
        if (v+2) < SIZE and int((v+2)/Width) == r :
            vv = v + 2
            if (vv + Width) < SIZE :
                movements[v].append(vv + Width)
            if (vv - Width) >= 0 :
                movements[v].append(vv - Width)
    return movements

#list all movements manually
def create_possible_movements():
    moves = [[] for _ in range(8)]
    moves[0] = [4, 6]
    moves[1] = [5, 7]
    moves[2] = [3, 6]
    moves[3] = [2, 7]
    moves[4] = [0, 5]
    moves[5] = [1, 4]
    moves[6] = [0, 2]
    moves[7] = [1, 3]
    return moves

# add edges to the graph. any pair of configurations are connected with a graph if and only
# if they are reachable from each other

for node in G.nodes():
    configuration = list(node)

    for i in range(SIZE):
        if configuration[i] != "*":        # this cell in the chess board has a knight
            
            for new_pos in moves[i]:       # can reach to other some of cofigurations by just move the knight in this cell
                if configuration[new_pos] != "*":     #if the possible move has a knight continue
                    continue
                    
                new_configuration = list(configuration)     # create new configuration

                #make the movement from i position to new_pos position
                new_configuration[i] = "*"                  
                new_configuration[new_pos] = configuration[i]
                
                # add edge between the two configuration if there is no one
                if not G.has_edge("".join(configuration), "".join(new_configuration)):
                    G.add_edge("".join(configuration), "".join(new_configuration))

#draw (G, layout = 'circo')

# The resulted Graph has
print(nx.number_of_nodes(G), "Node")
print(nx.number_of_edges(G), "Edge")
print(nx.number_connected_components(G), "Connected Component")


# after create the Graph of Guarini puzzle. we check if 2 configurations lie in the same strongely connected component then it is
# possible to go from one to the other. If they are located in 2 different strongely connected components then it impossible to 
# convert one to the other
# 1- From "W*W**B*B" To "W*B**W*B"
# 2- From "W*W**B*B" To "B*B**W*W"
# 3- From "W*W**B*B" To "W*B**B*W"

assert "B*B***W*W" in nx.node_connected_component(G, "W*B***B*W")
assert "B*B***W*W" in nx.node_connected_component(G, "W*W***B*B")
assert "W*B***B*W" not in nx.node_connected_component(G, "W*W***B*B")

# As we saw "W*B**W*B" is reachable from "W*W**B*B" where they are lie in the same connected component so we need to find the 
# minimum number of movements to reach from "W*W**B*B" to "W*B**W*B" 

print(" -> ".join(nx.shortest_path(G, "W*B***B*W", "B*B***W*W" )))
