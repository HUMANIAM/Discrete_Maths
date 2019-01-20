""" The Hanoi tower. you have 3 towers 0, 1, 2 and n discs. these discs are put from smaller 
in the top to the greater in the bottom. you are asked to move all n discs
from 0 tower to another tower under 2 constriants
1- don't put large disc above smaller one
2- only one move at a time
Application on recursion
"""
m = 0
fmt = "move disc {} to tower {} "

def hanoi_tower(n, src = 0, targ = 2, helper = 1):
	global m, fmt

	#base case
	if n == 1 : print(fmt.format(n, targ)); m += 1; return
	
	hanoi_tower(n-1, src, helper, targ)
	print(fmt.format(n, targ)); m += 1;
	hanoi_tower(n-1, helper, targ, src)
	
def main():
	n = int(input())
	assert(n < 70)
	hanoi_tower(n)
	print("Number of Moves : ", m)

if __name__ == '__main__':
	main()