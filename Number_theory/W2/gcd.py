"""
gcd using Euclidean algorithm
"""
from fractions import Fraction

def lcm(a, b) :
	def gcd (a, b) :
	# a, b are non_negative
		assert a >= 0 and b >= 0
		while b != 0 :	a, b = b, a%b
		return a

	return a*b / gcd(a, b)

def squares(n, m):
	assert n >= 0 and m >= 0
	a, b = n, m

	# gcd(n, m)
	while b != 0 :	a, b = b, a%b

	return int(n/a * m/a)

def lcm(a, b) :
	return a*b / gcd(a, b)

def gcd (a, b) :
	# a, b are non_negative
	assert a >= 0 and b >= 0
	while b != 0 :	a, b = b, a%b
	return a

def naive_gcd(a, b):
	# a, b are non_negative
	assert a >= 0 and b >= 0

	if a == 0 or b == 0 : return max(a, b)

	for d in range(min(a, b), 1, -1) :
		if a % d == 0 and b % d == 0 : return d 

	return 1
def gcd_tes(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a - b
    else:
      b = b - a

  return max(a, b)

def main():
	k = 22
	for y  in range(5, 11):
		if (22 - 3*y) % 5 == 0 :
			print((22 - 3*y) / 5); break;
	while True:
		a, b = input().split()
		print(lcm(int(a), int(b)))

if __name__ == '__main__':
	main()