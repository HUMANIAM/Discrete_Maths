"""
Modular Exponentiation is a fast method to compute b**n % m instead of compute b**n then find b**n %m
we can find represent n by its binary expansion and start with x = 1 and power = b%m then every time
update power and update x where x is the final remainder
"""
import math
some_primes = []

# Greatest common divisor using Euclid's algorithm
def GCD(a, b) :
	return GCD(b, a%b) if b != 0 else a

# create some primes to find prime factorization of number n
def create_some_primes(n) :
	global some_primes
	some_primes.append(2)

	for n in range(3, n, 2) :
		if is_prime(n) : some_primes.append(n)

#prime factorization of number n
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

# primality of number n
def is_prime(n):
	for d in some_primes :
		if n % d == 0 :
			return False
	return True

# Euler totient counts the number of coprimes of a number
# a, b are coprime if GCD(a, b) = 1
def euler_Totient(n) :
	if n == 1 : return 1

	# if n is prime then coprimes n-1. zero isn't coprime with n where GCD(0, n) = n > 1
	if is_prime(n) : return n - 1
	else :
		# prime factorization
		prime_factors = factors_of_n(n)
		coprimes = 1
		for p in prime_factors :
			coprimes *= p-1

		return coprimes

"""
Fermat's little Theorm can be used to make fast modular exponentiation.
pow(a, p-1) == 1 (mod p) when
p is prime
GCD(a, b) = 1 >> a and b are coprime
so the magic will happen in this case:
* p is prime and GCD(a, p) = 1 then pow(a, n) (mod p) = pow(a, n % p-1) mod p
"""

# fast modular of pow(b, e) % m
def FastModularExponentiation(b, e, m):
	# if m is prime and GCD(b, m) = 1 use Fermat little theorem
	if is_prime(m) and GCD(b, m) == 1 :
		e = e % (m - 1)

	# represent e by binary expansion
	bits = bin(e)[2:]
	r = 1
	power = b%m

	# for every component compute mod m and then multiply it by total remainder
	for bit in bits[::-1] :	# from right to left
		if bit == '1' :	r = (r*power) % m
		power = (power* power) % m
		
	return r

# main function	
def main():
	create_some_primes(1000)
	print(FastModularExponentiation(5, 77, 11) == (5**77)%11)

	# print((2**5)%6)
	# print(FastModularExponentiation(34, 60, 77))
if __name__ == '__main__':
	main()