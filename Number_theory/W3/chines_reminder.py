"""
Chines Reminder theorm : if GCD(a, b) = 1 then for any reminder Ra, Rb there exist a number n such
********************** that n%a = Ra and n%b = Rb. How can we find this number.
n = Ra * Ma * Ya + Rb * M2 * Y2 + ............+ Rk * Mk * Yk
M = a*b*c*......*z
Ma = M without a
Ya = inverse of M without a
check 
when we divide n by a all terms contains a except the first one so remainders are zero except the
first term. from the first term we need Ra as a remainder then (Ma * Ya) % 1 must be 1
"""
import math
from itertools import combinations

def gcd(a, b) :
	return a if b == 0 else gcd(b, a%b)

def ExtendedEuclid(a, b):
  assert a >= 0 and b >= 0 

  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = ExtendedEuclid(b, a % b)
    x = q
    y = p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

""" given set of remainders and set of devisors we will find n that satisfies 
all this moduler relationships
"""
# a and b are coprime if GCD(a, b) = 1
def relatively_primes(nums) :
	for p in combinations(range(len(nums)), 2) :
		if gcd(nums[p[0]], nums[p[1]]) != 1 :
			return False
	return True


def ChineseRemainderTheorem(remainders, divisors):
	# all divisors must be coprime where aX + bY = 1 or GCD(a, b) = 1 so d*x is invertable
	if not relatively_primes(divisors) :
		return -1     # -1 means they are not relatively prime

	"""
	m = d1*d2*......dk
	Mj = m/dj
	Mj*Yj = 1 mod dj
	n = r1 * M1 * Y1 + ........... + rk * Mk * Yk
	"""

	m, Mj, Yj = 1, [], []
	for d in divisors : m *= d
	for d in divisors : Mj.append(m/d)

	# compute inverse multiplicative modular of Mj mod dj. Mj and dj are coprime 
	for i in range(len(divisors)):
		d, x, y = ExtendedEuclid(Mj[i], divisors[i])
		Yj.append(x)

	# compute n
	n = 0
	for j in range(len(divisors)) :
		rj = remainders[j]
		mj = Mj[j]
		yj = Yj[j]
		n += rj * mj * yj

	# find n where 0 < n < m
	if n < 0 :
		n = (math.ceil(-n/(m)) * m + n) % m
	else : 
		n %= m

	# assert that the suggested number satisfies all moduli relations
	for i in range(len(remainders)) :
		assert n % divisors[i] == remainders[i]

	return int(n)

def main():
	print(ChineseRemainderTheorem([2, 2, 2, 2], [4, 5, 7, 11]))


if __name__ == '__main__':
	main()