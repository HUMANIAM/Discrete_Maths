from itertools import permutations
from itertools import product
from itertools import combinations, combinations_with_replacement
import collections
import numpy as np

"""
problem : you have n types of fruits every type has unlimited value and you need to choose r fruits
********   out of the n types (repetition is allowable). what is the number of ways to do that?

solution : you can use seperators idea between the n types (n-1) seperators plus choosen objects 	
********	then you have n-1+r places and you need to pick r positions to place the r objects that
you select
"""
def combination_rep(n, r) :
	Cs = []
	for c in combinations_with_replacement(range(1,n+1), r):
		Cs.append(c)
	return Cs

def main():
	dd = 0
	for d in product(range(10), repeat = 4):
		if sum(d) == 10:
			dd += 1
	print(dd)
	# print(combination_rep(3, 2))
if __name__ == '__main__':
	main()