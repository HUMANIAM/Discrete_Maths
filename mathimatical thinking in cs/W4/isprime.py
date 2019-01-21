"""Number is prime if it is advisable by only itself and 1 or there are no two smaller numbers 
	whose product equal to the number
"""

def isPrime(n):
	h = n/2 + 1
	for i in range(2, int(n/2) + 1, 1) :
		if n%i is 0 : return False
	return True

def main():
	print(isPrime(int(input())))
	
if __name__ == '__main__':
	main()