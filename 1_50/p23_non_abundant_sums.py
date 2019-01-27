'''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers'''
from time import time
a=time()
k=28123
def factor(i):
	temp_facto=[1]
	for j in range(2,int(i/2)+1):
		if i%j==0:
			temp_facto.append(j)
	return sum(temp_facto)

def checknum(i):
	if i<factor(i):
		return True
	else:
		return False
abundent_num=set()
post_int=list(range(1,k+1))
for i in range(2,int(k)+1):
	if checknum(i):
		abundent_num.add(i)
z=list(abundent_num)
k=set([z[i]+z[j] for i in range(len(z)) for j in range(i,len(z))])
sumall=0
for i in post_int:
	if i not in k:
		sumall+=i
print(sumall)
d=time()
print(d-a)
