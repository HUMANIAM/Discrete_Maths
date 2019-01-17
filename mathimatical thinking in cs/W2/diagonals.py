"""we need to find m diagonals in n*n grid where there is no 2 diagonals touch each others"""
NONE, TL, TR = 0, 1, 2

class DiagonalSequence:
	def __init__(self, n, m):
		self.n = n
		self.m = m
		self.mat = [[-1]*self.n for i in range(self.n)]


	def is_valid_diag(self, r, c, typ) :
		#check constraints
		rr = r-1
		cc = c-1
		if typ == TL :
			if rr >= 0 and self.mat[rr][c] == TR : return False
			if cc >= 0 and self.mat[r][cc] == TR : return False
			if rr >= 0 and cc >= 0 and self.mat[rr][cc] == TL : return False

		if typ == TR : 
			if rr >= 0 and self.mat[rr][c] == TL : return False
			if cc >= 0 and self.mat[r][cc] == TL : return False
			if rr >= 0 and c+1 != self.n and self.mat[rr][c+1] == TR : return False

		return True

	def solution(self, v = 0, d = 0):
		if d == self.m : return True
		if v == self.n * self.n : return False

		r = int(v / self.n)
		c = v % self.n

		for i in range(2, -1, -1):
			if self.is_valid_diag(r, c, i) :
				self.mat[r][c] = i
				if self.solution(v+1, d + (i != 0)) : return True

		return False


def main():
	diagseq = DiagonalSequence(5, 16)
	diagseq.solution()
	print(diagseq.mat)
if __name__ == '__main__':
	main()