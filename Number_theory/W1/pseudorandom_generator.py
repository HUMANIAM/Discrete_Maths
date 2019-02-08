"""
In fact, when computer generate random number it doesn't generate it random where the procedure
is systematic method so we call this numbers are psudorandom rather than random.

there are many algorithms used to generate psuedorandom numbers
1- Linear congruentail method. we choose 4 integers
	a : multiplier   2 <= a < m
	m : modulus		 
	c : increment    0 <= c < m
	x0: seed         0 <=  x0 < m   initial value for the psuedo random generator

  Xn+1 = (a*Xn + c) mod m

2- pure multiplicative generator use c = 0
"""

import random
# every time you run the program you get the same order of random numbers because X0 is fixed
random.seed(0)  

class congruential_pseudo_gen(object) :
	
	def __init__(self):
		self.__a = 7**5
		self.__c = 1
		self.__m = 2**31
		self.__x0 = None
		self.__Xn = None

	def seed(self, x) :
		self.__x0 = x
		#formula is (a * Xn-1 + c)  mode m
		self.__Xn = (self.__a * self.__x0 + self.__c) % self.__m

	def random(self, f, t) :
		if self.__Xn is None : return None

		r = self.__Xn
		self.__Xn = (self.__a * self.__Xn + self.__c) % self.__m
		return f + r % (t - f)


def built_in_generator(n, f, t):
	randoms = []
	for _ in range(n):
		randoms.append(random.randint(f, t))

	return randoms

def main():
	print(-1%2)
	exit(0)
	rg = congruential_pseudo_gen()
	rg.seed(0)
	for _ in range(10000000) :
		r = rg.random(7, 12)
		if r < 7 or r > 12 : print("failed case"); break;
	
if __name__ == '__main__':
	main()
