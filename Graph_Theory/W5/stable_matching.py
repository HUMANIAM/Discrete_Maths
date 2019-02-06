"""
In this program we will implement the Gale-Shabely algorithm which is used to find the stable matching
(exactly the perfect matching). 
"""

def stableMatching(n, menPreferences, womenPreferences):
# Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n                      
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n                      
    # Each man made 0 proposals, which means that 
    # his next proposal will be to the woman number 0 in his list
    nextManChoice = [0] * n                       
    
    # While there exists at least one unmarried man:
    while unmarriedMen:
        # Pick an arbitrary unmarried man
        he = unmarriedMen[0]                      
        # Store his ranking in this variable for convenience
        hisPreferences = menPreferences[he]       
        # Find a woman to propose to
        she = hisPreferences[nextManChoice[he]] 
        # Store her ranking in this variable for convenience
        herPreferences = womenPreferences[she]
        # Find the present husband of the selected woman (it might be None)
        currentHusband = womanSpouse[she]         
        
        # Look at the situation from the view of the woman
        # what is the preference between the current husband and the proposed man
        currHus_pos, propsHus_pos = -1, -1
        if currentHusband is not None :
        	currHus_pos = herPreferences.index(currentHusband)
        	propsHus_pos = herPreferences.index(he)

        # woman accept the proposal if she doesn't has a husband or the proposed husband better
        if currentHusband is None or propsHus_pos < currHus_pos:
        	womanSpouse[she] = he 			# update husband of this woman
        	manSpouse[he] = she 			# update wife of this man
        	nextManChoice[he] += 1 			# update the next choice for the current man
        	unmarriedMen.remove(he)         # remove the current man from unmarridmen list

        	if currentHusband is not None :    # if he is a better husband
        		unmarriedMen.append(currentHusband)    # append the current husband to unmarried list
        		manSpouse[currentHusband] = None       # now current husband don't have wife

        else :     
        	nextManChoice[he] += 1 # rejected by the current woman so select another one
        
    return manSpouse
    


def main():
	l = [1]
	if l : print("hello world")
	# You might want to test your implementation on the following two tests:
	assert(stableMatching(1, [ [0] ], [ [0] ]) == [0])
	assert(stableMatching(2, [ [0,1], [1,0] ], [ [0,1], [1,0] ]) == [0, 1])

if __name__ == '__main__':
	main()