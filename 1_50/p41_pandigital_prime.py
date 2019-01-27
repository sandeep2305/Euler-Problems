'''Pandigital prime
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?'''
from itertools import permutations

def isPrime(n):
    if n==2 or n==3: 
    	return True
    elif n%2==0 or n<2: 
    	return False
    else:
    	for i in range(3,int(n**0.5)+1,2):   # only odd numbers
    		if n%i==0:
    			return False    
    	return True

n=int(input())
list_num=list()
digits='123456789'
for i in range(n):
	temp_num=digits[:i+1]
	for k in list(set(["".join(m) for m in permutations(temp_num)])):
		if isPrime(int(k)):
			list_num.append(k)
		
print(list_num)
