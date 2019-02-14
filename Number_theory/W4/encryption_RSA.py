"""
RSA is the most frequently used algorithm in modern technology to encrypt data. It is public key
cryptosystem where to send a message to somebody you need to encrypt it using his public key
then he use his private key to decrypt it.

* The algorithm is based on Fast Modular Exponentiation algorithm
* Bob has 2 keys Private key and public key
* public key : is (Exponent e)(Modulo n=pq)
* Bob publishes his private key e and n. so everyone need to communicate with him will use
* them to encrypt the message C = M**d mod n
* Message must be coprime with the modulo so module must fit very large to fit large msg
"""
import math

# gcd(a, b)
def gcd(a, b):
	return a if b==0 else gcd(b, a%b)

# fast modular of pow(b, e) % m
def FastModularExponentiation(b, e, m):
	# represent e by binary expansion
	bits = bin(e)[2:]
	r = 1
	power = b%m

	# for every component compute mod m and then multiply it by total remainder
	for bit in bits[::-1] :	# from right to left
		if bit == '1' :	r = (r*power) % m
		power = (power* power) % m
		
	return r

# Extended Euclidean algorithm
def ExtendedEuclid(a, b):
  assert a >= 0 and b >= 0 
  if b == 0:
    d, x, y = a, 1, 0
  else:
    (d, p, q) = ExtendedEuclid(b, a % b)
    x, y = q, p - q * (a // b)

  assert a % d == 0 and b % d == 0
  assert d == a * x + b * y
  return (d, x, y)

# convert message to hex string
def strToHex(str):
	charsHex = ''
	for c in str :
		chex = hex(ord(c))[2:]   # '0xff' remove 0x
		if len(chex) == 1 :
			chex = '0' + chex

		charsHex += chex
	return charsHex

# convert hexadecimal string to regular string
def hexToStr(strHex) :
	regStr = ""
	for p in range(0, len(strHex)-1, 2) :
		regStr += chr(int(strHex[p:p+2], base = 16))
	return regStr

# convert from str to int
def ConvertToInt(str) :
	return int(strToHex(str), base = 16)

# Encrypt the msg using RSA algorithm
def Encrypt(message, modulo, exponent):
	return FastModularExponentiation(ConvertToInt(message), exponent, modulo)

# Decrypt the msg using RSA algorithm
def Decrypt(cipherMessage, e, p, q) :
	n = p*q
	qn = (p-1)*(q-1)

	# GCD(e, (p - 1)(q - 1)) = 1 they are coprime so e is invertable
	gcd, x, y = ExtendedEuclid(e, qn)
	d = x

	# d > 0 where minp = 2 and minq = 3
	d %= qn
	
	# after some analysis of the ciphertext C and it is relation to M we found
	# M = C**d (mod n)

	M = FastModularExponentiation(cipherMessage, d, n)
	return hexToStr(hex(M)[2:])
##################################################
# 1- simple attack
#*****************
def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
	for pmsg in potential_messages :
		if ciphertext == Encrypt(pmsg, modulo, exponent) :
			return pmsg
	return None


# 2- small primes
#****************
def DecipherSmallPrime(ciphertext, modulo, exponent):
	# find the small prime
	LIMIT = 1000000
	for small_prime in range(2, LIMIT):
		if modulo % small_prime == 0 :
			big_prime = modulo // small_prime
			return Decrypt(ciphertext, exponent, small_prime, big_prime)

	# there is no small prime both are so big
	return "don't know"
	

# 3- small difference between p and q
# **********************************
def DecipherSmallDiff(ciphertext, modulo, exponent):
	# n + ((p-q)/2)**2 = ((p+q)/2)**2
	LIMIT = 5000
	for df in range(1, LIMIT) :
		rhsSqrt = int(math.sqrt(4*modulo + df**2))
		p = (rhsSqrt + df) / 2

		if p - int(p) == 0 :
			q = modulo // int(p)
			return Decrypt(ciphertext, exponent, int(p), int(q))
	
	# big difference
	return "don't know"


# 4- insufficient randomness
# **************************
def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
  # the same seeding of the RNG results in device1 and device2 has the same p 
  common_p = gcd(first_modulo, second_modulo)
  if common_p == 1 :
  	return ("unknown message 1", "unknown message 2")

  first_q  = first_modulo // common_p
  second_q = second_modulo // common_p
  msg1 = Decrypt(first_ciphertext, first_exponent, common_prime, first_q)
  msg2 = Decrypt(second_ciphertext, second_exponent, common_prime, second_q)
  return (msg1, msg2)


# 5- Hastad's Attack (Broadcast the same message using the same exponent)
#********************
def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
    r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
    msg = int(math.sqrt(r))
    return hexToStr(hex(msg)[2:])

# 6- analysis based attacks
#**********************
"""
There are many other attacks based on analysis of 
Time to decrypt the message
Power consumption to decrypt the message
Error return from the vicitm (trial and error)
"""
def main():
	print(int("0x" + strToHex("aa"), 16))
	p = 1000000007
	q = 1000000009
	n = p * q
	e = 239
	ciphertext = Encrypt("attack", n, e)
	message = DecipherSmallDiff(ciphertext, n, e)
	print(ciphertext)
	print(message)

if __name__ == '__main__':
	main()