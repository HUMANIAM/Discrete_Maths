"""Problem Description : you are give source word and target word and your task is find the min number of swaps
  ********************  to reach from the source to the destination 
  Technique : Gready algorithm
"""

def neighbor_trans (src, des) :
	src, des = [c for c in src], [c for c in des]
	transports = []

	for i in range(0, len(src)) :
		try:
			if src[i] != des[i] :
				for j in range (i+1, len(src)) :
					if src[j] == des[i] :				# postition of the char in the src
						# move it to the correct place
						for k in range(j, i, -1) :
							transports.append((k-1, k))
							src[k-1], src[k] = src[k], src[k-1]
						break
		except Exception as e:
			print(i, j)
			raise e
		
	return transports

def non_neighbor_trans(src, des):
	src, des = [c for c in src], [c for c in des]
	transports = []

	for i in range(0, len(src)) :
		try:

			if src[i] != des[i] :
				for j in range (i+1, len(src)) :
					if src[j] == des[i] :
						transports.append((i, j))
						src[i], src[j] = src[j], src[i]
						break

		except Exception as e:
			print(i, j)
			raise e
		
	return transports
  
def interface() :
	# src = input("Enter the source sentence :")
	# des = input("Enter the destination sentence :")
	src, des = "MARINE", "AIRMEN"
	trans = neighbor_trans(src, des)
	
	print("****************************")	
	print ( 'To convert "{}" >> "{}"'.format(src, des))
	print ("You need : {} Translations".format(len(trans)))
	print("^^^^^^^^^^^^^^^^^^")

	print ("STEPS From Left To Right\r\n________")

	for pair in trans :
		print(pair, " : ", end = "   ")
		print("* {} with {}".format( src[pair[0]], src[pair[1]]))

def main():
	print(len(neighbor_trans("0324567198", "0123456789"))%2)
	# interface()

if __name__ == '__main__':
	main()