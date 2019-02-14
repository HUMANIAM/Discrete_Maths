"""
one time pad is one of the streaming cipher where using the encryption key exactly one in each 
communication. Using Xoring between the plaintext message and the key we get the ciphertext msg
C = M xor k 						at Alice
M = C xor K = M xor K xor K 		at Bob

* Eve don't understand anything from C message when he receive it from eavesdropping on the communication
between Alice and Bob

* but Alice and Bod make a common mistake by using the same key K several times
* Eve now have C1 = M1 xor K       and  C2 = M2 xor K     then  C = C1 xor C2
* Eve now have ciphertext of the combined messages M1 and M2  C = M1 xor M2
* if you can guess word from M1 or M2 you can easily get the corresponding word in the other msg
* guess word say W and then W' = C xor W at specific position. if the result word is readable
* we guess what it is and using it to discover the remaining part of the other message
* if the W' is not readable shift the crib word W to the next position and repeat the previous steps
"""

AliceMsg = 'secret message'
BobMsg = 'the program'

# convert regular string to hexdecimal string
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


# encrypt message
class Encrypt(object):
	"""docstring for EncryptMsg"""
	# static attrs are accessed through the class. No need to create instances of it
	__privateKey = strToHex("supersecretverys")
	
	# C = s1 xor s2
	@staticmethod
	def xor (s1, s2) :
		# s1 and s2 must have the same length
		assert len(s1) == len(s2)

		res = ""
		for i in range(len(s1)) :
			res += hex(int(s1[i], 16) ^ int(s2[i], 16))[2:]

		return res


	# encrypt the msg from plain text to cipher text using xor operation
	@staticmethod
	def encryptMsg(msg) :
		return Encrypt.xor(strToHex(msg), Encrypt.__privateKey)


"""
Eve situation is a situation where eve has 2 cipher texts encrypted using the same key 2-time-pad
and Eve want to discover the current message from cipher texts C1, C2
"""

def tryGuessingSubstring(substr, msg_len, Cipher_msgs):
	good_guesses = []
	# msg_len = int(len(Cipher_msgs) / 2)

	for pos in range(msg_len - len(substr) + 1):
		guess_pref = chr(0) * pos
		guess_suff = chr(0) * (msg_len - (len(substr) + pos) )
		guesshex = strToHex(guess_pref + substr + guess_suff)

		msg_other_part = hexToStr(Encrypt.xor(guesshex, Cipher_msgs))[pos : pos + len(substr)]

		# the generated part may be good guess or not. we use simple criteria to measure that
		# good guess if it has only space or alphabetic chars
		good = True
		for c in msg_other_part :
			if not c.isalpha() and not c.isspace():
				good = False
				break

		if good :
			good_guesses.append((substr, pos, msg_other_part))

	# print good guesses
	for guess in good_guesses :
		strf = "position: %d, one message part: \"%s\", another message part: \"%s\""
		print( strf % (guess[1], guess[0], guess[2]))


def eve_situation():
	# C1 and C2 messages are encrypted using the same private key
	C1 = Encrypt.encryptMsg("steal the secret")
	C2 = Encrypt.encryptMsg("the boy the girl")
		
	# xoring C1 and C2 gives C = (M1 xor M2)
	C = Encrypt.xor(C1, C2)

	# assert C == Encrypt.xor(C1, C2)

	"""
	Eve now has the xoring between the original msgs. but How does help her?
	* she can do some statistical analysis using her knowledge of English.
	* guess a word for one msg then compute the corresponding characters in C
	* at every position we will do that. every the other part of the msg has meaning chars
	* consider it as part of the msg say C xor GuessWord = " yes " it is really good guess
	* and also readable word if you know english.
	"""

	tryGuessingSubstring(" the ", len("steal the secret"),  C)

	# if we have more msgs then we can construct more parts of the message


# main function
def main():
	eve_situation()
	
if __name__ == '__main__':
	main()