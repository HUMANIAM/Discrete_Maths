""" we have only 2 coins 7, 5 and we are given n we need to find out if we can pay n by only 5 and 7
	coins if yes print only one possible solution

	using recursion to solve the solution
"""

def can_be_paid(n):
	if n == 0 : return True
	if n < 7 and n != 5 : return False
	
	if can_be_paid(n-5) or can_be_paid(n-7): return True 
	return False

def change(amount):
	# base cases
	if amount < 0 : return []
	if amount == 5 : return [5]
	if amount == 7 : return [7]

	subpayment = change(amount-5)
	if len(subpayment) : subpayment.append(5); return subpayment
	else : 
		subpayment = change(amount-7)

		if len(subpayment) : subpayment.append(7); return subpayment

	return []


def main():
	print(change(100))
	
if __name__ == '__main__':
	main()