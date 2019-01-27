#nth prime number in series 
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

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
count=1
num=1
prime_num=[2]
while count<n:
	if isPrime(num):
		count+=1
		prime_num.append(num)
	num+=2
print(max(prime_num))
