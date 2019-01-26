from itertools import permutations
from itertools import product
from itertools import combinations
import collections
import numpy as np

"""
rule of sum : you have 2 sets A, B the |A+B| = |A| + |B| - |AB|
***********
"""
def rule_of_sum(A, B) :
	return set(A+B)

"""
rule of product : you have 2 sets has N, M objects respectively then there are NM pairs
**************
"""

def self_product(A, n) :
	return list(product(A, repeat = n))

def rule_of_product(A, B):
	if type(B) == int :
		return self_product(A, B)

	return list(product(A, B))


"""
Tuples : is the number of sequences of length k composed out on n symbos n**k
******
"""
def tuples(A, n):
	if type(A) == str :
		return [''.join(tuple) for tuple in self_product(A, n)]
	return self_product(A, n)

"""
K-permutation : the number of sequences of length k with no repetion composed
************** out of n symbols n!/(n-k)!
"""
def k_permutation(A, k) :
	if type(A) == str :
		return [''.join(p) for p in permutations(A, k)]
	return list(permutations(A, k))

"""
k-compination : the number of subsets of length k with no repetion from n symbols
*************   (n) = n!/(k! * (n-k)!)
				(k)
"""
def k_compination(A, k) :
	if type(A) == str :
		return [''.join(c) for c in combinations(A, k)]
	return list(combinations(A, k))

"""
problem : number of games
********
Descritpion : you have n teams and each team must play the other teams exactly one match
********      what is the number of matches
"""
def games(n):
	return set(k_compination(range(1, n+1), 2))

"""
problem : number of ways to divide ten persons into two teams and every team has 5 persons
*******
solution : the number of ways to select the first team is 10 choose 5 once you choose the first
*******    team the second team is determined at the same time so we hav (n c) of partitions
but that not correct because if you select A as the first team the B as the second team
you also choose B as the first team and A as the second team so solution will be have of number
of choices
"""
def divide_into_teams(n, k) :
	teams = list( combinations( range(1,n+1), k) )
	games = []
	for i in range(0, len(teams)-1) :
		for j in range(i+1, len(teams)):
			dif = len(np.setdiff1d(teams[i], teams[j], assume_unique = True))
			if dif == k :
				games.append([teams[i], teams[j]])

	return games

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
Binomial coefficients : (a+b)^n = (n 0) a^n + (n 1) a^(n-1) + ----------- + (n n) b^n 
"""
def binomial_coefficients(n, a, b) :
	global combs
	coeffs = []
	for k in range(n+1) :
		coeffs.append(combs[(n, k)] * (a**(n-k)) * (b**k))

	return coeffs

"""
problem : you have number of 4 digits what is the size of these numbers that contains
******   at least 7 digit in the 4 digits
"""
def seven_numbers(n):
	nums = []
	for p in product(range(10), repeat = n) :
		if 7 in p : nums.append(p)

	return nums


"""
problem : 4 digit number with increasing order 
"""
def increasing_number(n):
	nums = []
	for p in product(range(10), repeat = n) :
		odd, even = 0, 0
		for i in p :
			if i%2 : 
				odd += 1
			else : even += 1

		if odd == even :
 			nums.append(p)

	return nums
def main():
	print(increasing_number(6)[0])
if __name__ == '__main__':
	main()