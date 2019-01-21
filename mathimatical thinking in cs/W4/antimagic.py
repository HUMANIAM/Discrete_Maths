"""Problem Description:
******************
An (-1,0,1) Antimagic SquareIs it possible to fill a 3x3 table by numbers -1, 0 and 1 so that the
um of each row, each column and both diagonals produce different numbers? Click the cell to change
number there. Sums of rows, columns and diagonals will be printed on the side of the table."""

from itertools import permutations

INF = 100000
N, R = 4, 2


def is_antimagic(square) :
	sums = []
	# rows
	for r in square :
		if sum(r) in sums : return False
		sums.append(sum(r))

	# columns
	for j in range(0, N) :
		summ = 0
		for i in range (0, N): summ += square[i][j]

		if summ in sums : return False
		sums.append(summ)

	#diagonals
	# Left Top to Right Bottom diag
	summ = 0
	for i in range(0, N):	summ += square[i][i]
	
	if summ in sums : return False
	sums.append(summ)

	# Left Bottom to Right Top
	summ = 0
	for i in range(N-1, -1, -1) : summ += square[(N-1)-i][i]
	if summ in sums : return False
	sums.append(summ)

	# they are all different
	return True

def search_bt(square, v = 0) :
	r, c = int(v/N), (v % N)
	#check if the previous assignment works if not return if the table is full
	if (v == N*N) or square[r][c] != INF :
		if(is_antimagic(square)) : return True
		if v == N*N : return False

	m = square[r][c]
	# Try the possible values for every cell
	for p in range(-R, R+1, 1) :
		if p != m :
			square[r][c] = p
			if search_bt(square, v+1) : return True

	return False

def main():
	square = [[INF] * N for i in range(1, N+1)]
	if search_bt(square) : 
		print(square)
	else : print("can't acheive constraints by this range of numbers")


if __name__ == '__main__':
	main()