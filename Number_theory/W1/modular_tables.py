"""
Modular tables are used to reduce the computation of arithematic modular of an expresion
* Multiplication Table some times imply the division table
* Addition table always implies the subtraction table
"""

def multi_modular_table(n):
	mod_table = [[None] * n for _ in range(n)]

	for i in range(n) : 
		for j in range(n):
			mod_table[i][j] = (i*j)%n
			
	return mod_table

def add_modular_table(n) :
	mod_table = [[None]*n for _ in range(n)]

	for i in range(n) :
		for j in range(n):
			mod_table[i][j] = (i + j) % n
	return mod_table

def main():
	for r in add_modular_table(7) : print(r)
if __name__ == '__main__':
	main()