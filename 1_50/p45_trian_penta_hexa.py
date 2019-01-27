'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''
import math

def isTriangleNum(n):
	z=(math.sqrt(8*n+1)-1)/2
	if int(z)==z:
		return True
	else:
		return False
		
def isPentagonalNum(n):
	z=(math.sqrt(24*n+1)+1)/6
	if int(z)==z:
		return True
	else:
		return False
		
def hexagonalNum(n):
	return (n*(2*n-1))
	
count=0
num=1
while count<3:
	gen_num=hexagonalNum(num)
	if isTriangleNum(gen_num) and isPentagonalNum(gen_num):
		print(gen_num)
		count+=1
	num+=1
