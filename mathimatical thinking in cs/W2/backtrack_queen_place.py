import itertools as it
from bf_queens_placement import QueenPlacement

class BTQueenPlacement:
	"""find the placement of queens in n*n chessboard where 2 queens can't attack
		each other. we can do that by * put make every col and every row is covered
		by only one queen * make sure there is no diagonal covered by 2 queens
	"""
	def __init__(self, n):
		self.n = n;
		self.solutions = []

	def valid_perm(self, rows):
		for (c1, c2) in it.combinations(range(self.n), 2) :
			if abs(c1 - c2) == abs(rows[c1] - rows[c2]): return False
		return True

	def valid_diagonal(self, rows, r):
		if len(rows) == 0 : return True
		c = len(rows)
		for cc in range(len(rows)) :
			if abs(r - rows[cc]) == abs(c - cc) : return False
		return True

	def solution(self, rows = []):
		for r in range(self.n) :
			# valid row and diagnal
			if r not in rows and self.valid_diagonal(rows, r): 
				rows.append(r)
				if len(rows) == self.n :
					self.solutions.append(list(rows)); rows.pop(); continue;
				self.solution(rows)
				rows.pop()
			

def main():
	queen2 = BTQueenPlacement(8)
	# assert(queen1.solution() == queen2.solution())
	# print(queen1.solution())
	queen2.solution()
	print(len(queen2.solutions))
	for sol in queen2.solutions : print(sol, end = "\n\n")

if __name__ == '__main__':
	main()