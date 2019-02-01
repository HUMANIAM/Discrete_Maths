"""
Description : A shady person offers you to play a game with him. the game has 3 dices and they are
*********** [1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7] the shady person offers you choose
your dice first then he. and they are both throw your dices and the one with higher number will be the winner

^^ if we start compare dices by list all possabilities and see who will win with every pairs notice what we saw
 * dice1 better than dice 3
 * dice 3 better than dice 2
 * dice 2 better than dice 1

This means that what ever you choose the shady person will win and here is the expriment
"""
from random import randint, seed, choice
from datetime import datetime
seed(datetime.now())

num_rounds = 10**6
dices = [
    [1, 1, 6, 6, 8, 8],
    [2, 2, 4, 4, 9, 9],
    [3, 3, 5, 5, 7, 7]
]


def shady_dice_choice(my_dice):
	if my_dice == 0 : return 1
	if my_dice == 1 : return 2
	if my_dice == 2 : return 0


def dice_game_round():
	global dices

	# the dice that I will choose
	my_dice_index = randint(0, 2)
	my_dice = dices[my_dice_index]

	# the shady man dice
	shady_dice = dices[shady_dice_choice(my_dice_index)]

	# throw dices
	my_number = my_dice[randint(0, 5)]
	shady_number = shady_dice[randint(0, 5)]

	if shady_number > my_number : return False
	return True
		

def play_dice_game():
	global num_rounds
	counts = [0, 0]   # rounds that the shady person win in 0 and I in 1

	#play
	for _ in range(num_rounds) : 
		counts[dice_game_round()] += 1

	#print results
	print("From {} rounds the shady man wins {} rounds and I win {} rounds\
. It is really a scam game".format(num_rounds, counts[0], counts[1]))



def main():
	print("\n\n\n")
	print("{} THE GAME {}".format(' '*50, ' '*20))
	play_dice_game()
if __name__ == '__main__':
	main()