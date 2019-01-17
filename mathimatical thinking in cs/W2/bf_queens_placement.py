import itertools as it

class QueenPlacement:
	"""find the placement of queens in n*n chessboard where 2 queens can't attack
		each other. we can do that by * put make every col and every row is covered
		by only one queen * make sure there is no diagonal covered by 2 queens
	"""
	def __init__(self, n):
		self.n = n;

	def valid_perm(self, rows):
		for (c1, c2) in it.combinations(range(self.n), 2) :
			if abs(c1 - c2) == abs(rows[c1] - rows[c2]): return False
		return True

	def solution(self):
		for perm in it.permutations(range(self.n)):
			if(self.valid_perm(perm)) : return list(perm)
		return []

def main():
	queen = QueenPlacement(4)
	print(queen.solution())
if __name__ == '__main__':
	main()