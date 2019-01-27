#special pythahorean triple such that a+b+c=1000 and a2+b2=c2
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math
def check_int(n):
	return int(n)==n
	
for a in range(0,1000):
	b=(1000*(1000-2*a))/(2*(1000-a))
	c=math.sqrt(a**2+b**2)
	if check_int(c) and b>a:
		print(int(a*b*c))
