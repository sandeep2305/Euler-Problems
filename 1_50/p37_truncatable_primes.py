'''The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes
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
trunt_prime=list()
num=11
while len(trunt_prime)<n:
	if isPrime(num):
		num_str=str(num)
		check_flag=list()
		for k in range(len(num_str)):
			trunt_1=int(''.join(num_str[k:]))
			trunt_2=int(''.join('0'+num_str[:-k-1]))
			if trunt_2==0:
				trunt_2=3
			if isPrime(trunt_1) and isPrime(trunt_2):
				check_flag.append(True)
			else:
				check_flag.append(False)
		if all(check_flag):
			trunt_prime.append(num)
			print(num)
	
	num+=2
print(sum(trunt_prime))
