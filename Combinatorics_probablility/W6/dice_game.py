#									** THE DICE GAME **                                 #
#										***********
"""
Description of the game : there is a poll with N different dices and there are 2 players. The first
------------------------  player pick randomly a dice then the another player pick randomly a dice from
the remaining dices. then they throw the dices the dice with the greater number whose player win

** Notes
**********
There are 2 scenarios
1- there is a dice with higher probability to win comparing with all other dices
	so if we play the game we choose the strategy of choosing first and when we choose we choose
	the dice with the best probability to win.

2- there is no dice with the best probability. so we can let the opponent choose first then we choose
	the dice that better than the dice selected by the opponent (second strategy)

"""
from random import randint, seed, choice
from datetime import datetime
from itertools import product
seed(datetime.now())

num_rounds = 10**1

#********************************
# find the better dice with greater probability to win
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    
    # check all possibilities
    for i in range(6) :
    	for j in range(6) :
    		if dice1[i] > dice2[j] : 
    			dice1_wins += 1
    		elif dice1[i] < dice2[j]  :
    			dice2_wins += 1

    return (dice1_wins, dice2_wins)

#******************************
# find the best dice among N dices
def find_the_best_dice(dices):
	L = len(dices)
	assert all(len(dice) == 6 for dice in dices)

	# rank_table
	rank_table = [[None]*L for _ in range(L)]

	for i in range(L):
		for j in range(L):
			if i == j or rank_table[i][j] != None : continue

			(icount, jcount) = count_wins(dices[i], dices[j])
			if icount > jcount :
				rank_table[i][j] = rank_table[j][i] = i

			elif icount < jcount :
				rank_table[i][j] = rank_table[j][i] = j

			else : rank_table[i][j] = rank_table[j][i] = -1

	# return the best one if exits else return -1
	for i in range (L):
		yes = True
		for j in range(L):
			if i == j : continue

			if rank_table[i][j] != i :
				yes = False
				break

		if yes : return i, rank_table
			
	# no best dice
	return -1, rank_table

#*******************************
# find the best strategy
def compute_strategy(dices):
	assert all(len(dice) == 6 for dice in dices)

	strategy = dict()
	strategy["choose_first"] = True

	# check the first strategy
	the_best, rank_table = find_the_best_dice(dices)
	if the_best == -1 : 
		strategy["choose_first"] = False
	else :
		strategy["first_dice"] = the_best
		return strategy

	# set the second strategy scenarios
	for i in range(len(dices)):
		for j in range(len(dices)):
			if i == j or rank_table[i][j] == i or rank_table[i][j] == -1 : continue
			
			strategy[i] = j
			break

	# return the strategy    
	return strategy

#**********************
# compare 2 dices by playing 1e6 rounds and see which will win more
def compare_two_dices(first, second) :
	global num_rounds
	score1, score2 = 0, 0

	for _ in range(num_rounds) :
		face1 = first[randint(0, 5)]
		face2 = second[randint(0, 5)]

		if face1 > face2 : 
			score1 += 1
		else :
			score2 += 1

	# print results
	if score1 > score2 : 
		print("^ dice {} is better than dice {} with score {} compared to score {}".\
format(first, second, score1, score2))
	
	elif score2 > score1 :
		print("^ dice {} is better than dice {} with score {} compared to score {}".\
format(second, first, score2, score1))

	else :
		print("^ dice {} is like dice {} ".format(first, second))

#*********************************
#test the first strategy
def first_strategy_test(dices, strategy):
	global num_rounds
	winning_rounds, losing_rounds = 0, 0
	dice_index = strategy['first_dice']
	the_best_dice = dices[dice_index]
	remaining_dices = dices[:dice_index] + dices[dice_index+1 :]

	for _ in range(num_rounds):
		opponent_dice = choice(remaining_dices)

		#throw dices
		opponent_dice_side = opponent_dice[randint(0, 5)]
		better_dice_side = the_best_dice[randint(0, 5)]

		if opponent_dice_side > better_dice_side : 
			losing_rounds += 1

		elif better_dice_side > opponent_dice_side :
			winning_rounds += 1

	print("\n\n** After playing the game {} according the first strategy you win {} and the opponent\
 win {}".format(num_rounds, winning_rounds, losing_rounds))

	print("\n** As you can see the first strategy works well")

#*********************************
#test the second strategy
def second_strategy_test(dices, strategy):
	global num_rounds
	winning_rounds, losing_rounds = 0, 0

	for _ in range(num_rounds):
		opponent_dice_index = randint(0, len(dices)-1)
		opponent_dice = dices[opponent_dice_index]
		better_dice = dices[strategy[opponent_dice_index]]

		#throw dices
		opponent_dice_side = opponent_dice[randint(0, 5)]
		better_dice_side = better_dice[randint(0, 5)]

		if opponent_dice_side > better_dice_side : 
			losing_rounds += 1

		elif better_dice_side > opponent_dice_side :
			winning_rounds += 1

	print("\n\n** After playing the game {} according the second strategy you win {} and the opponent\
win {}".format(num_rounds, winning_rounds, losing_rounds))

	print("\n** As you can see the second strategy works well")


#***********************************
# play the game
def play_dice_game(dices, strategy):
	global num_rounds
	print("\n** we will test the strategy  1000000 rounds and see what will happen")

	if strategy['choose_first'] :
		print("\n** We will test the first strategy by choosing the best dice {} first in \
every round then let the other player choose any other dice".format(dices[strategy['first_dice']]))

		first_strategy_test(dices, strategy)

	else :
		print("\n** We will test the second strategy by letting the opponent choose any dice then\
 we choose the better one according to the mentioned scenarios")

		second_strategy_test(dices, strategy)

#******************************
#interface with the user
def dice_game_interface(dices):
	strategy = compute_strategy(dices)
	if strategy['choose_first'] : 
		print("^ use the first strategy and choose every time {}"\
			.format(dices[strategy['first_dice']]))
	else :
		print("^ choose the second strategy as following :")
		for i in range (len(dices)):
			print("** If he choose {} then choose {}".format(i+1, strategy[i]+1))

	strategy_test = input("\n\n^*^ If you want test the strategy then Enter yes : ")
	if strategy_test == "yes" :
		play_dice_game(dices, strategy)
		
#main
def main():
	dices = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
	dice_game_interface(dices)
if __name__ == '__main__':
	main()