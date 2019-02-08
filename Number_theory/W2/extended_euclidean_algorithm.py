"""
as we see before the gcd(a, b) can be computed efficiently in O(log(b)) using the Eucledian algorithm
we can use also the same algorithm to compute the multiplicative inverse of a mod b
d = gcd(a, b) and d can be represented by the next formula
d = a*x + b*y >> d = b*p + (a%b)*q
a%b = a - (a // b) * b
d = a*q + b*(p - a//b * q)
x = q, y = p - a//b * q
"""

def extended_gcd(a, b):
  assert a >= 0 and b >= 0 

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = extended_gcd(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

def modular_division(a, b, n) :
	d, x, y = extended_gcd(a, n)
	assert a >= 0 and b >= 0 and d == 1
	return (b*x) % n


def main():
	r = modular_division( 2, 7, 9) 
	print(r)
if __name__ == '__main__':
	main()