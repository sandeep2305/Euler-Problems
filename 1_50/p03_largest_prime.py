#Largest prime factor of a number
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    

    return True
    
n=int(input())
factor_max=0
k=1
while k<=n:
	if n%k==0:
		if isPrime(k) and k>factor_max:
			factor_max=k
		n=n/k
	k=k+1
print(factor_max)
