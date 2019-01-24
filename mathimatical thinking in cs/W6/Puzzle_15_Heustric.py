"""Problem description : you are given you a matrix with 16 different numbers from 0 to 15 and
  ********************  your task is find the steps of moves to reach from the current configuration
  of the puzzle to the target one.
  ^ if it is possible print the solution
  ^ if not print impossible
"""
def perm_is_even_fast(p) :
	pos, swaps = {}, 0
	perm = [i for sl in p for i in sl]
	for i in range(len(perm)) :	pos[perm[i]] = i
	
	for i in range(len(perm)) :
		j = (i+1)%16
		if j == perm[i]: continue
		swaps += 1
		perm[pos[j]], pos[perm[i]], perm[i] = perm[i], pos[j], j

	return swaps % 2 == 0

def puzz_astar(start,end):
    """
    A* algorithm
    """
    front = [ [heuristic_2(start), [start, "Get ready"]] ] #optional: heuristic_1
    expanded = []
    expanded_nodes=0
    
    while front :
        i = 0
        #choose the node that is closest to the solution
        for j in range(1, len(front)) :
            if front[i][0] > front[j][0]: i = j

        path = front[i]; 						# list of puzzle configuration [dist, path]
        front = front[:i] + front[i+1:]  		# remove this path from all paths
        endnode = path[-1][0]; 					# the last configuration in the path

        if endnode == end:	break 				# we are done

        expanded.append(endnode)
        for config in moves(endnode): # Try the 4 choices U, L, R, D

            if config[1] in expanded: continue   # avoid cycles
            front.append([config[0]] + path[1:] + [[config[1], config[2]]])

        expanded_nodes += 1

    print ("Expanded nodes:", expanded_nodes)
    print("read the solution in out.txt file")
    open("out.txt", "w").write(str('\n'.join([config[1] for config in path[1:]])))
    # pp.pprint(path)


def moves(mat): 
    """
    Returns a list of all possible moves
    """
    output, m = [], eval(mat) 

    #location of emtpy cell
    p = [i for sl in m for i in sl].index(0)
    i, j = int(p/4), p % 4 


    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      output.append([heuristic_2(str(m)), str(m), "Move {}".format(m[i][j])])
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 3:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      output.append([ heuristic_2(str(m)), str(m), "Move {}".format(m[i][j]) ])
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      output.append([ heuristic_2(str(m)), str(m), "Move {}".format(m[i][j]) ])
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 3:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      output.append([ heuristic_2(str(m)), str(m), "Move {}".format(m[i][j]) ])
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    return output

def heuristic_1(puzz):
    """
    Counts the number of misplaced tiles. It results in so many nodes generating so it is not
    good heuristic
    """ 
    misplaced = 0
    compare = 1
    m = eval(puzz)
    for i in range(4):
        for j in range(4):
            if m[i][j] != compare%16:
                misplaced += 1
            compare += 1
    return misplaced

def heuristic_2(puzz):
    """
    Manhattan distance
    """  
    distance = 0
    m = eval(puzz)

    for i in range(4) :
    	for j in range(4): 
    		r = int(m[i][j]/4) if m[i][j]%4 else int(m[i][j]/4) - 1
    		c = (m[i][j]%4 - 1) if m[i][j]%4 else 3

    		if m[i][j] == 0 or (r == i and c == j ) : continue
    		distance += abs(i - r) + abs(j+1 - c)

    return distance

if __name__ == '__main__':
    puzzle = str([[2,6,3,4],[9,11,7,8],[1,13,14,12],[5,10,15,0]])
    end = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])

    if perm_is_even_fast(eval(puzzle)) : 
    	puzz_astar(puzzle, end)
    else : 
    	print("puzzle must be odd permutation to be solved")
