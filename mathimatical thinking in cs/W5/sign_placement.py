"""Problem Description : 
you are given sequence of numbers and target sum you need to put (+ or -) to get the 
target sum
"""
ADD, SUB = 1, 0
summ = 0

def gready_solution(nums, tar, signs):
	summ = 0
	for i in range(0, len(nums)):
		if summ < tar :
			signs[i], summ = ADD, (summ + nums[i])
		else :
			signs[i], summ = SUB, (summ - nums[i])
	return summ

def findSigns(nums, tar, signs, s = 0) :
	global summ
	# print("sum : ", summ, " signs : ", signs)
	if s == len(nums) and summ == tar : return True
	elif s == len(nums) : return False

	for i in range(0, 2) :
		signs[s] = i

		# if it's negative sign
		if i == 0:
			summ -=  nums[s]
			if findSigns(nums, tar, signs,  s+1) : return True
			summ += nums[s]
		#if it is positive sign
		else :
			summ += nums[s]
			if findSigns(nums, tar, signs,  s+1) : return True
			summ -= nums[s]

	signs[s] = None
	return False

def mapsign (x) :
	if x is None : return x
	if x : return '+'
	return '-'		

def main():
	# N = int(input())		# number of numbers
	# nums = [int(input()) for i in range(0, N)]	#numbers
	# tarsum = int(input())	#target sum
	global summ
	N = 9
	nums = [i for i in range(1, N+1)]
	not_found = []
	
	for i in range (-45, 46, 2):
		summ = 0
		signs = [None] * (N)
		ok = findSigns(nums, i, signs)
		if not ok : not_found.append(i)
		# if ok : print(i , " : ", list(map(mapsign, signs)))
	print(not_found)
	
if __name__ == '__main__':
	main()