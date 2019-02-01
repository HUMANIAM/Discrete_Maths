"""
Description : MontyHall is a problem where you have 3 doors behind one of them a car and behind the
***********  two others there is a goat. if you pick a door you have two choices switch or not switch
which strategy has max probability to win.
"""

from itertools import permutations
from itertools import product
from itertools import combinations
import collections
import numpy as np

# first value : the selected door , second value : the door has the prize
x = np.random.random_integers(low = 1, high = 3, size = (5,2))

def montyHall():
	[[sel_door, win_door]] = np.random.random_integers(low = 1, high = 3, size = (1,2))
	opt_open_doors = [i for i in range(1,4)]   # which door monty will open

	# if the selected door has the prize then monty can open anyone of the other doors.
	if sel_door == win_door :
		opt_open_doors.remove(sel_door)
		open_door = np.random.choice(opt_open_doors)
		opt_open_doors.remove(open_door)
		switch_door = opt_open_doors[0]

	# if they are different then monty must open the remaining door
	else :
		opt_open_doors.remove(sel_door)
		opt_open_doors.remove(win_door)
		open_door = opt_open_doors[0]
		switch_door = win_door

	if switch_door == win_door :
		switch, not_switch = 1, 0
	else:
		switch, not_switch = 0,1

	return switch, not_switch

# simulate monty hall with switching startegy
def simulate(N):
	results = [0, 0]
	for i in range(N):
		s, ns = montyHall()
		if s : results[1] += 1
		if ns : results[0] += 1
	
	print("* In {} expriment using the switching strategy you win in {} and lose \
in {}".format(N, results[1], results[0]))

#main 
def main():
	simulate(1000000)
	# for i in range (50, 100000, 50):
	# 	simulate(i)
if __name__ == '__main__':
	main()
