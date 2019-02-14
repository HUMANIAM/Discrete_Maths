"""
prime number : is a number that is divisable by 1 and only itself
composite number : is not a prime number
* any number can be represents by factors of only type prime
* if n is a composite number then n has a prime divisor <= sqrt(n)
* there are infinitely many primes
* a, b are relatively prime if gcd(a, b) = 1
* the integers a1, a2, a3, ......., an are pairwise relatively prime if gcd(ai, aj) = 1
"""
import math

some_primes = []
def is_prime(n):
	h = math.ceil(n/2)
	for d in range(2, h) :
		if n % d == 0 :
			return False

	return True

def create_some_primes(n) :
	global some_primes
	for n in range(2, n) :
		if is_prime(n) : some_primes.append(n)

def factors_of_n(n):
	global some_primes
	assert n > 1
	factors = []
	p = 0

	while not is_prime(n):
		while n % some_primes[p] != 0 : p += 1

		# reduce n 
		while n % some_primes[p] == 0 : 
			factors.append(some_primes[p])
			n = int(n/some_primes[p])

	if n != 1 : factors.append(n)
	return factors


def main():
	print(is_prime(239))
	create_some_primes(1000)
	# print(factors_of_n(87))
if __name__ == '__main__':
	main()