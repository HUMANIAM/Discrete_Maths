"""
Puzzle : serach for the configuration that satisfy this constraints
a --------- b ----------- c
|			|			  |
|			| 			  |
|			|			  |
h --------- i ----------- d
|			|			  |
|			|			  |
|			|			  |
g --------- f ----------- e

(a+b+i+h) = (b+c+d+i) = (d+e+f+i) = (h+i+f+g) = (a+c+e+g) = (b+d+f+h) = 20
* range of numbers from 1 to 9
"""
from itertools import permutations
def main() :
	for p in permutations(range(1, 10)) :
		#check cases
		squ1 = p[0] + p[1] + p[2] + p[3]
		squ2 = p[4] + p[5] + p[6] + p[7]
		squ3 = p[0] + p[4] + p[5] + p[8]
		squ4 = p[1] + p[8] + p[5] + p[6]
		squ5 = p[7] + p[8] + p[2] + p[6]
		squ6 = p[7] + p[8] + p[3] + p[4]

		t = (squ1==20) and (squ2==20) and (squ3==20)
		t = t and (squ4==20) and (squ5==20) and (squ6==20)
		if t : print(p)
if __name__ == '__main__':
	main()