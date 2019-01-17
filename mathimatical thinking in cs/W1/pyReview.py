import sys

			#out/input 
# print("hello world")
# name = input("Your name : ")
# age = input("Your age : ", end="\n")
# print("print hello ", name, "you have ", age, "years old")

######################################################
		#read file/and write it in anthor one
# flname = input("File Name :")
# fhd = open(flname, "w")
# fhd.write("hello world\n")
# fhd.close()

# print(open(flname, "r").read())
#######################################################

			#looping
"""
for x in range(1,10):
	if x>=1 and x<5 :
		print(x, " : small")
	elif x>=5 and x<=7:
		print(x, " : meduim")
	else:
		print(x, " : large")
		i = 1
		while(i<=x):
			print(i, end=" ")
			i += 1
		print()
	pass
a, b = 5, 6
print(a, b);
"""

######################################################
				#some info about python
"""
1- has only four standard data types {string, number, list, dict, tuple}
2- numbers are (float, int(long type), complex)
"""
############################################################
						#python strings
# 1- slice is used [:]   2- append by + operator  3- * operator is the repetition operator
# str1 = "a"*10
# print(str1[1:], '\n', str1[:5], '\n', str1[:-1], '\n')
##############################################################
						#python lists
# 1-can contain any types of elements		2- use * times to dublicate the list 3- you can use slicing like strings
# 4- use + to concatenate two lists
# lst = ["hello", 1, 1.5]
# print(lst*2)
# print(lst[1:])


#######################################################
						#Tuples
# 1- like lists but is immutable (read only data type) surrounded by () not [] like in list
# tuples is exactly like lists but they are read only data type
# tup = (1, 1.2, 'a', "hello")
# print(tup[0], tup[1:-1], tup*2)

#############################################################3
						#dictionary
# dict = {}
# dict[1] = "ahmed"
# dict["ahmed"] =1
# print(len(dict), dict[1])
# print(list(dict.items()))
# print(list(dict.keys()))

#####################################################################
					#converting
# 1- int(x, [,base])  2-float()   3- str()  4- complex(real, [,imag]) 5-tuple(s) 6- list() 7-dict()
# 8-repr(x)	9-eval(str)  10-set(s) 11-chr(int) 12-ord(ch>int) 13-unichr(int) 14-hex(int) 15-oct(x)

#####################################################################
					#arithematic/comparison/assignment/bitwise/logical operators
# 1- (+, -, *, /, **, //floor division) 2- (==, !=, >, <, <=, >=) 3-(+=, -=, *=, /=, //=, **=)
# 4- (&, |, ~, ^, <<, >>) 5- (and, or, not) 
						#membership/identity operators
# 1- (in, not in)  2-(is, is not)  

######################################################################
							#Iterator and Generator					
# Iterator is an object which allows a programmer to traverse 
# through all the elements of a collection, regardless of its specific implementation.
# an iterator object implements two methods, iter() and next().

# EX:
"""
list = [1, 2, 3, 4]; it = iter(list); 

while True:
	try:
		print(next(it))
	except Exception as e:
		break
"""
# or
"""
for x in it:
	print(x)
"""
# A generator is a function that produces or yields a sequence of values using yield method.
# When a generator function is called, 
# it returns a generator object without even beginning execution of the function.
# When the next() method is called for the first time, the function starts executing 
# until it reaches the yield statement, which returns the yielded value. The yield keeps track i.e.
# remembers the last execution and the second next() call continues from previous value. 

#in few words, generator is a function but this function uses yield key word instead of return
#when you call it it returns generator object(iterator) before the execution of the function
#when you call next(it) the function is executed untill the yield line
#to show the importance of generator. you need to read the next example
"""
def gen_records(path="hello.txt"):
    with open(path) as handle:
        record = {}
        for line in handle:
            if line == '\n':
                yield record 		#=return record
                record = {}
                continue
            key, value = line.rstrip("\n").split(" : ", 1) #one split
            record[key] = value

for record in gen_records('hello.txt'):
    print("{} had {} years old".format(
        record["name"], record["age"]))
"""
#to write efficient code that handle data part by part you need to use generator
#this is a good technique to handle and processing large streaming of data through socket conn

##############################################################################
"""						#sets and lamda
set = {1, 1, 5}
# lambda is anonymous function 
# lambda arguments : expression
x = lambda a : a + 10
print(x(5))
"""
###############################################################################
								#numbers
#convert types 1-int(), float(), complex(x), complex(i, h), long()
"""import math
a = 5; del a;
a = 5; a=0x5; a=0x9;

#mathematical functions
print("abs(-5) : ", abs(-5))
print("ceil(5/2) : ", math.ceil(5.0/2.0))
print("exp(5) : ", math.exp(5))
print("fabs(5) : ", math.fabs(-5))
print("floor(5/2) : ", math.floor(-5/2))
print("log(5) : ", math.log(5))
print("max() : ", max(5, 10, 20))
print("sqrt() : ", math.sqrt(25))
print("pow(5, 2) : ", math.pow(5, 2))

"""
#################################################################################
							#Random Numbers Functions
# Random numbers are used for games, simulations, testing, security, 
# and privacy applications. Python includes the following functions that are commonly used.
import random, math
list = [1, 2, 3]

###choice(seq) : returns a random item from a list, tuple, or string.
print(random.choice(list))

###random(): returns a random float from 0.0 to 1.0
print(math.floor(random.random()*100))

###seed(x, y): calls this function before calling any other random functions. why? it intialize the
		# basic random number generator. where random generator is not already random but deterministic
		#random value is generated by doing some operations on the pervious generated number but at the
		#the beginning there is no previous number you use seed funtion to set this number
		#the current time is a frequently-used seed as it is unique
		#x is the previous random value, y is the version of x 1 is int(x), 2 is hash of int(x)
# random.seed(5, 1) 

###shuffle(seq) : randomize the items of seq
random.shuffle(list)
print(list)

###uniform(x, y) : return float r where x<=r<y
print(random.uniform(5, 6))


