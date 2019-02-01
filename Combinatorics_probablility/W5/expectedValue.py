from random import randint, seed
from datetime import datetime

seed(datetime.now())

num_rounds = 10**6
sum_of_values = 0

times = [0 for _ in range(7)]
for _ in range(num_rounds):
	x = randint(1, 6)
	times[x] += x
	sum_of_values += x
    
print("The average is {}".format(sum_of_values/(num_rounds*1.0)))
print("E[X] = {}".format(21/6.0))
print(times[1:])