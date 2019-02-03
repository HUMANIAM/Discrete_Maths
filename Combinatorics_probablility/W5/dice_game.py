"""
In this dice game Bob and Alice has 2 unusual dices Alice dice = [3, 3, 2, 2, 2, 2] but Bob dice 
[1, 1, 1, 1, 6, 6]. we need to see who will win more Alice or Bob
if we depend on the expected value EA < EB then bob will win more but that is not right where by observing
the dice of Bob we can not that he has in every trial probability to lose by 2/3 and 1/3 to win
and in every trial is independent of the previous trials so Alice will win more
"""

from random import randint, seed
from datetime import datetime
seed(datetime.now())
num_rounds = 10**6
Alice, Bob = 0, 0
alice_dice = [2, 2, 2, 2, 3, 3]
bob_dice = [1, 1, 1, 1, 6, 6]

def who_win_more() :
	global Alice, Bob
	for _ in range(num_rounds) :
		rv_alic = alice_dice[randint(0, 5)]
		rv_bob = bob_dice[randint(0, 5)]

		if rv_bob > rv_alic : 
			Bob += 1
		else : Alice += 1

	print("In {} Alice win {} and Bob win {}".format(num_rounds, Alice, Bob))

def main():
	who_win_more()	
if __name__ == '__main__':
	main()