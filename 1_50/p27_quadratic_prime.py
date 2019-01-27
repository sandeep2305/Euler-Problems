'''Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.'''
import time

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    
    return True
    
def PrimeGenerate(n):
	num=1
	if n<2: return []
	prime_num=[2]
	while num<=n:
		if isPrime(num):
			prime_num.append(num)
		num+=2
	return prime_num

n=int(input())
initial=time.time()
max_prime=0
prime_list=PrimeGenerate(n)
for b in prime_list:
	for a in range(-(b-2),n+1,2):
		count=0
		flag=True
		while flag:
			new_num= count**2+a*count+b
			if not isPrime(new_num):
				flag=False
			count+=1
		if (count-1)>max_prime:
			max_prime=count-1
			a_coefi=a
			b_coefi=b
final=time.time()
print(max_prime,a_coefi,b_coefi)
print(a_coefi*b_coefi)
print(final-initial)

