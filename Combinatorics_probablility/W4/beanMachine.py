from itertools import permutations
from itertools import product
from itertools import combinations
import collections
import random
from datetime import datetime
import numpy as np
"""
Bean machine is a machine invented by the sir francesis galton and it is composed of source of beans
and n layers and n columns beans fall from up to down and at the end the max number of beans will collect
at the centre of machine. the probability diagram that describe it looks like the pascal's triangle
(n c)/2**k
"""
"""
Pascal's Triangle is a clever way to represent combinations
"""
combs = {}
def pascal_triangle(n) :
	global combs
	if n < 0 : return -1
	#set cells of the upright angle
	for i in range(n+1) :
		combs[(i, 0)] = 1
		combs[(i, i)] = 1

	# fill the remaining combinations
	for i in range(1, n+1):
		for m in range(1, i) :
			combs[(i, m)] = combs[(i-1, m)] + combs[(i-1, m-1)]


"""
How can we determine the probability of any element of the sets why we say sometimes in the toss coin
expriment they are equally likely and other times we say not. that is because if we run the expriment
of tossing coin an infinite number. we will notice the number of occurrence of heads = the number of 
occurrence of the tails.
"""

def probability(nfaces, trials):
	freq = [0 for f in range(nfaces+1)]
	faces = [f for f in range(1, nfaces+1)]

	for i in range(0, trials):
		freq[random.choice(faces)] += 1

	return [freq[i]/trials for i in range(1, nfaces+1)]


def main() :
	""" Bean machine """
	pascal_triangle(10)
	# r = 0
	# p = 2**1000
	# for i in range(400, 601):
	# 	r += combs[1000, i]/p
	# print(r*100)
	# count = [0 for i in range(0, 13)]
	# print((2**10 - 9)/2**10)
	# r = 0
	# for i in range(0, 11, 2):
	# 	r += combs[10, i]
		
	# print( 2*combs[10, 2]/(2**10) )
	i = 10000000
	while i < 100000000 :
		probs = coin_prob(2, i)
		print(probs, "   diff = ", abs(probs[0]-probs[1]))
		i *= 10

if __name__ == '__main__':
	main()