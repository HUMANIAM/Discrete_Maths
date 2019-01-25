from itertools import permutations
from itertools import product
from itertools import combinations

def truthTable (n) :
	return list(product([True, False], repeat = n))

def findSolution():
	print( len( list( product(range(10), repeat = 4) ) ) )
	p = 0
	for d in product(range(10), repeat = 4) :
		ok = True
		for i in range(1, len(d)) :
			if d[i] <= d[i-1] : ok = False; break
		
		p = p + 1 if ok else p
		if ok : print(d)
	
	print(p)

def main():
	print(25*25*25)
	print(len(list(combinations(range(1,26), 3))))
	# print(truthTable(1))

if __name__ == '__main__':
	main()