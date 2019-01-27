'''It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?'''
#z=x+2*y^2
#y=sqrt(z-x)/2
import time
import math

def isPrime(n):
    if n==2 or n==3: 
    	return True
    elif n%2==0 or n<2: 
    	return False
    else:
    	for i in range(3,int(math.sqrt(n))+1,2):   # only odd numbers
    		if n%i==0:
    			return False    
    	return True
 
initial=time.time()   	
num=3
prime_list=[2]
count=0
while count<1:
	if isPrime(num):
		prime_list.append(num)
	else:
		#if not any([True for k in range(1,int(num**(1/2))) for i in prime_list if num==i+2*k**2 ]):
			#count+=1
			#print(num)
		flag=False
		for i in prime_list:
			for k in range(1,int(math.sqrt((num-i)/2)+1)):
				if num==i+2*k**2:
					flag=True
					break
			if flag:
				break
		else:
			print(num)
			count+=1
	num+=2
final=time.time()
print(final-initial)
