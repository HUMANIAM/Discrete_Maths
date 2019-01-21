"""Problem Description:
Suppose there is a sequence of 20 cells, the first cell contains number 1 and the last cell 
contains 50. We would like to fill all cells with integer numbers in such a way that 
numbers in the neighbouring cells differ by at most kk. For which minimal kk this is possible?
"""

f, t = 1, 50

k = 3
print(1)
for i in range(19) : print(k*i + 1)
