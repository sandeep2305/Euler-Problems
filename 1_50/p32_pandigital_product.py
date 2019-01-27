'''We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum'''
def reverse_join(str_input):
	return "".join(sorted(str_input))

def comparision(n):
	return n=='123456789'
num=list()
n=int(input())
for a in range(1,n+1):
	for b in range(a,n+1):
		c=a*b
		temp_str=str(a)+str(b)+str(c)
		if len(temp_str)>9:
			break
		if comparision(reverse_join(temp_str)):
			num.append(c)
print(sum(set(num)))
