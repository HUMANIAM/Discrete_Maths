"""your are given n integers labeled from 1 to n and you need to choose subset of numbers
	where there is no 2 numbers are x and 2x we need to find the max subset
"""
import math

n = int(input())
chains = []
for i in range(1, n+1, 2) :
	chains.append([i])
	j = int(i/2)
	k = i * 2
	while k <= n : chains[j].append(k); k = k*2

total = 0
for ch in chains :	total = total + math.ceil(len(ch) / float(2)) 
print(total)
	