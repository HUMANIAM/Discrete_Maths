# n! = n * (n-1)* (n-2)* ......... 2 * 1
# one must ensure that the program will terminate after a finite number of steps
# infinte recursion results in stack overflow or maximum recursion depth exceed
# if parameter base case based on not change program will not terminate

def factorial(n) :
	assert(n > 0)
	if n == 1 : return 1		# base case
	return n * factorial(n-1)

def main():
	n = int(input("Enter the number :"))
	print(factorial(n))

if __name__ == '__main__':
	main()