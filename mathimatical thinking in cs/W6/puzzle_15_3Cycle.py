"""Problem description : you are given you a matrix with 16 different numbers from 0 to 15 and
  ********************  your task is find the steps of moves to reach from the current configuration
  of the puzzle to the target one.
  ^ if it is possible print the solution
  ^ if not print impossible
"""

def perm_is_even(p) :
	swaps = 0
	for i in range(0, len(p)) :
		if i == p[i] : continue
		for j in range(i+1, len(p)) :
			if p[j] == i : 
				p[j], p[i] = p[i], p[j]
				swaps += 1
				break
	return swaps % 2 == 0

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

"""This solution is based on A* algorithm"""
def solution(position):

	end = str([[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12],[13, 14, 15, 0]])
	start = str([position[4*i : 4*(i+1)] for i in range(0, 4)])
	moves = []

	# 3-cycle solution

	return moves
	
def main():
	print(solution([2,6,3,4,9,11,7,8,1,13,14,12,5,10,15,0]))
	
if __name__ == '__main__':

	main()